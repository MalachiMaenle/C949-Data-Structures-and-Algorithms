class BSTIterator:
    def __init__(self, node):
        self.node = node

    def __next__(self):
        return self.next()

    def next(self):
        if self.node is None:
            raise StopIteration
        else:
            current = self.node.data
            self.node = self.node.get_successor()
            return current