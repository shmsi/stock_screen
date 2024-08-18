
from pydantic import BaseSettings

class Settings(BaseSettings):
    redis_host: str = "redis"
    redis_port: int = 6379
    kafka_bootstrap_servers: str = "kafka:9092"
    kafka_topic: str = "stock_prices"

settings = Settings()
