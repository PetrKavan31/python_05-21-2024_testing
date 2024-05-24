import pytest
from Calculator import MyCalculator

@pytest.fixture
def calc():
    return MyCalculator()

def test_add(calc):
    assert calc.add(3,2) == 5


# if __name__ == "__main__":
    # pytest.main()
