# embed.py - turn every chunk into an embedding and store it in ChromaDB

import json
import chromadb

CHUNKS_FILE = "chunks.json"
DB_FOLDER = "chroma_db"
COLLECTION_NAME = "ioe_docs"

# 1. Load the chunks we made with chunker.py
with open(CHUNKS_FILE, encoding="utf-8") as f:
    chunks = json.load(f)
print(f"Loaded {len(chunks)} chunks")

# 2. Open (or create) a database that is saved in the chroma_db folder
client = chromadb.PersistentClient(path=DB_FOLDER)

# Start fresh every time we run this, so re-running never creates duplicates
try:
    client.delete_collection(COLLECTION_NAME)
except Exception:
    pass  # it didn't exist yet, that's fine
collection = client.create_collection(COLLECTION_NAME)

# 3. Prepare the three lists ChromaDB needs: ids, texts, and labels (metadata)
ids, documents, metadatas = [], [], []
seen_ids = set()
for chunk in chunks:
    chunk_id = chunk["id"]
    # If the same id appears twice (rare formatting quirk), make it unique
    while chunk_id in seen_ids:
        chunk_id += "-dup"
    seen_ids.add(chunk_id)

    ids.append(chunk_id)
    documents.append(chunk["text"])
    metadatas.append({
        "subject": chunk["subject"],
        "source": chunk["source"],
        "page": chunk["page"],
        "exam": chunk["exam"],
        "question_no": chunk["question_no"],
    })

# 4. Add everything. ChromaDB turns each text into an embedding automatically.
print("Creating embeddings... (the first run downloads a small model, ~80 MB)")
collection.add(ids=ids, documents=documents, metadatas=metadatas)
print(f"Stored {collection.count()} chunks in the database\n")

# 5. Test: search by MEANING
test_question = "how to find the frequency spectrum quickly using butterfly diagram"
results = collection.query(query_texts=[test_question], n_results=3)

print(f"Test search: '{test_question}'\n")
for text, meta, distance in zip(
    results["documents"][0], results["metadatas"][0], results["distances"][0]
):
    print(f"--- {meta['exam']} | Q{meta['question_no']} | distance {distance:.3f} ---")
    print(text[:250])
    print()