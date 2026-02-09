from chapter3.Stack import Stack
from chapter3.StackList import StackList

print('\n\033[1;32m' + '-----Chapter 3-----' + '\033[0m')

print('\n\033[31m' + 'Stack: ' + '\033[0m')
# region Stack test
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(str(stack.pop()) + ", " + str(stack.pop()) + ", " + str(stack.pop()))
# endregion
# region Stack notes
# push to put stuff on the top of the stack, pop to take stuff off the top of the stack
# Linked-List stack - uses a linked list to create the stack
# endregion

print('\n\033[31m' + 'StackList: ' + '\033[0m')
# region StackList test
stackList = StackList()
stackList.push(45)
stackList.push(72)
stackList.push(90)
print(str(stackList.pop()) + ", " + str(stackList.pop()) + ", " + str(stackList.pop()))
# endregion
# region StackList notes
# uses an array to create the stack (bounded vs. unbounded)
# endregion