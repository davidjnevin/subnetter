import ipaddress


def calculate_subnet(ip_address, subnet_mask):
    try:
        network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
        network_address = network.network_address
        broadcast_address = network.broadcast_address
        host_addresses = list(network.hosts())

        return {
            "network_address": str(network_address),
            "broadcast_address": str(broadcast_address),
            "host_addresses": [str(host) for host in host_addresses],
            "error": None,
        }
    except ValueError as e:
        return {"error": str(e)}
