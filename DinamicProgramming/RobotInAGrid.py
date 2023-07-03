
class Grid:
    def __init__(self, offLimitCells = [], r=0, c=0):
        self.offLimitsCells = offLimitCells
        self.rows = r
        self.columns = c
        self.pathNodes = []
        self.nodes = {}
        self.firstNode = Node((0,0))
        self.addChildNodes(self.firstNode,0,0)
        self.pathFound = False

    def addChildNodes(self,node,i,j):
        if i == self.rows-1 and j == self.columns-1:
            node.setLast()
            return
        if i != self.rows-1 and (i+1,j) not in self.offLimitsCells:
            if (i+1,j) not in self.nodes:
                d_n = Node((i+1,j))
                self.nodes[(i+1,j)] = d_n
            else:
                d_n = self.nodes[(i+1,j)]
            node.addDownChild(d_n)
            self.addChildNodes(d_n,i+1,j)
        if j != self.columns-1 and (i,j+1) not in self.offLimitsCells:
            if (i,j+1) not in self.nodes:
                r_n = Node((i,j+1))
                self.nodes[(i,j+1)] = r_n
            else:
                r_n = self.nodes[(i,j+1)]
            node.addRightChild(r_n)
            self.addChildNodes(r_n,i, j+1)
        return

    def inOrderTraversal(self, node, function):
        if node != None and not node.traversed:
            node.traversed = True
            if node.isLast():
                function(node)
                return
                #self.pathNodes.append(node)
            else:
                self.inOrderTraversal(node.right, function)
                function(node)
                #self.pathNodes.append(node)
                self.inOrderTraversal(node.down, function)
                # if node.getRight() != None:
                #     self.pathNodes.remove(node.getRight())

    def preOrderTraversal(self, node, function1, function2 = None):
        if node != None and not node.traversed and not self.pathFound:
            node.traversed = True
            if node.isLast():
                function1(node)
                if function2 != None:
                    self.pathFound = True
                return
            else:
                function1(node)
                self.preOrderTraversal(node.right, function1, function2)     
                if function2 != None and node.right != None and not self.pathFound:
                    function2(node.right)           
                self.preOrderTraversal(node.down, function1, function2)
        else:
            return

    def bestPathSearch(self):
        self.preOrderTraversal(self.firstNode, self.addToBestPath, self.removeFromBestPath)
        for n in self.pathNodes:
            print(n)     
    
    def addToBestPath(self, node):
        self.pathNodes.append(node)

    def removeFromBestPath(self, node):
        self.pathNodes.remove(node)

    def printGrid(self):
        self.preOrderTraversal(self.firstNode, print)


class Node:
    def __init__(self, coordinates, last = False):
        self.down = None
        self.right = None
        self.last = last
        self.coordinates = coordinates
        self.traversed = False

    def getDown(self):
        return self.down
    
    def getRight(self):
        return self.right

    def isLast(self):
        return self.last
    
    def setLast(self):
        self.last = True
    
    def addDownChild(self, node):
        self.down = node

    def addRightChild(self, node):
        self.right = node
    
    def __str__(self) -> str:
        return f"{self.coordinates}" + ("-Last" if self.last else "")


if __name__ == "__main__":
    r = 5
    c = 7
    offLimitCells = []
    offLimitCells.append((0,1))
    offLimitCells.append((1,2))
    offLimitCells.append((2,1))
    offLimitCells.append((3,4))
    grid = Grid(offLimitCells,r,c)
    #grid.printGrid()
    grid.bestPathSearch()

