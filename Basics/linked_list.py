class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self): 
        self.head = None
    
    def createNode(self, data):
        newNode = Node(data)
        if self.head is None: 
            self.head = newNode
            return
        current = self.head
        while current.next:   
            current = current.next
        current.next = newNode   

    def display(self):
        """Prints the data of each node in the list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))


my_list = LinkedList()
my_list.createNode(10)
my_list.createNode(20)
my_list.createNode(30)
my_list.display()
