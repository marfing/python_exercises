import pytest
from zeros_in_factorial import factorial_calc


@pytest.fixture
def get_calc():
    return factorial_calc()

    
def test_0(get_calc):
    calc = get_calc
    assert calc.find_last_zeros(0) == 0

def test_100(get_calc):
    calc = get_calc
    assert calc.find_last_zeros(100) == 24

def test_1000(get_calc):
    calc = get_calc
    assert calc.find_last_zeros(1000) == 249
