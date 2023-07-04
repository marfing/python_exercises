import pytest
from find_smallest_difference import find_small_diff_in_sorted, mergeSort


def test_crack_code():
    arr1 = [1,3,15,11,2]
    arr2 = [23,127,135,19,8]
    assert find_small_diff_in_sorted(arr1, arr2) == 3

def test_crack_code():
    arr1 = [23,127,135,19,8]
    arr2 = [1,3,15,11,2]
    assert find_small_diff_in_sorted(arr1, arr2) == 3

def test_all_zero():
    arr1 = [0,0,0,0]
    arr2 = [0,0,0,0]
    assert find_small_diff_in_sorted(arr1, arr2) == 0

def test_just_one():
    arr1 = [0,0,0,0,1]
    arr2 = [0,0,0,0,4,3,2]
    assert find_small_diff_in_sorted(arr1, arr2) == 1

def test_1():
    arr1 = []
    arr2 = [0,0,0,0,4,3,2]
    assert find_small_diff_in_sorted(arr1, arr2) == 2

def test_2():
    arr1 = [4,567,23]
    arr2 = []
    assert find_small_diff_in_sorted(arr1, arr2) == 4

def test_3():
    arr1 = [1,1,1]
    arr2 = [1]
    assert find_small_diff_in_sorted(arr1, arr2) == 0


def test_4():
    arr1 = [1,45,8]
    arr2 = [7,5,46]
    assert find_small_diff_in_sorted(arr1, arr2) == 1
