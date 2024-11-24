class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
    
    def dequeue(self):
        if self.head:
            current_node = self.head
            self.head = current_node.next
            current_node.tail = None

            if self.head == None:
                self.tail = None