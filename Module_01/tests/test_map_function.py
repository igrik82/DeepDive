from map_function import power

list_1 = [1, 2, 3, 4]


def test_power():
    assert list(map(power, list_1)) == [1, 4, 9, 16]
