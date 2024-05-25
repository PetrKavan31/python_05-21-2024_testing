import pytest
from calc_MJ import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(3, 2) == 5
    assert calc.add(-1, -1) == -2
    assert calc.add(0, 0) == 0

def test_subtract(calc):
    assert calc.subtract(3, 2) == 1
    assert calc.subtract(-1, -1) == 0
    assert calc.subtract(0, 0) == 0

def test_multiply(calc):
    assert calc.multiply(3, 2) == 6
    assert calc.multiply(-1, -1) == 1
    assert calc.multiply(0, 0) == 0

def test_divide(calc):
    assert calc.divide(6, 2) == 3
    assert calc.divide(-1, -1) == 1
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(1, 0)

def test_maximum(calc):
    assert calc.maximum(3, 2) == 3
    assert calc.maximum(-1, -1) == -1
    assert calc.maximum(0, 0) == 0

def test_minimum(calc):
    assert calc.minimum(3, 2) == 2
    assert calc.minimum(-1, -1) == -1
    assert calc.minimum(0, 0) == 0

def test_percentage(calc):
    assert calc.percentage(50, 20) == 10
    assert calc.percentage(100, 10) == 10
    assert calc.percentage(0, 100) == 0

def test_power(calc):
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(0, 5) == 0

