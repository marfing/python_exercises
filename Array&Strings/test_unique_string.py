from unique_string import check_unique, check_unique_with_hash
import pytest


def test_brute_force_non_unico ():
    assert check_unique("abcdefb") == "non unico"

def test_brute_force_unico ():
    assert check_unique("abcdef") == "unico"    

def test_hash_non_unico ():
    assert check_unique_with_hash("abcdefb") == "hash - non unico"

def test_hash_unico ():
    assert check_unique_with_hash("abcdef") == "hash - unico"       