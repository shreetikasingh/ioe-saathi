# rag.py - the full RAG pipeline: question -> search -> AI answer with sources

import json
import os
import re
import chromadb
from dotenv import load_dotenv
from google import genai
from google.genai import errors, types

# ---------- Settings ----------
DB_FOLDER = "chroma_db"
COLLECTION_NAME = "ioe_docs"
NUM_RESULTS = 6  # how many past questions to give the AI
MODELS = ["gemini-3.6-flash", "gemini-3.5-flash-lite", "gemini-3.8-flash"]

SYSTEM_INSTRUCTION = """You are IOE Saathi, a friendly study assistant for students of the
Institute of Engineering (IOE), Tribhuvan University, Nepal. Right now you cover
Digital Signal Analysis and Processing (DSP).

You will be given CONTEXT: real past exam questions, each labelled like [DSP | 2082 Baishakh | Q3].

Rules:
1. If the student's question is about DSP or any topic that appears in the CONTEXT,
   ANSWER it helpfully: explain the concept simply using your own knowledge,
   then list the related past questions from the CONTEXT with their citations,
   e.g. (2082 Baishakh, Q3).
2. If the student asks which questions or topics have come in exams, list the matching
   questions from the CONTEXT with their citations.
3. Only cite labels that actually appear in the CONTEXT. Never invent questions,
   exam years or question numbers.
4. Only if the question has nothing to do with DSP (for example general knowledge or
   another subject), reply: "I couldn't find this in the past papers I have. I can help
   with DSP concepts and past questions."
5. Keep answers clear and concise. Use LaTeX for math.
6. Reply in the same language the student used: Nepali in Devanagari gets a Nepali
   answer, Romanized Nepali (e.g. "FFT ke ho?") gets a Romanized Nepali answer, and
   English gets English. Keep technical terms (FFT, Z-transform, ROC...) in English.
"""

# Turns a student's question into a good search query (and translates Nepali)
REWRITE_INSTRUCTION = """Rewrite the student's question into a short English search query
for a database of DSP (Digital Signal Processing) exam questions.
- Translate Nepali (Devanagari or Romanized) into English.
- Replace everyday descriptions with standard DSP terms, e.g.
  "ripples when we truncate the impulse response" -> "Gibbs phenomenon in FIR filter design".
- Keep formulas, numbers, years and question numbers.
- Return ONLY the search query, nothing else."""
REWRITE_MODELS = ["gemini-3.5-flash-lite", "gemini-3.6-flash", "gemini-3.8-flash"]

# ---------- Setup ----------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    # On Streamlit Cloud the key lives in "Secrets" instead of a .env file
    try:
        import streamlit as st
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass
# Give up on a slow request after 60 s and retry at most twice, so nobody waits forever
ai_client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(
        timeout=60_000,  # milliseconds
        retry_options=types.HttpRetryOptions(attempts=2),
    ),
)
db_client = chromadb.PersistentClient(path=DB_FOLDER)
collection = db_client.get_or_create_collection(COLLECTION_NAME)


def build_database_if_empty():
    """Make sure the database matches chunks.json. On a fresh server (like Streamlit
    Cloud) it's empty, and after adding subjects it's out of date: rebuild in both cases."""
    with open("chunks.json", encoding="utf-8") as f:
        chunks = json.load(f)
    if collection.count() == len(chunks):
        return  # database is already up to date
    # Out of date (e.g. new subjects were added): wipe it and rebuild
    existing = collection.get()["ids"]
    if existing:
        collection.delete(ids=existing)
    ids, documents, metadatas, seen = [], [], [], set()
    for chunk in chunks:
        chunk_id = chunk["id"]
        while chunk_id in seen:
            chunk_id += "-dup"
        seen.add(chunk_id)
        ids.append(chunk_id)
        documents.append(chunk["text"])
        metadatas.append({k: chunk[k] for k in ("subject", "source", "page", "exam", "question_no")})
    collection.add(ids=ids, documents=documents, metadatas=metadatas)


build_database_if_empty()


# ---------- The three steps of RAG ----------
def rewrite_query(question):
    """Ask a small, fast model to turn the question into a better English search query.
    If every model fails, we simply search with the original question."""
    for model_name in REWRITE_MODELS:
        try:
            response = ai_client.models.generate_content(
                model=model_name,
                contents=question,
                config=types.GenerateContentConfig(system_instruction=REWRITE_INSTRUCTION),
            )
            query = (response.text or "").strip()
            if query:
                return query
        except Exception:
            continue
    return question


def retrieve(question, rewrite=True):
    """R: find the past questions closest in meaning to the student's question.
    We search with BOTH the improved query and the original, improved results first."""
    queries = [rewrite_query(question), question] if rewrite else [question]
    results = collection.query(query_texts=queries, n_results=NUM_RESULTS)
    combined = []
    for docs in results["documents"]:  # one list of results per query
        for doc in docs:
            if doc not in combined:
                combined.append(doc)
    return combined[:NUM_RESULTS]


