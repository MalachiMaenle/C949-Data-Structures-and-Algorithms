from chapter5.BinarySearchTree import BinarySearchTree

print('\033[1;32m' + '-----Chapter 5-----' + '\033[0m')

print('\033[31m' + 'BinarySearchTree: ' + '\033[0m')
# region BinarySearchTree test
tree = BinarySearchTree()
itemList = [83,28,547,187,167,457,10,35,1,5,7,2435,6426]
for item in itemList:
    tree.insert_key(item)
tree.print_tree()
# endregion
# region BinarySearchTree notes
# Leaf - A tree node with no children
# Internal node - a node with at least one node
# root - the top node of the tree with no parent nodes
# parent a node with a child is that child's parent
# ancestors - include all parents up until the trees root
# descendants - all children recursively of the node
# edge - link between nodes
# depth - number of edges between the root node and the current node
# level - all nodes that are at the same depth
# tree height - largest depth of any node
# full - every node contains 0 or 2 children
# complete - if all levels contain all possible nodes and all nodes in the last level as as far left as possible
# perfect - all internal nodes have 2 children and all leaf nodes are at the same level
# subtree - any node in the tree and all of its descendants
# endregion