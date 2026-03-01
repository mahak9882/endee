from endee import Endee

INDEX_NAME = "dash1"

client = Endee("localhost:8080")

print("Deleting index if exists...")
try:
    client.delete_index(INDEX_NAME)
    print("Index deleted.")
except Exception as e:
    print("Index may not exist:", e)

print("Creating new index...")

client.create_index(
    name=INDEX_NAME,
    dimension=384,
    space_type="cosine",
    precision="float32"   # 🔥 REQUIRED
)

print("Index recreated successfully!")