def build_prompt(question, context_chunks):
    """A: augment the question with the retrieved context."""
    context = "\n\n".join(context_chunks)
    return f"CONTEXT:\n{context}\n\nSTUDENT'S QUESTION:\n{question}"


def generate(prompt):
    """G: ask Gemini to answer, trying each model until one works."""
    for model_name in MODELS:
        try:
            response = ai_client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(system_instruction=SYSTEM_INSTRUCTION),
            )
            return response.text
        except Exception as e:  # busy, quota, timeout... try the next model
            print(f"   ({model_name} failed: {getattr(e, 'code', type(e).__name__)}, trying next...)")
    return "Sorry, all AI models are busy right now. Please try again in a minute."


def ask(question, show_sources=True):
    """The whole pipeline in one function."""
    context_chunks = retrieve(question)
    if show_sources:
        # The first line of each chunk is its label, e.g. [DSP | 2082 Baishakh | Q3]
        labels = [chunk.splitlines()[0] for chunk in context_chunks]
        print("   Retrieved:", ", ".join(labels))
    prompt = build_prompt(question, context_chunks)
    return generate(prompt)


# ---------- Solve mode: step-by-step solutions, with Python to check the math ----------
SOLVE_INSTRUCTION = """You are IOE Saathi, a DSP tutor for IOE (Tribhuvan University, Nepal) students.
Solve the student's numerical problem step by step, like a model answer in an exam copy.

Rules:
1. Write the formula or method before each step, then substitute the numbers.
2. Use the Python code execution tool (NumPy / SciPy are available) to CHECK every
   calculation: convolutions, DFT/FFT values, partial fractions, filter coefficients.
   Never rely on mental arithmetic. If the code disagrees with your working, fix the working.
3. End with the final answer clearly marked as **Final answer:**.
4. If the CONTEXT contains the same or a similar past question, mention it, e.g. (asked in 2082 Baishakh, Q3).
5. Use LaTeX for math. Keep explanations short and exam-focused.
"""

# Matches things like "2082 Baishakh Q3", "2081 bhadra q.2", "2079 Q 10"
EXAM_REFERENCE = re.compile(r"(20\d\d)\s*([A-Za-z]+)?.*?\bQ\.?\s*(\d{1,2})\b", re.IGNORECASE)


def find_exact_question(question):
    """If the student names a paper and question number, fetch exactly that question."""
    match = EXAM_REFERENCE.search(question)
    if not match:
        return None
    year, session, q_no = match.group(1), match.group(2), int(match.group(3))
    found = collection.get(where={"question_no": q_no}, include=["documents", "metadatas"])
    for doc, meta in zip(found["documents"], found["metadatas"]):
        if meta["exam"].startswith(year) and (not session or session.lower() in meta["exam"].lower()):
            return doc
    return None


def solve(question):
    """Solve a numerical problem. Returns (answer_text, python_code_used, context_chunks)."""
    exact = find_exact_question(question)
    context_chunks = [exact] if exact else retrieve(question)[:3]
    prompt = build_prompt(question, context_chunks)
    if exact:
        prompt += "\n\nThe student wants you to solve the past question shown in the CONTEXT."

    for model_name in MODELS:
        try:
            response = ai_client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SOLVE_INSTRUCTION,
                    tools=[types.Tool(code_execution=types.ToolCodeExecution())],
                ),
            )
            # The answer comes back in pieces: text, the code it wrote, and the code's output
            text_parts, code_parts = [], []
            for part in response.candidates[0].content.parts:
                if part.text:
                    text_parts.append(part.text)
                if part.executable_code:
                    code_parts.append(part.executable_code.code)
                if part.code_execution_result and part.code_execution_result.output:
                    code_parts.append("# Output:\n# " + part.code_execution_result.output.strip().replace("\n", "\n# "))
            return "\n\n".join(text_parts), "\n\n".join(code_parts), context_chunks
        except Exception as e:  # busy, quota, timeout... try the next model
            print(f"   ({model_name} failed: {getattr(e, 'code', type(e).__name__)}, trying next...)")
    return "Sorry, all AI models are busy right now. Please try again in a minute.", "", context_chunks


# ---------- Chat in the terminal ----------
if __name__ == "__main__":
    print("IOE Saathi is ready! Ask about DSP past questions. Type 'exit' to quit.\n")
    while True:
        question = input("You: ").strip()
        if question.lower() in ("exit", "quit"):
            print("Bye! All the best for your exams.")
            break
        if not question:
            continue
        print("\nIOE Saathi:", ask(question), "\n")