# SRE Health Check API

A beginner-friendly SRE project built with Python, FastAPI, and Docker.
Demonstrates health check endpoints, structured logging, Docker containerization,
and readiness/liveness probes — concepts used in real-world SRE and DevOps environments.

---

## Endpoints

| Endpoint   | Purpose                          |
|------------|----------------------------------|
| `/`        | Root — confirms app is running   |
| `/health`  | Liveness check                   |
| `/ready`   | Readiness check with dependency  |
| `/metrics` | Basic uptime and system metrics  |
| `/docs`    | Auto-generated API documentation |

---

## How to run

### With Docker Compose (recommended)
```bash
docker-compose up --build
```

### Without Docker (local)
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open browser: http://localhost:8000/docs

---

## Concepts covered
- FastAPI REST API development
- Health check and readiness probe design (used in Kubernetes)
- Structured JSON logging
- Docker containerization
- Docker Compose orchestration
- Uptime and metrics tracking
