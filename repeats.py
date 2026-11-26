# repeats.py - find past questions that were asked again and again (no AI calls, free)
#
# Idea: turn every question into an embedding (numbers that capture its meaning).
# Two questions from DIFFERENT exams whose embeddings are very similar = a repeat.
# Output: repeats.json

import json
from collections import defaultdict

import numpy as np
from chromadb.utils import embedding_functions

CHUNKS_FILE = "chunks.json"
LABELS_FILE = "topic_labels.json"
OUTPUT_FILE = "repeats.json"

# How similar two questions must be to count as "the same question" (0 to 1).
# Higher = stricter. We'll look at the results and tune this.
THRESHOLD = 0.85


def question_body(chunk):
    """Drop the '[DSP | 2082 Baishakh | Q3]' label and the question number,
    so only the actual question wording is compared."""
    body = chunk["text"].split("\n", 1)[-1]
    body = body.split(".", 1)[-1] if body[:3].strip().rstrip(".").isdigit() else body
    return body.replace("***", "").strip()


class Groups:
    """Union-find: a classic way to merge items into groups.
    If A~B and B~C, then A, B and C all end up in one group."""

    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        while self.parent[i] != i:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def join(self, a, b):
        self.parent[self.find(a)] = self.find(b)


if __name__ == "__main__":
    chunks = json.load(open(CHUNKS_FILE, encoding="utf-8"))
    try:
        labels = json.load(open(LABELS_FILE, encoding="utf-8"))
    except FileNotFoundError:
        labels = {}

    print(f"Embedding {len(chunks)} questions (runs on your laptop)...")
    embed = embedding_functions.DefaultEmbeddingFunction()
    vectors = np.array(embed([question_body(c) for c in chunks]), dtype=float)

    # Cosine similarity of every question with every other question
    vectors /= np.linalg.norm(vectors, axis=1, keepdims=True)
    similarity = vectors @ vectors.T

    groups = Groups(len(chunks))
    for i in range(len(chunks)):
        for j in range(i + 1, len(chunks)):
            same_subject = chunks[i]["subject"] == chunks[j]["subject"]
            different_exam = chunks[i]["exam"] != chunks[j]["exam"]
            if same_subject and different_exam and similarity[i, j] >= THRESHOLD:
                groups.join(i, j)

    # Collect the groups that contain questions from 2 or more different exams
    members = defaultdict(list)
    for i in range(len(chunks)):
        members[groups.find(i)].append(i)

    repeats = []
    for idx in members.values():
        exams = {chunks[i]["exam"] for i in idx}
        if len(exams) < 2:
            continue
        # Show the newest version as the "main" wording
        idx.sort(key=lambda i: chunks[i]["exam"], reverse=True)
        repeats.append({
            "subject": chunks[idx[0]]["subject"],
            "times_asked": len(exams),
            "topic": labels.get(chunks[idx[0]]["id"], "Other"),
            "question": question_body(chunks[idx[0]]),
            "asked_in": [
                {"id": chunks[i]["id"], "exam": chunks[i]["exam"], "question_no": chunks[i]["question_no"]}
                for i in idx
            ],
        })

    repeats.sort(key=lambda r: -r["times_asked"])
    json.dump(repeats, open(OUTPUT_FILE, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    repeated_questions = sum(len(r["asked_in"]) for r in repeats)
    print(f"\nFound {len(repeats)} repeated questions "
          f"(covering {repeated_questions} of {len(chunks)} past questions)\n")
    for r in repeats[:8]:
        where = ", ".join(f"{a['exam']} Q{a['question_no']}" for a in r["asked_in"])
        print(f"🔁 {r['times_asked']}x  [{r['topic']}]  {r['question'][:90]}...")
        print(f"      asked in: {where}\n")
    print(f"Saved to {OUTPUT_FILE}")