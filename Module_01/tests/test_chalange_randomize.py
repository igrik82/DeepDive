import chalange_randomize

test_list = [1, 2, 3, 4, 5, 6]


def test_randomize():
    assert chalange_randomize.randomize(test_list) != test_list
