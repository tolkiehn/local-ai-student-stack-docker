#!/bin/bash

echo "WARNING"
echo "This removes containers and volumes."

read -p "Continue? (y/N): " confirm

if [[ "$confirm" != "y" ]]; then
  echo "Cancelled."
  exit 0
fi

docker compose down -v

echo
echo "All containers and volumes removed."