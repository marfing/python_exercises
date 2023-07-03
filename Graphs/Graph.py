from Node import Node
from queue import Queue

class Graph:
    def __init__(self):
        self.nodes = []
        self.visited = []
        self.final = []

        self.path = []
        self.queue = Queue()


    def addNode(self, nodes : Node):
        for node in nodes:
            if node not in self.nodes:
                self.nodes.append(node)

    
    def DepthFirstSearch(self, node_to_find : Node, from_node : Node=None, parent_node : Node=None,):
        self.visited.append(from_node)
        if from_node == None or from_node.stop or ( len(from_node.adj) == 0 and from_node.value != node_to_find.value):
            if parent_node != None and self.HasNodeValidChildren(parent_node):
                if not parent_node.stop :          
                    self.visited.remove(parent_node) 
                    parent_node.stop = True      
            if from_node != None: 
                from_node.stop = True
                self.visited.remove(from_node)
            return

        if from_node.value == node_to_find.value:
            self.final.append(self.visited)
            if parent_node != None: 
                parent_node.stop = True 
                print(f"Parent stop value: {parent_node.stop}")
            self.visited = [n for n in self.visited[:-1] if not n.stop]
        else:    
            if len(from_node.adj) != 0: 
                for adj in from_node.adj:
                    if not adj.stop and not from_node.stop: self.DepthFirstSearch(node_to_find,adj,from_node)
            else:
                if not from_node.stop:
                    self.visited.remove(from_node)    
                    from_node.stop = True

    def HasNodeValidChildren(self, node : Node):
        for child in node.adj:
            if child != None and not child.stop:
                return True
        return False
    
    def BreadthFirst_search(self, node : Node, root: Node=None):
        #prima chiamata con queue vuota
        if root != None and root in self.nodes and self.queue.empty():
            self.queue.put(root)

        _node = self.queue.get()

        if _node.value != node.value:
            if _node.visited == False:
                _node.visited = True
                self.visited.append(_node)
                if not adj:
                    _node.good_path = False
                else:
                    for adj in _node.adj:
                        if adj.visited == False:
                            self.queue.put(adj)
                    self.depthFirst_search(node)
        else:
            print(f"Found a path from {self.visited[0].value} to {node.value}")
            return
    
    # def findBestRoute(self, node : Node, root: Node=None):
    #     self.depthFirst_search(node, root)
    #     if self.visited:
    #         for n in self.visited[::-1]:
    #             if not n.good_path:
    #                 self.visited.remove(n)
    #             else:
    #                 #rimuoverlo se tutti i figli hanno bad path 

    #         last = self.visited[-1]
    #         if node not in last.adj:
    #             self.visited.pop(-1)

n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n0.addAdj(n5)
n0.addAdj(n1)
n0.addAdj(n7)
n1.addAdj(n3)
n1.addAdj(n4)
n2.addAdj(n1)
n3.addAdj(n2)
n3.addAdj(n4)
n5.addAdj(n6)
n7.addAdj(n1)
n7.addAdj(n2)

g = Graph()
g.addNode([n0,n1,n2,n3,n4,n5])
#g.findBestRoute(n2,n0)

g.DepthFirstSearch(n2, n0)
for g in g.final:
    print(f"Visited nodes: {[n.value for n in g]}")


