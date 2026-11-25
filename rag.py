# rag.py - the full RAG pipeline: question -> search -> AI answer with sources

import os
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
"""

# ---------- Setup ----------
load_dotenv()
ai_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
db_client = chromadb.PersistentClient(path=DB_FOLDER)
collection = db_client.get_collection(COLLECTION_NAME)


# ---------- The three steps of RAG ----------
def retrieve(question):
    """R: find the past questions closest in meaning to the student's question."""
    results = collection.query(query_texts=[question], n_results=NUM_RESULTS)
    return results["documents"][0]


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
        except errors.APIError as e:
            print(f"   ({model_name} busy, error {e.code}, trying next...)")
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