from chapter2.DoublyLinkedList import DoublyLinkedList
from chapter2.SinglyLinkedList import SinglyLinkedList

print('\033[1;32m' + '-----Chapter 2-----' + '\033[0m')

# SinglyLinkedList
print('\033[31m' + 'SinglyLinkedList: ' + '\033[0m')
singleList = SinglyLinkedList()
singleList.append(3)
singleList.append(4)
singleList.append(1)
singleList.append(2)
singleList.print()
singleList.sort()
singleList.print()

# DoublyLinkedList
print('\033[31m' + 'DoublyLinkedList: ' + '\033[0m')
doubleList = DoublyLinkedList()
doubleList.append("a")
doubleList.append("b")
doubleList.append("c")
doubleList.append("d")
doubleList.print()
doubleList.remove("c")
doubleList.print_reverse()