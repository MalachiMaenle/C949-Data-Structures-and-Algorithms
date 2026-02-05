from chapter10.Node234 import Node234

class Tree234:
    def __init__(self):
        self.root = None

    def contains_key(self, key):
        return self.search_recursive(key, self.root) is not None

    def fuse(self, parent, left_node, right_node):
        if parent is self.root and parent.get_key_count() == 1:
            return self.fuse_root()

        left_node_index = parent.get_child_index(left_node)
        middle_key = parent.get_key(left_node_index)
        fused_node = Node234.create_full_node(left_node.get_key(0),middle_key,right_node.get_key(0),left_node.get_child(0),left_node.get_child(1),right_node.get_child(0),right_node.get_child(1))
        key_index = parent.get_key_index(middle_key)
        parent.remove_key(key_index)
        parent.set_child(key_index, fused_node)
        return fused_node

    def fuse_root(self):
        old_child0 = self.root.get_child(0)
        old_child1 = self.root.get_child(1)
        self.root.set_key(1, self.root.get_key(0))
        self.root.set_key(0, old_child0.get_key(0))
        self.root.set_key(2, old_child1.get_key(0))
        self.root.set_key_count(3)
        self.root.set_child(0, old_child0.get_child(0))
        self.root.set_child(1, old_child0.get_child(1))
        self.root.set_child(2, old_child1.get_child(0))
        self.root.set_child(3, old_child1.get_child(1))
        return self.root

    def get_height(self):
        return Tree234.get_height_recursive(self.root)

    @staticmethod
    def get_height_recursive(node):
        if node.get_child(0) is None:
            return 0
        return 1 + Tree234.get_height_recursive(node.get_child(0))

    @staticmethod
    def get_min_key(node):
        current = node
        while current.get_child(0) is not None:
            current = current.get_child(0)
        return current.get_key(0)

    def get_length(self):
        count = 0
        nodes = [self.root]

        while len(nodes) > 0:
            node = nodes.pop()
            if node is not None:
                count = count + node.get_key_count()

                for i in range(node.get_key_count()):
                    nodes.append(node.get_child(i))
        return count

    def insert(self, key):
        return self.insert_recursive(key, self.root, None)

    def insert_recursive(self, key, node, node_parent):
        if self.root is None:
            self.root = Node234(key)
            return True

        if node.has_key(key):
            return False

        if node.get_key_count() == 3:
            node = self.split(node, node_parent)

        if not node.is_leaf():
            return self.insert_recursive(key, node.next_node(key), node)

        node.insert_key_with_children(key, None, None)
        return True
    def key_swap(self, node, existing_key, replacement_key):
        if node is None:
            return False

        key_index = node.get_key_index(existing_key)
        if key_index == -1:
            next_node = node.next_node(existing_key)
            return self.key_swap(next_node, existing_key, replacement_key)

        node.set_key(key_index, replacement_key)
        return True

    def merge(self, node, node_parent):
        node_index = node_parent.get_child_index(node)
        left_sibling = node_parent.get_child(node_index - 1)
        right_sibling = node_parent.get_child(node_index + 1)

        if left_sibling is not None and left_sibling.get_key_count() >= 2:
            self.rotate_right(left_sibling, node_parent)
        elif right_sibling is not None and right_sibling.get_key_count() >= 2:
            self.rotate_left(right_sibling, node_parent)
        else:
            if left_sibling is None:
                node = self.fuse(node_parent, node, right_sibling)
            else:
                node = self.fuse(node_parent, left_sibling, node)

        return node

    def print_keys(self, separator=","):
        self.print_recursive(self.root, separator, False)

    @staticmethod
    def print_recursive(node, separator, printed_first):
        if node is None:
            return printed_first

        for i in range(node.get_key_count()):
            printed_first = Tree234.print_recursive(node.get_child(i), separator, printed_first)

            if printed_first:
                print(separator, end="")
            else:
                printed_first = True

            print(node.get_key(i), end="")

        Tree234.print_recursive(node.get_child(node.get_key_count()),separator, printed_first)

        return printed_first

    def remove(self, key):
        if self.root.is_leaf() and self.root.get_key_count() == 1:
            if self.root.get_key(0) is key:
                self.root = None
                return True
            return False

        current_parent = None
        current = self.root
        while current is not None:
            if current.get_key_count() == 1 and current is not self.root:
                current = self.merge(current, current_parent)

            key_index = current.get_key_index(key)
            if key_index != -1:
                if current.is_leaf():
                    current.remove_key(key_index)
                    return True
                tmp_child = current.get_child(key_index + 1)
                tmp_key = Tree234.get_min_key(tmp_child)
                self.remove(tmp_key)
                self.key_swap(self.root, key, tmp_key)
                return True
            current_parent = current
            current = current.next_node(key)
        return False

    def rotate_left(self, node, node_parent):
        node_index = node_parent.get_child_index(node)
        left_sibling = node_parent.get_child(node_index - 1)
        left_sibling.insert_key_with_children(node_parent.get_key(node_index - 1),left_sibling.get_child(left_sibling.get_key_count()),node.get_child(0))
        node_parent.set_key(node_index - 1, node.get_key(0))
        node.remove_key(0)

    def rotate_right(self, node, node_parent):
        node_index = node_parent.get_child_index(node)
        right_sibling = node_parent.get_child(node_index + 1)
        node_rightmost_child = node.get_child(node.get_key_count())
        key_for_right_sibling = node_parent.get_key(node_index)
        right_sibling.insert_key_with_children(key_for_right_sibling,node_rightmost_child, right_sibling.get_child(0))
        node_parent.set_key(node_index, node.get_key(node.get_key_count() - 1))
        node.remove_key(node.get_key_count() - 1)

    def search(self, key):
        return self.search_recursive(key, self.root)

    def search_recursive(self, key, node):
        if node is None:
            return None

        if node.has_key(key):
            return node

        return self.search_recursive(key, node.next_node(key))

    def split(self, node, node_parent):
        split_left = Node234(node.get_key(0), node.get_child(0), node.get_child(1))
        split_right = Node234(node.get_key(2), node.get_child(2), node.get_child(3))

        if node_parent is not None:
            node_parent.insert_key_with_children(node.get_key(1), split_left, split_right)
        else:
            node_parent = Node234(node.get_key(1), split_left, split_right)
            self.root = node_parent

        return node_parent