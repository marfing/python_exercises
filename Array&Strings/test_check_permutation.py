from check_permutation import check_is_permutation
import pytest

def test_check_is_permutation_true():
    string1 = "pippo"
    string2 = "ipopp"

    assert check_is_permutation(string1, string2) == True


def test_check_is_permutation_false1():
    string1 = "pippo"
    string2 = "ipoppa"

    assert check_is_permutation(string1, string2) == False

def test_check_is_permutation_false2():
    string1 = "pippo"
    string2 = "epopp"

    assert check_is_permutation(string1, string2) == False