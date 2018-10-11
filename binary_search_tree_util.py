class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, new_data, node):
        if new_data < node.data:
            if node.left is not None:
                self.insert_node(new_data, node.left)
            else:
                node.left = Node(new_data)
        else:
            if node.right:
                self.insert_node(new_data, node.right)
            else:
                node.right = Node(new_data)

    def BST_from_array(self, arr):
        for item in arr:
            self.insert(item)

    def preorder_traversal(self, node):  # (NLR)
        if node:
            print(node.data, end='->')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):  # (LNR)
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end='->')
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):  # (LRN)
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end='->')
