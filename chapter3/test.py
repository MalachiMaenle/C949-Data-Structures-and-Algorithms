from chapter3.Stack import Stack
from chapter3.StackList import StackList

print('\033[1;32m' + '-----Chapter 3-----' + '\033[0m')

# Stack
print('\033[31m' + 'Stack push/pop: ' + '\033[0m')
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(str(stack.pop()) + ", " + str(stack.pop()) + ", " + str(stack.pop()))

# StackList
print('\033[31m' + 'StackList push/pop: ' + '\033[0m')
stackList = StackList()
stackList.push(45)
stackList.push(72)
stackList.push(90)
print(str(stackList.pop()) + ", " + str(stackList.pop()) + ", " + str(stackList.pop()))