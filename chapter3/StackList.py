class StackList():
    def __init__(self):
        self.stack_list = []

    def pop(self):
        return self.stack_list.pop()

    def push(self, item):
        self.stack_list.append(item)