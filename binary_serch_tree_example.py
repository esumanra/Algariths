import binary_search_tree_util as bf

bst = bf.BinarySearchTree()
arr = ['F', 'D', 'B', 'E', 'A', 'C', 'J', 'G', 'K', 'I']
a1 = [1, 2, 3, 4, 5, 6, 7, 8]

bst.BST_from_array(arr)
bst.preorder_traversal(bst.root)
print('\n')
bst.inorder_traversal(bst.root)
print('\n')
bst.postorder_traversal(bst.root)
print('\n')
