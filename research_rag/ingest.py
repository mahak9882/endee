print("STEP 1 - Script started")

import os
import uuid
import json
from endee import Endee
from sentence_transformers import SentenceTransformer
from research_rag.utils import extract_text_from_pdf

print("STEP 2 - Imports done")

# =============================
# CONFIG
# =============================
INDEX_NAME = "dash1"
DATA_FOLDER = "data/papers"
CHUNK_SIZE = 1000
OVERLAP = 200

# =============================
# CHUNKING
# =============================
def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=OVERLAP):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# =============================
# CONNECT TO ENDEE
# =============================
print("Connecting to Endee...")
client = Endee("localhost:8080")
index = client.get_index(INDEX_NAME)

# =============================
# LOAD MODEL
# =============================
print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Model loaded.\n")

# =============================
# METADATA STORE
# =============================
metadata_store = {}

# =============================
# INGEST LOOP
# =============================
for filename in os.listdir(DATA_FOLDER):
    if not filename.endswith(".pdf"):
        continue

    print(f"\nIngesting {filename}...")

    filepath = os.path.join(DATA_FOLDER, filename)
    text = extract_text_from_pdf(filepath)

    if not text.strip():
        print("No text extracted. Skipping.")
        continue

    chunks = chunk_text(text)
    print(f"Total chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")

        embedding = model.encode(
            chunk,
            show_progress_bar=False,
            convert_to_numpy=True,
            normalize_embeddings=False
        ).tolist()

        vector_id = str(uuid.uuid4())

        vector_data = {
            "id": vector_id,
            "vector": embedding
        }

        index.upsert([vector_data])

        # Store metadata locally
        metadata_store[vector_id] = {
            "source": filename,
            "text": chunk[:1000]
        }

    print(f"Finished {filename}")

# Save metadata file
with open("metadata_store.json", "w", encoding="utf-8") as f:
    json.dump(metadata_store, f, indent=2, ensure_ascii=False)

print("\nIngestion completed successfully!")