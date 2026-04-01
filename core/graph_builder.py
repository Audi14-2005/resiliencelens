import networkx as nx

def build_graph(services):
    G = nx.Graph()

    for service in services:
        service_node = service["name"]
        cloud_node = f'{service["cloud"]}-{service["region"]}'
        asn_node = service["asn"]

        G.add_node(service_node, type="service")
        G.add_node(cloud_node, type="cloud")
        G.add_node(asn_node, type="network")

        G.add_edge(service_node, cloud_node)
        G.add_edge(service_node, asn_node)

    return G