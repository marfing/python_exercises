import pytest
from english_int import converter

@pytest.fixture
def get_calc():
    return converter()

def test_1(get_calc):
    conv = get_calc
    assert conv.toEnglish(631234) == 'six hundred thirty one thousand two hundred thirty four '

def test_2(get_calc):
    conv = get_calc
    assert conv.toEnglish(0) == 'zero '

def test_3(get_calc):
    conv = get_calc
    assert conv.toEnglish(00000) == 'zero '

def test_4(get_calc):
    conv = get_calc
    assert conv.toEnglish(9) == 'nine '

def test_5(get_calc):
    conv = get_calc
    assert conv.toEnglish(10) == 'ten '

def test_6(get_calc):
    conv = get_calc
    assert conv.toEnglish(11) == 'eleven '

def test_7(get_calc):
    conv = get_calc
    assert conv.toEnglish(12) == 'twelve '

def test_8(get_calc):
    conv = get_calc
    assert conv.toEnglish(20) == 'twenty '

def test_9(get_calc):
    conv = get_calc
    assert conv.toEnglish(22) == 'twenty two '

def test_10(get_calc):
    conv = get_calc
    assert conv.toEnglish(100) == 'one hundred '

def test_11(get_calc):
    conv = get_calc
    assert conv.toEnglish(132) == 'one hundred thirty two '    

def test_12(get_calc):
    conv = get_calc
    assert conv.toEnglish(1000000) == 'one milion '    

def test_13(get_calc):
    conv = get_calc
    assert conv.toEnglish(1100000) == 'one milion one hundred thousand '

def test_14(get_calc):
    conv = get_calc
    assert conv.toEnglish(1110000) == 'one milion one hundred ten thousand '

def test_15(get_calc):
    conv = get_calc
    assert conv.toEnglish(1111000) == 'one milion one hundred eleven thousand '

def test_16(get_calc):
    conv = get_calc
    assert conv.toEnglish(1000001) == 'one milion one '

def test_17(get_calc):
    conv = get_calc
    assert conv.toEnglish(1631234) == 'one milion six hundred thirty one thousand two hundred thirty four '

def test_18(get_calc):
    conv = get_calc
    assert conv.toEnglish(1031034) == 'one milion thirty one thousand thirty four '
