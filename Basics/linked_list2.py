
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def create(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
    def printNode(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        for i in elements:
            print(i," -> ",end="")

my_list = LinkedList()
my_list.create(34)
my_list.create(30)
my_list.create(24)
my_list.create(14)
my_list.printNode()
