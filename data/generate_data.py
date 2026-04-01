import csv
import random
from datetime import datetime, timedelta

services = ["auth", "payments", "orders", "search", "analytics", "media"]
clouds = ["AWS", "GCP", "Azure"]
regions = ["us-east-1", "us-west-2", "us-central1", "eastus"]
asns = ["AS16509", "AS15169", "AS8075"]

def generate_data(rows=5000):
    with open("data/simulated_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        
        writer.writerow([
            "timestamp", "service", "cloud", "region", "asn",
            "cloud_status", "network_status", "latency", "failure"
        ])

        start_time = datetime.now()

        for i in range(rows):
            timestamp = start_time + timedelta(seconds=i)

            cloud_status = random.choice(["operational", "degraded", "down"])
            network_status = random.choice(["stable", "unstable", "down"])
            latency = random.randint(50, 500)

            # Failure logic (important for ML)
            failure = 1 if (
                cloud_status == "down" or
                network_status == "down" or
                latency > 400
            ) else 0

            writer.writerow([
                timestamp,
                random.choice(services),
                random.choice(clouds),
                random.choice(regions),
                random.choice(asns),
                cloud_status,
                network_status,
                latency,
                failure
            ])

if __name__ == "__main__":
    generate_data(10000)