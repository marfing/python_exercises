class Node:
    def __init__(self,value=None):
        self.value = value
        self.adj = []
        self.visited = False
        self.stop = False
    
    def addAdj(self, node):
        if node not in self.adj:
            self.adj.append(node) 