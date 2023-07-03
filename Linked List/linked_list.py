class Node:

    def __init__(self, data, prev=None):
        self.next = None
        self.prev = prev
        self.data = data
        if prev != None:
            prev.next = self
        print(f"Creato nodo: {data}")
    
    def setNext(self,data):
        self.next = Node(data, self)
        
# head -> nodes -> tail

class Linked_list:

    def __init__(self, list = []):
        self.tail = None
        self.head = None
        self.size = 0
        self.createFromList(list)
    
    def createFromList(self,list):
        for data in list:
            self.add(data)
    
    def getHead(self):
        return self.head
    
    def getTail(self):
        return self.tail

    #add tail node
    def add(self, data):
        new_node = Node(data, self.tail)
        self.tail = new_node
        print(f"New head: {self.tail.data}")

        if self.head == None:
            self.head = new_node
            print(f"New Head: {self.head.data}")
        self.size += 1

    #add head node
    def push(self, data):
        head = Node(data)
        head.next = self.head
        if self.head != None:
            self.head.prev = head
        self.head = head
        if self.tail == None:
            self.tail = head
        self.size += 1
        
    #remove head
    def pop(self):
        self.head = self.head.next
        self.head.prev = None

    def deleteNodeByData(self, data):
        node = self.head
        while node != None:
            if node.data == data:
                if node != self.tail:
                    node.next.prev = node.prev
                if node != self.head:
                    node.prev.next = node.next
                break
            node = node.next
        if node == self.head:
            self.head = node.next    
        if node == self.tail:
            self.tail = node.prev
        self.size -= 1

    def deleteNode(self, node: Node):
        if node != self.tail:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        if node != self.head:
            node.prev.next = node.next
        else:
            self.head = node.next
        self.size -= 1

    def printList(self):
        print(f"{self.getDataList()}")

    def getDataList(self):
        list = []
        if self.head != None:
            list.append(self.head.data)
            node = self.head
            while node.next != None:
                list.append(node.next.data)
                node = node.next
            return list
        else:
            return "Empty Linked List"

    def remove_dups(self):
        node = self.head
        while node != None:
            temp_node = node.next
            while temp_node != None:
                if temp_node.data == node.data:
                    self.deleteNode(temp_node)
                temp_node = temp_node.next
            #list = self.getDataList()
            node = node.next
        
    def get_last_k(self, k):
        node = self.tail
        list = self.getDataList()
        output = []
        for i in range(k):            
            if node.prev != None:
                output.append(node.data)
                node = node.prev
            else:
                break
        return output[::-1]
    
    # Write code to partition a linked list around a value x, such that all nodes less than x come
    # before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
    # to be after the elements less than x (see below). The partition element x can appear anywhere in the
    # "right partition"; it does not need to appear between the left and right partitions.
    # EXAMPLE
    # Input:
    #     3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
    # Output:
    #     3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
    
    def list_partition(self,partition):
        node = self.head
        #identifico eventuale nodo partizione
        #identifico dimensione lista
        _size = 0
        found = False
        while node != None:
            if node.data == partition and not found:
                found = True
            node = node.next
            _size += 1
        
        node = self.head
        for i in range(_size):
            next_node = node.next
            if node.data > partition and node != self.tail:
                self.deleteNode(node)
                self.add(node.data)
            elif node.data < partition and node != self.head:
                self.deleteNode(node)
                self.push(node.data)
            # elif node.data == partition:
            #     continue
            node = next_node
            #list = self.getDataList()

    # You have two numbers represented by a linked list, where each node contains a single
    # digit.The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
    # function that adds the two numbers and returns the sum as a linked list.
    # EXAMPLE
    # Input:(7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
    # Output: 2 -> 1 -> 9. That is, 912.

    def reverse_sum(self, other_list):
        node = self.head
        other_node = other_list.getHead()
        l_result = Linked_list()
        riporto = 0
        while node != None or other_node != None:            
            if other_node == None:
                b = 0
            else:
                b = other_node.data
                other_node = other_node.next

            if node == None:
                a = 0
            else:
                a = node.data
                node = node.next
            
            value = a + b + riporto
            if value > 9:
                l_result.add(value-10)
                #result.append(value-10)
                riporto = 1
            else:
                l_result.add(value)
                #result.append(value)
                riporto = 0
        return l_result
    
    def is_palindrome(self):
        node1 = self.head
        node2 = self.tail
        list = self.getDataList()
        for i in range(int(self.size)):
            if node1.data != node2.data:
                return False
            node1 = node1.next
            node2 = node2.prev
        return True
         
    def get_first_intersection():
        pass             

# l = Linked_list()
# l.printList()

# l.addHeadNode('h_primo')
# l.printList()

# l.addHeadNode('h_secondo')
# l.printList()

# l.addHeadNode('h_terzo')
# l.printList()

# l.addTailNode('t_primo')
# l.printList()

# l.deleteNodeByData('h_secondo')
# l.printList()

# print(f"Removing h_terzo")
# l.deleteNodeByData('h_terzo')
# l.printList()

# print(f"Removing t_primo")
# l.deleteNodeByData('t_primo')
# l.printList()