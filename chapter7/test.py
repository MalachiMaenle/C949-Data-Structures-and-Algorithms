from chapter7.MaxHeap import MaxHeap
from queue import PriorityQueue

print('\033[1;32m' + '-----Chapter 7-----' + '\033[0m')

print('\033[31m' + 'MaxHeap: ' + '\033[0m')
# region MaxHeap test
max_heap = MaxHeap()
numbers = [ 10, 2, 5, 18, 22 ]

for number in numbers:
    max_heap.insert(number)
    print(f"   --> heap data: {max_heap.get_heap_data_string()}")

while max_heap.get_length() > 0:
    removed_value = max_heap.remove()
    print(f"   --> removed {removed_value}, heap data: ", end="")
    print(max_heap.get_heap_data_string())
# endregion
# region MaxHeap notes
#
# endregion

print('\033[31m' + 'Treap: ' + '\033[0m')
# region Treap test
# endregion
# region Treap notes
# A treap search is the same as a BST search using the main key, since the treap is a BST
# A treap insert initially inserts a node as in a BST using the main key, then assigns a random priority to the node, and percolates the node up until the heap property is not violated.
# A treap delete can be done by setting the node's priority such that the node should be a leaf, percolating the node down using rotations until the node is a leaf, and then removing the node.
# endregion

print('\033[31m' + 'Priority Queue: ' + '\033[0m')
# region PriorityQueue test
items_to_insert = [54, 71, 22, 33, 18, 64, 91]

priority_queue = PriorityQueue()
for item in items_to_insert:
    priority_queue.put(item)
    print(f"Enqueued {item} into priority_queue")

print(f"priority_queue's size = {priority_queue.qsize()}")

while priority_queue.qsize() > 0:
    dequeued_item = priority_queue.get()
    print(f"Dequeued {dequeued_item} from priority_queue")
# endregion
# region PriorityQueue notes
# The PriorityQueue class gives highest priority to the smallest item.
# endregion