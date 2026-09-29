#!/bin/bash

mkdir -p backups

TIMESTAMP=$(date +%Y%m%d-%H%M%S)

echo "Creating backup..."

tar -czf \
backups/local-ai-backup-${TIMESTAMP}.tar.gz \
.env \
docker-compose.yml

echo "Backup created:"
echo "backups/local-ai-backup-${TIMESTAMP}.tar.gz"