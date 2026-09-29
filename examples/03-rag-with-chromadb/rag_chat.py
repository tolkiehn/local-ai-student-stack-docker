import chromadb
import ollama

client = chromadb.PersistentClient(
    "./chroma"
)

collection = client.get_collection(
    "ems_protocols"
)


def ask(question):

    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    context = "\n\n".join(
        results["documents"][0]
    )

    prompt = f"""
Answer the question using only the
provided context.

Context:
{context}

Question:
{question}
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":

    print("RAG Chat")
    print("Type 'quit' to stop.\n")

    while True:

        question = input("> ")

        if question.lower() == "quit":
            break

        answer = ask(question)

        print("\n" + answer + "\n")