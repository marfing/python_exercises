import pytest
from zeros_in_factorial import factorial_calc


@pytest.fixture
def get_calc():
    return factorial_calc()

    
def test_0(get_calc):
    calc = get_calc
    calc.factorial(0)
    assert calc.find_zeros() == 1
    assert calc.find_zeros_by_math() == 1

def test_1(get_calc):    
    calc = get_calc
    calc.factorial(1)
    assert calc.find_zeros() == 0
    assert calc.find_zeros_by_math() == 0

def test_7(get_calc):    
    calc = get_calc
    calc.factorial(7)
    assert calc.find_zeros() == 2
    assert calc.find_zeros_by_math() == 2

def test_20(get_calc):    
    calc = get_calc
    calc.factorial(20)
    assert calc.find_zeros() == 7
    assert calc.find_zeros_by_math() == 7

