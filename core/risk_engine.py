def calculate_risk(services, cloud_status, network_status):
    score = 0
    issues = []

    # Check cloud issues
    for service in services:
        for cloud in cloud_status:
            if (service["cloud"] == cloud["provider"] and
                service["region"] == cloud["region"] and
                cloud["status"] != "operational"):

                score += 50
                issues.append(f'{service["name"]} affected by {cloud["provider"]} outage')

    # Check network issues
    for service in services:
        for net in network_status:
            if service["asn"] == net["asn"] and net["status"] != "stable":
                score += 30
                issues.append(f'{service["name"]} affected by ASN instability')

    return score, issues