import time
import random
import queue

event_queue = queue.Queue()

services = ["auth", "payments", "orders", "search"]
clouds = ["AWS", "GCP", "Azure"]
asns = ["AS16509", "AS15169", "AS8075"]

def generate_event():
    return {
        "service": random.choice(services),
        "cloud": random.choice(clouds),
        "cloud_status": random.choice(["operational", "degraded", "down"]),
        "asn": random.choice(asns),
        "network_status": random.choice(["stable", "unstable", "down"]),
        "latency": random.randint(50, 500)
    }

def stream_data():
    while True:
        event = generate_event()
        event_queue.put(event)
        time.sleep(1)