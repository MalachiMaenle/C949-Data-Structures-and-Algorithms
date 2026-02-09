from chapter6.AVLTree import AVLTree

print('\n\033[1;32m' + '-----Chapter 6-----' + '\033[0m')

print('\n\033[31m' + 'AVLTree: ' + '\033[0m')
# region AVLTree test
keys_to_insert = [10, 20, 5, 22, 15, 47, 19, 3, 12, 18]
keys_to_remove = [12, 20, 30]

show_tree_after_each_insertion = False

tree = AVLTree()

for key in keys_to_insert:
    tree.insert_key(key)
    if show_tree_after_each_insertion:
        print(f"Tree after inserting {key}:")
        tree.print_tree("\n\n")

print("Tree after initial insertions:")
tree.print_tree("\n\n")

for key in keys_to_remove:
    if tree.remove_key(key):
        print(f"Removed key {key}:")
        tree.print_tree("\n\n")
    else:
        print(f"Failed to remove key {key} (not found)")
# endregion
# region AVLTree notes
#
# endregion