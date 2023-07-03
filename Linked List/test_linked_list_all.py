from linked_list import Linked_list
import pytest 

class Params:
    def __init__(self):
        self.list = ['a','b','c','d','e','f','g','h','i','i','l','a']
        self.num_list = [3,5,8,5,10,2,1]
        self.l = Linked_list()
        self.num_l = Linked_list()
        self.l.createFromList(self.list)
        self.num_l.createFromList(self.num_list)
        self.l.printList()
        self.num_l.printList()

@pytest.fixture
def get_params():
    return Params()

def test_create_from_list(get_params):
    param = get_params
    assert param.list == param.l.getDataList()

def test_remove_dups(get_params):
    param = get_params
    param.l.remove_dups()
    list = ['a','b','c','d','e','f','g','h','i','l']
    assert param.l.getDataList() == list

def test_get_last_k(get_params):
    k = 4
    param = get_params
    output = param.l.get_last_k(k)
    assert output == ['i','i','l','a']

def test_list_partition(get_params):
    part = 5
    param = Params()
    param.num_l.list_partition(5)
    param.num_l.printList()
    assert param.num_l.getDataList() == [1,2,3,5,5,8,10]


def test_reverse_sum():
    input1 = [7,1,6]
    input2 = [5,9,2]
    input3 = [5,9]
    input4 = [2,4,9,2]

    l1 = Linked_list(input1)

    l12_result = l1.reverse_sum(Linked_list(input2))
    l13_result = l1.reverse_sum(Linked_list(input3))
    l14_result = l1.reverse_sum(Linked_list(input4))
    
    assert l12_result.getDataList() == [2,1,9]
    assert l13_result.getDataList() == [2,1,7]
    assert l14_result.getDataList() == [9,5,5,3]

def test_is_palindrome():
    l1 = Linked_list(['a','c','c','a'])
    l2 = Linked_list(['a','c','c','a','b'])
    l3 = Linked_list(['a','c','i','c','a'])
    l4 = Linked_list(['p','c','i','c','a'])
    
    assert l1.is_palindrome() == True
    assert l2.is_palindrome() == False
    assert l3.is_palindrome() == True
    assert l4.is_palindrome() == False