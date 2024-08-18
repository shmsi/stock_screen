import redis
from .config import settings


redis_client = redis.Redis(
    host=settings.redis_host, port=settings.redis_port, decode_responses=True
)


