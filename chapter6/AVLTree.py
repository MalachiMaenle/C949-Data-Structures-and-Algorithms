from chapter6.AVLNode import AVLNode
from chapter6.AVLPrint import AVLPrint

class AVLTree:
    def __init__(self):
        self.root = None

    def contains(self, key):
        return self.search(key) is not None

    def get_root(self):
        return self.root

    def insert_key(self, key):
        if self.contains(key):
            return False
        self.insert_node(AVLNode(key))
        return True

    def insert_node(self, node):
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None:
                if node.get_key() < current_node.get_key():
                    if current_node.get_left() is None:
                        current_node.set_left(node)
                        current_node = None
                    else:
                        current_node = current_node.get_left()
                else:
                    if current_node.get_right() is None:
                        current_node.set_right(node)
                        current_node = None
                    else:
                        current_node = current_node.get_right()
            node = node.get_parent()
            while node is not None:
                self.rebalance(node)
                node = node.get_parent()

    def print_tree(self, end=""):
        print(f"{AVLPrint.tree_to_string(self.root)}{end}", end="")

    def rebalance(self, node):
        node.update_height()

        if node.get_balance() is -2:
            if node.get_right().get_balance() is 1:
                self.rotate_right(node.get_right())
            self.rotate_left(node)
        elif node.get_balance() is 2:
            if node.get_left().get_balance() is -1:
                self.rotate_left(node.get_left())
            self.rotate_right(node)

    def remove_key(self, key):
        node = self.search(key)
        if node is None:
            return False
        return self.remove_node(node)

    def remove_node(self, node_to_remove):
        if node_to_remove is None:
            return False

        parent = node_to_remove.get_parent()

        if node_to_remove.get_left() is not None and node_to_remove.get_right() is not None:
            successor_node = node_to_remove.get_right()
            while successor_node.get_left() is not None:
                successor_node = successor_node.get_left()

            node_to_remove.set_key(successor_node.get_key())

            self.remove_node(successor_node)

            return True

        # Case 2: Root node (with 1 or 0 children)
        elif node_to_remove is self.root:
            if node_to_remove.get_left() is not None:
                self.root = node_to_remove.get_left()
            else:
                self.root = node_to_remove.get_right()

            if self.root is not None:
                self.root.set_parent(None)

            return True

        # Case 3: Internal with left child only
        elif node_to_remove.get_left() is not None:
            parent.replace_child(node_to_remove, node_to_remove.get_left())

        # Case 4: Internal with right child only OR leaf
        else:
            parent.replace_child(node_to_remove, node_to_remove.get_right())

        # Anything that was below node_to_remove that has persisted is already
        # correctly balanced, but ancestors of node_to_remove may need
        # rebalancing
        node_to_rebalance = parent
        while node_to_rebalance is not None:
            self.rebalance(node_to_rebalance)
            node_to_rebalance = node_to_rebalance.get_parent()

        return True

    def rotate_left(self, node):
        parent = node.get_parent()
        right_child = node.get_right()
        right_left_child = right_child.get_left()

        node.set_right(right_left_child)

        right_child.set_left(node)

        if parent is not None:
            parent.replace_child(node, right_child)
        else:
            self.root = right_child
            self.root.set_parent(None)

    def rotate_right(self, node):
        parent = node.get_parent()
        left_child = node.get_left()
        left_right_child = left_child.get_right()

        node.set_left(left_right_child)

        left_child.set_right(node)

        if parent is not None:
            parent.replace_child(node, left_child)
        else:
            self.root = left_child
            self.root.set_parent(None)

    def search(self, desired_key):
        current_node = self.root
        while current_node is not None:
            if current_node.get_key() is desired_key:
                return current_node

            elif desired_key < current_node.get_key():
                current_node = current_node.get_left()

            else:
                current_node = current_node.get_right()

        return None
