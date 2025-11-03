from hw4 import sum_general_int_list


def test_flat_list():
    lst = [1, 2, 3, 4]
    assert sum_general_int_list(lst) == 10


def test_single_nested_list():
    lst = [[1, 2], 3]
    assert sum_general_int_list(lst) == 6


def test_deeply_nested_list():
    lst = [[[1, 2], 3]]
    assert sum_general_int_list(lst) == 6


def test_empty_list():
    lst = []
    assert sum_general_int_list(lst) == 0


def test_list_with_empty_sublist():
    lst = [[], [3, 2], 1]
    assert sum_general_int_list(lst) == 6


def test_nested_empties():
    lst = [[[], []]]
    assert sum_general_int_list(lst) == 0


def test_increasing_depth_chain():
    lst = [1, [2, [3]]]
    assert sum_general_int_list(lst) == 6
