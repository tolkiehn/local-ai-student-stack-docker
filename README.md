# Local AI Infrastructure

A reusable Docker-based local AI platform for healthcare simulation, AI prototyping, agent development, Retrieval-Augmented Generation (RAG), and student projects.

This repository provides a complete local AI stack consisting of:

- Ollama (local LLM runtime)
- Open WebUI (browser-based chat interface)
- Langflow (visual workflow builder)
- ChromaDB (vector database for RAG)

The goal is to provide a reproducible, version-controlled AI environment that can be used by lecturers, students, project teams, and researchers.

---

# Why This Stack?

Modern AI projects typically require multiple components:

| Component | Purpose |
|------------|------------|
| Ollama | Run LLMs locally on your computer |
| Open WebUI | Chat interface similar to ChatGPT |
| Langflow | Build workflows and AI pipelines visually |
| ChromaDB | Store embeddings and enable Retrieval-Augmented Generation (RAG) |
| Docker | Create reproducible environments across operating systems |

This repository packages all of these components into a single reproducible Docker setup.

---

# Architecture

```text
┌─────────────────────┐
│     Open WebUI      │
│   Browser Chat UI   │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│       Ollama        │
│ Local LLM Runtime   │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│      Langflow       │
│ Visual Workflows    │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│      ChromaDB       │
│   Vector Storage    │
└─────────────────────┘
```

---

# System Requirements

## Recommended

- 16 GB RAM
- 20+ GB free disk space
- Multi-core processor
- Stable internet connection

## Minimum

- 8 GB RAM
- Small language models only

---

# Installation Prerequisites

## Install Docker Desktop

This project requires Docker Desktop.

### Download

Download Docker Desktop from:

https://www.docker.com/products/docker-desktop/

### Installation

Follow the installer instructions for your operating system.

### Important

After installation:

1. Start Docker Desktop.
2. Wait until Docker reports it is running.
3. Ensure Docker shows a green status indicator.

### Verify Installation

macOS / Linux:

```bash
docker --version
docker compose version
```

Windows PowerShell:

```powershell
docker --version
docker compose version
```

Expected output:

```text
Docker version XX.XX.XX
Docker Compose version XX.XX.XX
```

If either command fails, Docker is not installed correctly.

---

## Install Git

Verify Git installation:

```bash
git --version
```

If Git is not installed:

https://git-scm.com/downloads

---

# Getting Started

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_ORGANISATION/local-ai-infrastructure.git

cd local-ai-infrastructure
```

---

## 2. Create Environment Configuration

Copy the example file:

macOS/Linux:

```bash
cp .env.example .env
```

Windows:

```powershell
copy .env.example .env
```

---

## 3. Configure Langflow Login

Open the file:

```text
.env
```

Example:

```dotenv
OLLAMA_PORT=11434
OPEN_WEBUI_PORT=8080
LANGFLOW_PORT=7860
CHROMA_PORT=8000

LANGFLOW_SUPERUSER=admin
LANGFLOW_SUPERUSER_PASSWORD=CHANGE_THIS_PASSWORD
LANGFLOW_AUTO_LOGIN=false
```

Use a strong password.

Never commit `.env` to Git.

---

## 4. Start the Infrastructure

Start all services:

```bash
docker compose up -d
```

On the first startup Docker will:

- download required images
- create volumes
- create networks
- start all services

This may take several minutes.

---

## 5. Verify Containers

Check container status:

```bash
docker compose ps
```

Expected:

```text
ollama       running
open-webui   running
langflow     running
chromadb     running
```

If a service is not running:

```bash
docker compose logs SERVICE_NAME
```

Example:

```bash
docker compose logs langflow
```

---

# Access the Services

After startup:

| Service | URL |
|----------|----------|
| Open WebUI | http://localhost:8080 |
| Langflow | http://localhost:7860 |
| Ollama API | http://localhost:11434 |
| ChromaDB API | http://localhost:8000 |

---

# First Login

## Open WebUI

Open:

```text
http://localhost:8080
```

Create your account.

---

## Langflow

Open:

```text
http://localhost:7860
```

Login using:

```text
Username: admin
Password: <password from .env>
```

---

# Install Language Models

After Ollama is running:

## Recommended Starter Model

```bash
docker compose exec ollama ollama pull llama3.2:3b
```

## Alternative Model

```bash
docker compose exec ollama ollama pull qwen3:4b
```

## Embedding Model

```bash
docker compose exec ollama ollama pull nomic-embed-text
```

## List Installed Models

```bash
docker compose exec ollama ollama list
```

Expected:

```text
NAME
llama3.2:3b
nomic-embed-text
```

---

# Verify the Installation

## Test Ollama

Run:

```bash
docker compose exec ollama ollama run llama3.2:3b
```

Send:

```text
Explain machine learning in one paragraph.
```

If a response appears, Ollama works correctly.

---

## Test Open WebUI

1. Open Open WebUI.
2. Select the installed model.
3. Send a message.

If a response appears, Open WebUI works correctly.

---

## Test Langflow

Create a simple workflow:

```text
Chat Input
      ↓
