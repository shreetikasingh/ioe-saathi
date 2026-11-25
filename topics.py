# topics.py - use Gemini to tag every past question with a syllabus topic
# Output: topics.json        -> the list of topics for each subject
#         topic_labels.json  -> {question id: topic}

import json
import os
import time
from collections import defaultdict
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import errors, types
from pydantic import BaseModel

# ---------- Settings ----------
CHUNKS_FILE = Path("chunks.json")
TOPICS_FILE = Path("topics.json")
LABELS_FILE = Path("topic_labels.json")
BATCH_SIZE = 40
MODELS = ["gemini-3.6-flash", "gemini-3.5-flash-lite", "gemini-3.8-flash"]

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


class TopicLabel(BaseModel):
    """The shape of each answer we want back from Gemini."""
    id: str
    topic: str


def ask_json(prompt, schema):
    """Ask Gemini and force the answer to be JSON in the given shape."""
    for model_name in MODELS:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=schema,
                ),
            )
            return json.loads(response.text)
        except errors.APIError as e:
            print(f"   {model_name} failed (error {e.code}), trying next...")
        except json.JSONDecodeError:
            print(f"   {model_name} returned broken JSON, trying next...")
    return None


def load_json(path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def save_json(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


# ---------- Step 1: decide the topics for each subject ----------
def discover_topics(subject, chunks):
    questions = "\n".join(f"- {c['text'][:160]}" for c in chunks)
    prompt = (
        f"Below are past exam questions from the IOE (Tribhuvan University, Nepal) subject '{subject}'.\n"
        "Group them into 8 to 12 main topics that roughly match the chapters of the course syllabus.\n"
        "Use short, clear topic names (2 to 5 words), e.g. 'Z-Transform' or 'FIR Filter Design'.\n"
        "Return only the list of topic names.\n\n"
        f"QUESTIONS:\n{questions}"
    )
    return ask_json(prompt, list[str])


# ---------- Step 2: tag each question with one topic ----------
def label_batch(batch, topics):
    questions = "\n\n".join(f"ID: {c['id']}\n{c['text'][:400]}" for c in batch)
    prompt = (
        "Assign each exam question below to exactly ONE topic from this list:\n"
        + "\n".join(f"- {t}" for t in topics)
        + "\n\nIf a question covers several topics, pick the main one. "
        "If none fit, use 'Other'. Copy the topic name exactly.\n\n"
        f"QUESTIONS:\n{questions}"
    )
    return ask_json(prompt, list[TopicLabel])


if __name__ == "__main__":
    chunks = load_json(CHUNKS_FILE, [])
    topics = load_json(TOPICS_FILE, {})
    labels = load_json(LABELS_FILE, {})

    by_subject = defaultdict(list)
    for chunk in chunks:
        by_subject[chunk["subject"]].append(chunk)

    for subject, subject_chunks in by_subject.items():
        print(f"\n=== {subject.upper()}: {len(subject_chunks)} questions ===")

        # Step 1 (skipped if we already have topics for this subject)
        if subject not in topics:
            print("Finding the main topics...")
            found = discover_topics(subject, subject_chunks)
            if not found:
                print("Could not get topics right now. Run the script again later.")
                continue
            topics[subject] = found
            save_json(TOPICS_FILE, topics)
        print("Topics:", ", ".join(topics[subject]))

        # Step 2 (only questions that don't have a label yet)
        todo = [c for c in subject_chunks if c["id"] not in labels]
        allowed = set(topics[subject])
        for start in range(0, len(todo), BATCH_SIZE):
            batch = todo[start:start + BATCH_SIZE]
            print(f"Labelling questions {start + 1}-{start + len(batch)} of {len(todo)}...")
            result = label_batch(batch, topics[subject])
            if not result:
                print("   Batch failed. Run the script again later to finish.")
                continue
            batch_ids = {c["id"] for c in batch}
            for item in result:
                if item["id"] in batch_ids:
                    labels[item["id"]] = item["topic"] if item["topic"] in allowed else "Other"
            save_json(LABELS_FILE, labels)  # save progress after every batch
            time.sleep(4)

    # ---------- Summary ----------
    print("\n=== Questions per topic ===")
    counts = defaultdict(int)
    for chunk in chunks:
        topic = labels.get(chunk["id"])
        if topic:
            counts[(chunk["subject"], topic)] += 1
    for (subject, topic), n in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"{subject.upper():6} {topic:35} {n}")