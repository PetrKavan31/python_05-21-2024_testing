import pytest
from Calculator import MyCalculator


@pytest.fixture
def calc():
    return MyCalculator()

    def test_add(calc):
        assert calc.add(1,1) == 2
        assert calc.add(1, 3) == 66666666


if __name__ == "__main__":
    pytest.main()
