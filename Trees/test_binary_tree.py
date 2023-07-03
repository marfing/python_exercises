import pytest
from Node import Node
from Tree import Tree

    #          1
    #         / \
    #        2   3
    #       / \  / \
    #     4  None None None
    #    / \
    # None None

class LocalTree(Tree):
    def __init__(self, root=None):
        super().__init__(root)
        node = self.root
        node.left=Node(2)
        node.right = Node(3)
        node.left.left = Node(4)


    def getRoot(self):
        return self.root

@pytest.fixture
def getTestTree():
    return LocalTree(Node(1))

def test_inOrderTraversal(getTestTree: Tree):
    tree = getTestTree
    tree.inOrderTraversal(tree.getRoot())
    assert [4,2,1,3] == tree.getTestValuesCheck()

def test_preOrderTraversal(getTestTree: Tree):
    tree = getTestTree
    tree.preOrderTraversal(tree.getRoot())
    assert [1,2,4,3] == tree.getTestValuesCheck()

def test_postOrderTraversal(getTestTree: Tree):
    tree = getTestTree
    tree.postOrderTraversal(tree.getRoot())
    assert [4,2,3,1] == tree.getTestValuesCheck()
