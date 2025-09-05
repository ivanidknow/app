import asyncio
from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from prometheus_fastapi_instrumentator import Instrumentator

from .config import settings
from .db import db_health
from .cache import redis_health

app = FastAPI(title=settings.APP_NAME)

# /metrics для Prometheus
if settings.METRICS_ENABLED:
    Instrumentator().instrument(app).expose(app, include_in_schema=False, endpoint="/metrics")

@app.get("/ping", response_class=PlainTextResponse, summary="Liveness ping")
async def ping() -> str:
    return "pong"

@app.get("/healthz", summary="DB & Redis health")
async def healthz() -> JSONResponse:
    db_ok, redis_ok = await asyncio.gather(db_health(), redis_health())
    status = "ok" if (db_ok and redis_ok) else "degraded"
    return JSONResponse({
        "status": status,
        "postgres": db_ok,
        "redis": redis_ok,
    })
