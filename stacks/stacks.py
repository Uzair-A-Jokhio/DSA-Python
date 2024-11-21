class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        # Create a node with the data
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        # Set the created node to the top node
        self.top = new_node
        # Increase the size of the stack by one
        self.size += 1

    def pop(self):
        # Check if there is a top element
        if self.top is None:
            return None
        else:
            popped_node = self.top
            # Decrement the size of the stack
            self.size -= 1
            # Update the new value for the top node
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data 
        
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None
        

if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push("hello world")
    my_stack.push(45)
    print(f"Stack size {my_stack.size}")
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    print(f"Stack size {my_stack.size}")