# Langflow RAG Example

This example demonstrates a simple RAG workflow in Langflow.

---

# Architecture

```text
Chat Input
    ↓
Retriever
    ↓
Prompt
    ↓
Ollama
    ↓
Chat Output
```

---

# Import Flow

Open:

```text
http://localhost:7860
```

Select:

```text
Import Flow
```

Choose:

```text
flow.json
```

---

# Configure Ollama

Set URL:

```text
http://ollama:11434
```

or

```text
http://localhost:11434
```

depending on your environment.

---

# Configure Retriever

Point the retriever to:

```text
ChromaDB
```

Collection:

```text
ems_protocols
```

---

# Test

Example question:

```text
What is the ABCDE assessment?
```

Expected behaviour:

1. Retrieve relevant documents.
2. Insert retrieved context.
3. Send prompt to Ollama.
4. Return grounded answer.

---

# Learning Goals

After completing this example you should understand:

- Retrieval-Augmented Generation
- Embeddings
- Vector databases
- Langflow workflows
- Local AI architectures