import redis
from .config import settings
import logging


redis_client = redis.Redis(
    host=settings.redis_host, port=settings.redis_port, decode_responses=True
)


def create_timeseries(client: redis.Redis, retention_msecs=None, labels=None):
    logging.info("Creating timeseries")
    client.ts().create(
        key=settings.ts_key, retention_msecs=retention_msecs, labels=labels
    )


def add_data(client: redis.Redis, timestamp, value):
    logging.info(f"Adding data to timeseries for {settings.ts_key}")
    client.ts().add(settings.ts_key, timestamp, value)
