from chapter8.BSTIterator import BSTIterator
from chapter8.BSTNode import BSTNode

class Set:
    def __init__(self, get_key_function=None):
        self.storage_root = None
        if get_key_function is None:
            self.get_key = lambda el: el
        else:
            self.get_key = get_key_function

    def __iter__(self):
        if self.storage_root is None:
            return BSTIterator(None)
        min_node = self.storage_root
        while min_node.left is not None:
            min_node = min_node.left
        return BSTIterator(min_node)

    def add(self, new_element):
        new_element_key = self.get_key(new_element)
        if self.node_search(new_element_key) is not None:
            return False

        new_node = BSTNode(new_element, None)
        if self.storage_root is None:
            self.storage_root = new_node
        else:
            node = self.storage_root
            while node is not None:
                if new_element_key < self.get_key(node.data):
                    if node.left:
                        node = node.left
                    else:
                        node.left = new_node
                        new_node.parent = node
                        return True
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = new_node
                        new_node.parent = node
                        return True
        return None

    def difference(self, other_set):
        result = Set(self.get_key)
        for element in self:
            if other_set.search(self.get_key(element)) is None:
                result.add(element)
        return result

    def filter(self, predicate):
        result = Set(self.get_key)
        for element in self:
            if predicate(element):
                result.add(element)
        return result

    def intersection(self, other_set):
        result = Set(self.get_key)
        for element in self:
            if other_set.search(self.get_key(element)) is not None:
                result.add(element)
        return result

    def __len__(self):
        if self.storage_root is None:
            return 0
        return self.storage_root.count()

    def map(self, map_function):
        result = Set(self.get_key)
        for element in self:
            new_element = map_function(element)
            result.add(new_element)
        return result

    def node_search(self, key):
        node = self.storage_root
        while node is not None:
            node_key = self.get_key(node.data)

            if node_key is key:
                return node
            elif key > node_key:
                node = node.right
            else:
                node = node.left
        return node

    def remove(self, key):
        self.remove_node(self.node_search(key))

    def remove_node(self, node_to_remove):
        if node_to_remove is not None:
            if node_to_remove.left is not None and node_to_remove.right is not None:
                successor = node_to_remove.get_successor()
                data_copy = successor.data
                self.remove_node(successor)
                node_to_remove.data = data_copy

            elif node_to_remove is self.storage_root:
                if node_to_remove.left is not None:
                    self.storage_root = node_to_remove.left
                else:
                    self.storage_root = node_to_remove.right

                if self.storage_root:
                    self.storage_root.parent = None

            elif node_to_remove.left is not None:
                node_to_remove.parent.replace_child(node_to_remove, node_to_remove.left)

            else:
                node_to_remove.parent.replace_child(node_to_remove, node_to_remove.right)

    def search(self, key):
        node = self.node_search(key)
        if node is not None:
            return node.data
        return None

    def union(self, other_set):
        result = Set(self.get_key)
        for element in self:
            result.add(element)
        for element in other_set:
            result.add(element)
        return result