import pytest
from Calculator import MyCalculator

@pytest.fixture
def calc():
    return MyCalculator()

def test_add(calc):
    assert calc.add(3,2) == 5
    assert calc.add(-1,-2) == -3
    assert calc.add(5,5) == 10

 # if __name__ == "__main__":
     # pytest.main()
