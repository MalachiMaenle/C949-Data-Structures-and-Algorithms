class BSTNode:
    def __init__(self, data, parent, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def count(self):
        left_count = 0
        right_count = 0
        if self.left is not None:
            left_count = self.left.count()
        if self.right is not None:
            right_count = self.right.count()
        return 1 + left_count + right_count

    def get_successor(self):
        if self.right is not None:
            successor = self.right
            while successor.left is not None:
                successor = successor.left
            return successor

        node = self
        while node.parent is not None and node == node.parent.right:
            node = node.parent
        return node.parent

    def replace_child(self, current_child, new_child):
        if current_child is self.left:
            self.left = new_child
            if self.left:
                self.left.parent = self
        elif current_child is self.right:
            self.right = new_child
            if self.right:
                self.right.parent = self