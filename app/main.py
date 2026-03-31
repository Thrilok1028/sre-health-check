from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime, timezone
import logging
import sys
import platform
import time

# ── Structured JSON logging setup ──────────────────────────────────────────
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
)
logger = logging.getLogger(__name__)

# ── App startup ────────────────────────────────────────────────────────────
app = FastAPI(
    title="SRE Health Check API",
    description="A simple health check API built with FastAPI and Docker",
    version="1.0.0"
)

START_TIME = time.time()


# ── Routes ─────────────────────────────────────────────────────────────────

@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message": "SRE Health Check API is running", "docs": "/docs"}


@app.get("/health")
def health_check():
    """Basic liveness check — is the app running?"""
    logger.info("Health check requested")
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "service": "sre-health-check-api"
        }
    )


@app.get("/ready")
def readiness_check():
    """Readiness check — is the app ready to serve traffic?"""
    logger.info("Readiness check requested")
    # Simulate a dependency check (e.g., config loaded)
    checks = {
        "app": "ok",
        "config": "ok"
    }
    all_ready = all(v == "ok" for v in checks.values())
    status_code = 200 if all_ready else 503

    logger.info(f"Readiness result: {checks}")
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "ready" if all_ready else "not ready",
            "checks": checks,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    )


@app.get("/metrics")
def metrics():
    """Basic metrics endpoint — uptime, system info."""
    uptime_seconds = round(time.time() - START_TIME, 2)
    logger.info(f"Metrics requested — uptime: {uptime_seconds}s")
    return {
        "uptime_seconds": uptime_seconds,
        "python_version": platform.python_version(),
        "platform": platform.system(),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
