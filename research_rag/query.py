print("STEP 1 - Query script started")

import json
from endee import Endee
from sentence_transformers import SentenceTransformer

INDEX_NAME = "dash1"

client = Endee("localhost:8080")
index = client.get_index(INDEX_NAME)

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Model loaded.\n")

with open("metadata_store.json", "r", encoding="utf-8") as f:
    metadata_store = json.load(f)

while True:
    query = input("Enter your question (or type exit): ")

    if query.lower() == "exit":
        break

    print("Embedding query...")
    vector = model.encode(query).tolist()

    print("Searching...")

    results = index.query(vector, 5)

    print("\nTop Results:\n")

    for i, item in enumerate(results):
        vector_id = item.get("id")
        score = item.get("score") or item.get("distance")

        metadata = metadata_store.get(vector_id)

        print(f"Result {i+1}")
        print("Score:", score)

        if metadata:
            print("Source:", metadata["source"])
            print("Text:", metadata["text"])
        else:
            print("Metadata not found.")

        print("-" * 60)