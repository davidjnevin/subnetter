import pytest


@pytest.fixture(
    params=[
        (
            "192.168.1.1",
            "255.255.255.0",
            {
                "network_address": "192.168.1.0",
                "broadcast_address": "192.168.1.255",
                "host_addresses": [f"192.168.1.{i}" for i in range(1, 255)],
                "error": None,
            },
        ),
        (
            "10.0.0.2",
            "255.255.254.0",
            {
                "network_address": "10.0.0.0",
                "broadcast_address": "10.0.1.255",
                "host_addresses": [f"10.0.{i // 256}.{i % 256}" for i in range(1, 510)],
                "error": None,
            },
        ),
        (
            "172.16.0.1",
            "255.255.0.0",
            {
                "network_address": "172.16.0.0",
                "broadcast_address": "172.16.255.255",
                "host_addresses": [f"172.16.{i // 256}.{i % 256}" for i in range(1, 65534)],
                "error": None,
            },
        ),
        (
            "192.168.1.1",
            "255.255.255.256",
            {"error": "Netmask must be between 0 and 32"},
        ),
    ]
)
def subnet_test_data(request):
    return request.param
