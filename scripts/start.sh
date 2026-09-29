#!/bin/bash

echo "Starting Local AI Infrastructure..."

docker compose up -d

echo
echo "Checking services..."
docker compose ps

echo
echo "Services should be available at:"

echo "Open WebUI: http://localhost:8080"
echo "Langflow:   http://localhost:7860"
echo "Ollama:     http://localhost:11434"
echo "ChromaDB:   http://localhost:8000"