Prompt
      ↓
Ollama
      ↓
Chat Output
```

Run the workflow.

If the flow executes successfully, Langflow works correctly.

---

## Test ChromaDB

Verify container:

```bash
docker compose ps
```

Check the endpoint:

```bash
curl http://localhost:8000
```

A response confirms that ChromaDB is reachable.

### Important

A new ChromaDB installation is initially empty.

This is expected.

Collections, embeddings and documents will only appear after applications start storing data.

---

# Common Docker Commands

## Start

```bash
docker compose up -d
```

## Stop

```bash
docker compose down
```

## Restart

```bash
docker compose restart
```

## View Logs

```bash
docker compose logs -f
```

## View Logs for One Service

```bash
docker compose logs -f langflow
```

## Show Running Containers

```bash
docker compose ps
```

---

# Updating the Stack

## Pull Latest Images

```bash
docker compose pull
```

## Recreate Containers

```bash
docker compose up -d
```

---

# Repository Structure

```text
local-ai-infrastructure/
│
├── README.md
├── docker-compose.yml
├── .env.example
├── .gitignore
│
├── docs/
│   ├── architecture.md
│   ├── setup.md
│   ├── troubleshooting.md
│   └── security.md
│
├── scripts/
│   ├── start.sh
│   ├── stop.sh
│   └── backup.sh
│
└── examples/
```

---

# Typical Student Workflow

1. Pull latest repository changes.
2. Start Docker stack.
3. Open Open WebUI.
4. Open Langflow.
5. Install required models.
6. Develop AI workflows.
7. Connect projects to Ollama and ChromaDB.
8. Commit work to project repositories.

Infrastructure should remain separate from project-specific repositories.

---

# Security

Never commit:

```text
.env
Passwords
API keys
Tokens
Secrets
Database exports
```

Always check:

```bash
git status
```

before committing.

---

# Troubleshooting

## Docker Does Not Start

Verify Docker Desktop is running.

Check:

```bash
docker ps
```

---

## Langflow Immediately Stops

Inspect logs:

```bash
docker compose logs langflow
```

Usually caused by:

- missing username
- missing password
- invalid environment variables

Verify:

```text
LANGFLOW_SUPERUSER
LANGFLOW_SUPERUSER_PASSWORD
```

exist inside `.env`.

---

## Open WebUI Shows No Models

Verify Ollama is running:

```bash
docker compose ps
```

Verify models:

```bash
docker compose exec ollama ollama list
```

If no models exist:

```bash
docker compose exec ollama ollama pull llama3.2:3b
```

---

## ChromaDB Appears Empty

This is expected on first startup.

ChromaDB does not contain data until:

- embeddings are generated
- collections are created
- documents are stored

An empty database does not indicate an error.

---

## Port Already In Use

Check:

```bash
docker compose logs
```

Possible cause:

- another Ollama instance
- another Langflow instance
- another service already using the port

Change ports in:

```text
.env
```

Example:

```dotenv
OPEN_WEBUI_PORT=8081
```

Restart:

```bash
docker compose up -d
```

---

# Git Workflow

## First Commit

```bash
git add .

git commit -m "Initial local AI infrastructure"
```

---

## Push Changes

```bash
git push origin main
```

---

## Create Release Tag

```bash
git tag v0.1.0

git push origin v0.1.0
```

---

# Future Extensions

Possible future additions:

- PostgreSQL
- Monitoring (Grafana)
- Reverse Proxy (Nginx)
- Authentication Providers
- Backup Automation
- Model Versioning
- Multi-User Support
- CI/CD Pipelines
- Automated Evaluation Workflows

---

# License

Add the licence appropriate for your organisation, institution, or project.


# Local AI Infrastructure

Reusable local AI platform for healthcare simulation projects.

## Components

- Ollama
- Open WebUI
- Langflow
- ChromaDB

## Start

docker compose up -d

## Stop

docker compose down

## Services

Open WebUI:
http://localhost:8080

Ollama:
http://localhost:11434

Langflow:
http://localhost:7860

ChromaDB:
http://localhost:8000