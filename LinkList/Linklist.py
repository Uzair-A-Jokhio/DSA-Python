""" CREATING A LINKLIST  """

class Node:
    """ a node for link list
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        """ insert an node at the begining of a link list 
        
        Args:
            data (_type_): _description_
        """
        new_node = Node(data)
        if self.head is None:
            self.head == new_node
            return 
        else:
            new_node.next = self.head
            self.head = new_node


    def insert_at_index(self, data, index):
        if (index ==0):
            self.insert_at_begin(data)

        position = 0
        current_node = self.head

        while (current_node != None and position + 1 != index):
            position += 1
            current_node = current_node.next
        
        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print('Index not present')
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        
        current_node.next = new_node

    def update_node(self, val, index):
        current_node = self.head 
        position = 0 
        if position == index:
            current_node.data = val 
        else:
            while(current_node != None and position + 1 != None):
                position += 1 
                current_node = current_node.next
            
            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")


    









llist = LinkList()
llist.insert_at_begin(3)
llist.insert_at_begin(2)

