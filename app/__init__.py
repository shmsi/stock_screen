import redis
from fastapi import FastAPI
from confluent_kafka import Consumer, KafkaException, KafkaError
import threading
from .config import settings
from .routes import router
from .data_stream import redis_client

app = FastAPI()


def consume_kafka():
    conf = {
        "bootstrap.servers": settings.kafka_bootstrap_servers,
        "group.id": "my_consumer_group",
        "auto.offset.reset": "earliest",
    }
    print("sleeping for 10 seconds")
    import time 
    time.sleep(10)

    consumer = Consumer(conf)
    consumer.subscribe([settings.kafka_topic])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print("ERROR: End of partition")
                    continue
                else:
                    raise KafkaException(msg.error())
            else:
                # Message processing
                redis_client.set("latest_stock_price", msg.value().decode("utf-8"))
                print(f"Received message: {msg.value().decode('utf-8')}")

    finally:
        # Clean up the consumer on exit
        consumer.close()


@app.on_event("startup")
def startup_event():
    thread = threading.Thread(target=consume_kafka)
    thread.start()


app.include_router(router)
