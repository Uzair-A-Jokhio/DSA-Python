class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right

    def __str__(self):
        left_data = self.left_child.data if self.left_child else "None"
        right_data = self.right_child.data if self.right_child else "None"
        return f"Parent node: {self.data}, Left child: {left_data}, Right child: {right_data}"

class BinarySerachTree(TreeNode):
    def __init__(self):
        self.root = None

    def search(self, search_value):
        current_node = self.root
        while search_value:
            if search_value == current_node:
                return True
            elif search_value > current_node:
                current_node = self.right_child
            else:
                current_node = self.left_child
        return False
    
    def insert(self, value):
        new_node = TreeNode(value)
        # Check if the BST is empty
        if self.root == None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                # Check if the data to insert is smaller than the current node's data
                if value < current_node.data:
                    if current_node.left_child == None:
                        current_node.left_child = new_node
                        return
                    else:
                        current_node = current_node.left_child
                # Check if the data to insert is greater than the current node's data
                elif value > current_node.data:
                    if current_node.right_child == None:
                        current_node.right_child = new_node
                        return
                    else:
                        current_node = current_node.right_child
                    
    
    def find_min(self):
    # Set current_node as the root
        current_node = self.root
        # Iterate over the nodes of the appropriate subtree
        while current_node.left_child:
            # Update current_node
            current_node = current_node.left_child
            return current_node.data
        

if __name__ == "__main__":
    node1 = TreeNode("B")
    node2 = TreeNode("C")
    root_node = TreeNode("A",node1, node2)
    node3 = TreeNode("D")
    node4 = TreeNode('E')
    new_root_node = TreeNode(root_node, node3, node4)
    print(new_root_node)