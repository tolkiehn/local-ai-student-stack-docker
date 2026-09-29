# Setup Guide

This document provides a quick way to verify that the Local AI Infrastructure is working.

---

# Start Infrastructure

```bash
docker compose up -d
```

---

# Verify Containers

```bash
docker compose ps
```

Expected:

```text
ollama
open-webui
langflow
chromadb
```

all running.

---

# Verify Open WebUI

Open:

```text
http://localhost:8080
```

You should see a chat interface.

---

# Verify Langflow

Open:

```text
http://localhost:7860
```

You should see the Langflow editor.

---

# Verify Ollama

```bash
docker compose exec ollama ollama list
```

---

# Verify ChromaDB

```bash
curl http://localhost:8000
```

---

# Install Recommended Models

```bash
docker compose exec ollama ollama pull llama3.2:3b

docker compose exec ollama ollama pull nomic-embed-text
```

---

# Success Criteria

Your installation is successful if:

- Ollama responds
- Open WebUI loads
- Langflow loads
- ChromaDB responds
- A model can answer a prompt