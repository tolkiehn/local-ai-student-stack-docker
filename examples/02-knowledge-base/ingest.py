from pathlib import Path
import chromadb

client = chromadb.PersistentClient("./chroma")

collection = client.get_or_create_collection(
    "ems_protocols"
)

documents = []
ids = []

for file in Path("kb").glob("*"):

    documents.append(
        file.read_text()
    )

    ids.append(
        file.stem.lower()
    )

collection.add(
    documents=documents,
    ids=ids
)

print(
    f"Added {len(documents)} files"
)