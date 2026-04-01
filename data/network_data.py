import random

def get_network_status():
    asns = ["AS16509", "AS15169", "AS8075"]

    data = []

    for asn in asns:
        status = random.choices(
            ["stable", "unstable", "down"],
            weights=[0.7, 0.2, 0.1]
        )[0]

        data.append({
            "asn": asn,
            "status": status
        })

    return data