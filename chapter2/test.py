from chapter2.DoublyLinkedList import DoublyLinkedList
from chapter2.SinglyLinkedList import SinglyLinkedList

print('\033[1;32m' + '-----Chapter 2-----' + '\033[0m')

print('\033[31m' + 'SinglyLinkedList: ' + '\033[0m')
# region SinglyLinkedList test
singleList = SinglyLinkedList()
singleList.append(3)
singleList.append(4)
singleList.append(1)
singleList.append(2)
singleList.print()
singleList.sort()
singleList.print()
# endregion
# region SinglyLinkedList notes
# Each list node has a pointer/reference to the next node
# the list has a reference to the first (head) and last (tail) node
# endregion

print('\033[31m' + 'DoublyLinkedList: ' + '\033[0m')
# region DoublyLinkedList test
doubleList = DoublyLinkedList()
doubleList.append("a")
doubleList.append("b")
doubleList.append("c")
doubleList.append("d")
doubleList.print()
doubleList.remove("c")
doubleList.print_reverse()
# endregion test
# region DoublyLinkedList notes
# Each node has data, a reference to the next node, and a reference to the previous node
# endregion