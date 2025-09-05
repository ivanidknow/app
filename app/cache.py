from typing import Optional
from redis.asyncio import Redis
from .config import settings

_redis: Optional[Redis] = None

def get_redis() -> Redis:
    global _redis
    if _redis is None:
        _redis = Redis.from_url(settings.REDIS_URL, encoding="utf-8", decode_responses=True)
    return _redis

async def redis_health() -> bool:
    r = get_redis()
    try:
        pong = await r.ping()
        return bool(pong)
    except Exception:
        return False
