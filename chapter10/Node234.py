class Node234:
    def __init__(self, key0, child0=None, child1=None):
        self.keys = [key0, 0, 0]
        self.key_count = 1
        self.children = [child0, child1, None, None]

    @staticmethod
    def create_full_node(key0, key1, key2, child0, child1, child2, child3):
        node = Node234(key0, child0, child1)
        node.keys = [key0, key1, key2]
        node.children = [child0, child1, child2, child3]
        node.key_count = 3
        return node

    def get_child(self, child_index):
        if 0 <= child_index <= self.key_count:
            return self.children[child_index]
        return None

    def get_child_index(self, child):
        for i in range(4):
            if self.children[i] is child:
                return i
        return -1

    def get_key(self, key_index):
        return self.keys[key_index]

    def get_key_count(self):
        return self.key_count

    def get_key_index(self, key):
        for i in range(self.key_count):
            if self.keys[i] == key:
                return i
        return -1

    def has_key(self, key):
        for i in range(self.key_count):
            if self.keys[i] == key:
                return True
        return False

    def insert_key_with_children(self, key, left_child, right_child):
        if key < self.keys[0]:
            self.keys[2] = self.keys[1]
            self.keys[1] = self.keys[0]
            self.keys[0] = key
            self.children[3] = self.children[2]
            self.children[2] = self.children[1]
            self.children[1] = right_child
            self.children[0] = left_child
        elif self.key_count == 1 or key < self.keys[1]:
            self.keys[2] = self.keys[1]
            self.keys[1] = key
            self.children[3] = self.children[2]
            self.children[2] = right_child
            self.children[1] = left_child
        else:
            self.keys[2] = key
            self.children[3] = right_child
            self.children[2] = left_child
        self.key_count += 1

    def is_leaf(self):
        return self.children[0] is None

    def next_node(self, key):
        i = 0
        while i < self.key_count:
            if key < self.keys[i]:
                return self.children[i]
            i += 1
        return self.children[i]

    def remove_key(self, key_index):
        if key_index == 0:
            self.keys[0] = self.keys[1]
            self.keys[1] = self.keys[2]
            self.children[0] = self.children[1]
            self.children[1] = self.children[2]
            self.children[2] = self.children[3]
            self.children[3] = None
            self.key_count -= 1
        elif key_index == 1:
            self.keys[1] = self.keys[2]
            self.children[2] = self.children[3]
            self.children[3] = None
            self.key_count -= 1
        elif key_index == 2:
            self.children[3] = None
            self.key_count -= 1

    def set_child(self, child_index, child):
        self.children[child_index] = child

    def set_key(self, key_index, key_value):
        self.keys[key_index] = key_value

    def set_key_count(self, new_key_count):
        self.key_count = new_key_count