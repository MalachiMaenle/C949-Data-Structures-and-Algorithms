class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_node(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while current_node is not None:
                if new_node.key < current_node.key:
                    if current_node.left is None:
                        current_node.left = new_node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        current_node = None
                    else:
                        current_node = current_node.right

    def search(self, search_key):
        current_node = self.root
        while current_node is not None:
            if current_node.key == search_key:
                return current_node
            elif search_key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def contains(self, key):
        return self.search(key) is not None

    def insert_key(self, key):
        if self.contains(key):
            # Duplicate keys not allowed
            return False
        # Create and insert a new node and return True
        self.insert_node(BSTNode(key))
        return True

    def remove(self, key):
        parent = None
        current_node = self.root
        # Search for the node
        while current_node is not None:
            # Check if current_node has a matching key
            if current_node.key == key:
                if current_node.left is None and current_node.right is None:
                    # Remove leaf
                    if parent is None:  # Node is root
                        self.root = None
                    elif parent.left is current_node:
                        parent.left = None
                    else:
                        parent.right = None
                    return True  # Node found and removed
                elif current_node.left is not None and current_node.right is None:
                    # Remove node with only left child
                    if parent is None:  # Node is root
                        self.root = current_node.left
                    elif parent.left is current_node:
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    return True  # Node found and removed
                elif current_node.left is None and current_node.right is not None:
                    # Remove node with only right child
                    if parent is None:  # Node is root
                        self.root = current_node.right
                    elif parent.left is current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    return True  # Node found and removed
                else:
                    # Remove node with two children

                    # Find successor (leftmost child of right subtree)
                    successor = current_node.right
                    while successor.left is not None:
                        successor = successor.left

                    # Copy successor's key to current node
                    current_node.key = successor.key

                    # Reassign parent, current_node, and key so that loop
                    # continues with new key
                    parent = current_node
                    current_node = current_node.right
                    key = successor.key
            elif current_node.key < key:
                # Search right
                parent = current_node
                current_node = current_node.right
            else:
                # Search left
                parent = current_node
                current_node = current_node.left
        return False  # Node not found

    def print_node(self, node):
        if node is None:
            return

        self.print_node(node.left)
        print(f"{node.key} ", end="")
        self.print_node(node.right)

    def print(self):
        current_node = self.root
        self.print_node(current_node)

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def print_level(self, node, level):
        if node is None:
            return

        if level == 1:
            print(node.key, end=" ")
        else:
            self.print_level(node.left, level - 1)
            self.print_level(node.right, level - 1)

    def printTree(self):
        self._printTree(self.root, "", True)

    def _printTree(self, node, prefix, is_left):
        if node is None:
            return

        # Print right subtree first (so it appears on top)
        if node.right is not None:
            self._printTree(
                node.right,
                prefix + ("│   " if is_left else "    "),
                False
            )

        # Print current node
        print(prefix + ("└── " if is_left else "┌── ") + str(node.key))

        # Print left subtree
        if node.left is not None:
            self._printTree(
                node.left,
                prefix + ("    " if is_left else "│   "),
                True
            )


class BSTNode:
    def __init__(self, node_key, left_child = None, right_child = None):
        self.key = node_key
        self.left = left_child
        self.right = right_child