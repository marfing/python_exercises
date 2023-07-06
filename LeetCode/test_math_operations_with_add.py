import pytest
from math_operations_with_add import my_multiply

def test_mult_1():
    assert my_multiply(-4,-5) == 20

def test_mult_2():
    assert my_multiply(0,0) == 0

def test_mult_3():
    assert my_multiply(0,5) == 0

def test_mult_4():
    assert my_multiply(5,0) == 0

def test_mult_5():
    assert my_multiply(-5,0) == 0

def test_mult_6():
    assert my_multiply(0,-2) == 0

def test_mult_7():
    assert my_multiply(-5,-3) == 15

def test_mult_8():
    assert my_multiply(-5,3) == -15

def test_mult_9():
    assert my_multiply(5,-3) == -15
    