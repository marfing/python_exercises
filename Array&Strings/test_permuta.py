
from permuta import permuta
import pytest

def test_should_have_permutations_number():
    word = 'test'
    result = permuta(word)
    word_len = len(word)
    permutations_number = 1
    for i in range(word_len):
        permutations_number = permutations_number * (i+1)
    assert len(result) == permutations_number

def test_should_have_specific_permutation():
    word = 'test'
    result = permuta(word)
    assert 'sett' in result
