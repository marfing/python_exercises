from one_away import one_away
import pytest

def test_one_away ():
    assert one_away("pale","ple") == True
    #assert one_away("pales","pale") == True
    #assert one_away("pale","bale") == True
    #assert one_away("pale","bake") == False