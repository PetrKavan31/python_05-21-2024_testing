import pytest
from hw_integers import IntegerSet


def test_integer_set_1():
    intset = IntegerSet([10, 20, 30, 40, 50])

    assert intset.sum() == 150
    assert intset.mean() == 30
    assert intset.max() == 50
    assert intset.min() == 10


def test_integer_set_2():
    intset = IntegerSet([-10, -20, -30, -40, -50])

    assert intset.sum() == -150
    assert intset.mean() == -30
    assert intset.max() == -10
    assert intset.min() == -50


if __name__ == "__main__":
    pytest.main()

# @pytest.fixture
# def integer_set():
#     return IntegerSet([0, 1, 2, 3, 4, 5])
#
#
# def test_sum(integer_set):
#     assert integer_set.sum() == 15
#
#
# def test_mean(integer_set):
#     assert integer_set.mean() == 2.5
#
#
# def test_max(integer_set):
#     assert integer_set.max() == 5
#
#
# def test_min(integer_set):
#     assert integer_set.min() == 0
#
#
# if __name__ == "__main__":
#     pytest.main()
