#test_hashtable.py
import pytest
from hashtable import HashTable, BLANK

#using pytest we can declare a variable to be used along the test file
@pytest.fixture
def hash_table():
    sample_data = HashTable(capacity=100)
    sample_data["hola"] = "hello"
    sample_data[98.6] = 37
    sample_data[False] = True
    sample_data['None'] = None
    return sample_data

def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None

def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100

def test_create_empty_value_slots():
    assert HashTable(capacity=3).values == [BLANK, BLANK, BLANK]

def test_should_insert_key_value_pairs(hash_table):
    assert "hello" in hash_table.values
    assert 37 in hash_table.values
    assert True in hash_table.values
    assert None in hash_table.values
    assert len(hash_table) == 100


def test_can_get_values_by_key(hash_table):
    assert hash_table["hola"] == "hello"
    assert hash_table[98.6] == 37
    assert hash_table[False] == True
    assert hash_table["None"] == None

def test_should_raise_error_on_missing_key(hash_table):
    with pytest.raises(KeyError) as exception_info:
        print(dir(hash_table['missing_key']))
    assert exception_info.value.args[0] == 'missing_key'


@pytest.mark.skip
def test_should_not_shrink_when_removing_elements():
    pass