from confluent_kafka import Producer
import json
import time
import random

# Configuration for the Confluent Kafka producer
conf = {"bootstrap.servers": "kafka:9092"}

# Create a Producer instance
producer = Producer(**conf)


def delivery_report(err, msg):
    """Called once for each message produced to indicate delivery result.
    Triggered by poll() or flush()."""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


while True:
    stock_price = {"symbol": "AAPL", "price": round(random.uniform(150, 160), 2)}
    # Produce the message asynchronously
    print("stock_price:", stock_price)
    producer.produce(
        "stock_prices",
        key=stock_price["symbol"],
        value=json.dumps(stock_price),
        callback=delivery_report,
    )

    # Wait up to 1 second for events. Callbacks will be invoked during
    # this method call if the message is acknowledged by the broker.
    producer.poll(1)

    time.sleep(1)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
# producer.flush()
