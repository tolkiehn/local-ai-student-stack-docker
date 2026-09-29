import chromadb

client = chromadb.PersistentClient(
    "./chroma"
)

collection = client.get_collection(
    "ems_protocols"
)

result = collection.query(
    query_texts=[
        "What is ABCDE?"
    ],
    n_results=3
)

print(result)