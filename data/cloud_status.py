import random

def get_cloud_status():
    providers = [
        ("AWS", "us-east-1"),
        ("AWS", "us-west-2"),
        ("GCP", "us-central1"),
        ("Azure", "eastus")
    ]

    statuses = []

    for provider, region in providers:
        status = random.choices(
            ["operational", "degraded", "down"],
            weights=[0.7, 0.2, 0.1]
        )[0]

        statuses.append({
            "provider": provider,
            "region": region,
            "status": status
        })

    return statuses