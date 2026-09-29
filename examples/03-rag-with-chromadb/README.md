Question
↓
Chroma retrieval
↓
Context
↓
LLM
↓
Answer

# RAG with ChromaDB

This example demonstrates:

Question
↓
Retrieval
↓
Knowledge Base
↓
LLM Answer

---

# Create Environment

```bash
python -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

or

```powershell
.venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install chromadb ollama
```

---

# Prepare Knowledge Base

Add files to:

```text
kb/
```

Run:

```bash
python ingest.py
```

---

# Start Chat

```bash
python rag_chat.py
```

Example:

```text
> What is the ABCDE assessment?
```

The answer will be generated using retrieved content from ChromaDB.