class AVLNode:
    def __init__(self, node_key):
        self.key = node_key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0

    def get_balance(self):
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        return left_height - right_height

    def get_key(self):
        return self.key

    def get_left(self):
        return self.left

    def get_parent(self):
        return self.parent

    def get_right(self):
        return self.right

    def replace_child(self, current_child, new_child):
        if self.left is current_child:
            self.set_left(new_child)
            return True
        elif self.right is current_child:
            self.set_right(new_child)
            return True

        return False

    def set_key(self, new_key):
        self.key = new_key

    def set_left(self, new_left_child):
        self.left = new_left_child

        if self.left is not None:
            self.left.parent = self

        self.update_height()

    def set_parent(self, new_parent):
        self.parent = new_parent

    def set_right(self, new_right_child):
        self.right = new_right_child

        if self.right is not None:
            self.right.parent = self

        self.update_height()

    def update_height(self):
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        self.height = max(left_height, right_height) + 1