from chapter10.Tree234 import Tree234

print('\033[1;32m' + '-----Chapter 10-----' + '\033[0m')

print('\033[31m' + 'B-Trees: ' + '\033[0m')
# region B-Trees test
keys_to_insert = [15, 42, 77, 36, 19, 47, 28, 39, 55, 73, 99]
keys_to_remove = [15, 47, 40, 19, 55, 77, 58, 28]

tree = Tree234()
for key in keys_to_insert:
    tree.insert(key)

    print(f"Inserted {key}. Tree now has height ", end="")
    print(f"{tree.get_height()}.")

print()
for key in keys_to_remove:
    if tree.remove(key):
        print(f"Removed {key}.")
        print(f"Tree now has height {tree.get_height()} and keys: ", end="")
        tree.print_keys(", ")
        print()
    else:
        print(f"Key {key} not found. Tree's keys are not changed.")
# endregion
# region B-Trees notes
# all keys are distinct
# all leaf nodes are the same level
# each nodes keys are sorted, leftmost is min, rightmost is max
# each key in an internal node has one left subtree and one right subtree
# endregion