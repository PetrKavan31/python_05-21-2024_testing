import pytest
from my_modul import add, subtract
# import my_modul


def test_add():
    assert add(1,2) == 3
    assert add(-1, 1) == 0
    assert add(0,0) == 0
    assert add(-1, -1) == -2


def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0


if __name__ == "__main__":
    pytest.main()
