# tests/test_subnet_calculator.py

from subnetter.subnet_calculator import calculate_subnet


def test_calculate_subnet(subnet_test_data):
    ip_address, subnet_mask, expected_output = subnet_test_data
    result = calculate_subnet(ip_address, subnet_mask)
    assert result == expected_output
