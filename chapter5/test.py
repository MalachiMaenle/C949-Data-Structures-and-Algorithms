from chapter5.BinarySearchTree import BinarySearchTree

print('\033[1;32m' + '-----Chapter 5-----' + '\033[0m')

# Stack
print('\033[31m' + 'BinarySearchTree: ' + '\033[0m')
tree = BinarySearchTree()
itemList = [83,28,547,187,167,457,10,35,1,5,7,2435,6426]
for item in itemList:
    tree.insert_key(item)
tree.printTree()
