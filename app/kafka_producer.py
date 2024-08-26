from confluent_kafka import Producer
import json
import time
import random

conf = {"bootstrap.servers": "kafka:9092"}

producer = Producer(**conf)


def delivery_report(err, msg):
    """Called once for each message produced to indicate delivery result.
    Triggered by poll() or flush()."""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


while True:
    stock_price = {"symbol": "AAPL", "price": round(random.uniform(150, 160), 2), "timestamp": int(time.time())}
    # Produce the message asynchronously
    print("stock_price:", stock_price)
    producer.produce(
        "stock_prices",
        key=stock_price["symbol"],
        value=json.dumps(stock_price),
        callback=delivery_report,
    )

    producer.poll(1)
    time.sleep(1)

