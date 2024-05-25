import pytest
from hw_integers import IntegerSet


@pytest.fixture
def integer_set():
    return IntegerSet([0, 1, 2, 3, 4, 5])


def test_sum(integer_set):
    assert integer_set.sum() == 15


def test_mean(integer_set):
    assert integer_set.mean() == 2.5


def test_max(integer_set):
    assert integer_set.max() == 5


def test_min(integer_set):
    assert integer_set.min() == 0


if __name__ == "__main__":
     pytest.main()
