from hw4 import compute_distance
import math


def test_one_degree_north():
    # One degree of latitude ≈ 111 km
    pairs = [((0, 0), (1, 0))]
    result = compute_distance(pairs)
    assert len(result) == 1
    assert math.isclose(result[0], 111, rel_tol=0.01)


def test_two_degrees_north():
    pairs = [((0, 0), (0, 2))]
    result = compute_distance(pairs)
    assert math.isclose(result[0], 222, rel_tol=0.01)
    

def test_both_coordinates_change():
    pairs = [((0, 0), (1, 1))]
    result = compute_distance(pairs)
    assert math.isclose(result[0], 157, rel_tol=0.01)


def test_zero_distance():
    pairs = [((10, 10), (10, 10))]
    result = compute_distance(pairs)
    assert result == [0.0]


def test_empty_list():
    result = compute_distance([])
    assert result == []
