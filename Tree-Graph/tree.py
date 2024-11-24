class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right

    def __str__(self):
        left_data = self.left_child.data if self.left_child else "None"
        right_data = self.right_child.data if self.right_child else "None"
        return f"Parent node: {self.data}, Left child: {left_data}, Right child: {right_data}"

if __name__ == "__main__":
    node1 = TreeNode("B")
    node2 = TreeNode("C")
    root_node = TreeNode("A",node1, node2)
    node3 = TreeNode("D")
    node4 = TreeNode('E')
    new_root_node = TreeNode(root_node, node3, node4)
    print(new_root_node)