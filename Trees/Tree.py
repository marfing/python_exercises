from Node import Node

class Tree:
    def __init__(self, root: Node=None):
        self.root = root
        self.test_values_check = []

    def getRoot(self):
        return self.root
    
    #print in ascending order
    def inOrderTraversal(self, node):
        if node != None:
            self.inOrderTraversal(node.left)
            self.visit(node)
            self.inOrderTraversal(node.right)
    
    def preOrderTraversal(self, node):
        if node != None:
            self.visit(node)
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)

    def postOrderTraversal(self, node):
        if node != None:
            self.postOrderTraversal(node.left)
            self.postOrderTraversal(node.right)
            self.visit(node)
            
    def visit(self, node):
        print(f"Node value: {node.value}")
        self.test_values_check.append(node.value)

    def getTestValuesCheck(self):
        return self.test_values_check

    #insert
    #remove
    #search
    #delete
    #traversing