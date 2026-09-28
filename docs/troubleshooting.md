## ChromaDB displays "No telemetry is configured"

This message is informational and does not indicate a startup failure.

Verify the service using:

    docker compose ps
    docker compose port chromadb 8000
    Test-NetConnection localhost -Port 8000
    Invoke-RestMethod http://localhost:8000/api/v2/heartbeat

ChromaDB is an API service and does not necessarily provide a graphical
web interface at its base address.

If the v2 heartbeat route is unavailable, inspect the container logs and
try the API route supported by the pinned ChromaDB version.