from string_compression import string_compression
import pytest

def test_string_compression():
    test = "aabcccccaaa"
    assert string_compression(test) == "a2b1c5a3"