class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        self.append_node(SinglyLinkedNode(item))

    def append_node(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        self.prepend_node(SinglyLinkedNode(item))

    def prepend_node(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def search(self, data_value):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data_value:
                return current_node
            current_node = current_node.next
        return None

    def insert_node_after(self, current_node, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif current_node == self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def remove_node_after(self, current_node):
        if current_node is None:
            # Special case: remove head
            self.head = self.head.next
            if self.head is None:
                # Last item was removed
                self.tail = None
        elif current_node.next is not None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node is None:
                # Last item was removed
                self.tail = current_node

    def remove(self, item_to_remove):
        previous = None
        current = self.head
        while current is not None:
            if current.data == item_to_remove:
                self.remove_node_after(previous)
                return True
            # Advance to next node
            previous = current
            current = current.next
        # Not found
        return False

    def find_insertion_position(self, data_value):
        position_a = None
        position_b = self.head
        while position_b is not None and data_value > position_b.data:
            position_a = position_b
            position_b = position_b.next
        return position_a

    def sort(self):
        if self.head is not None:
            previous_node = self.head
            current_node = self.head.next
            # Loop through the list's nodes
            while current_node is not None:
                # Find the insertion position
                next_node = current_node.next
                position = self.find_insertion_position(current_node.data)
                # Insert current_node at that position
                if position is previous_node:
                    previous_node = current_node
                else:
                    self.remove_node_after(previous_node)
                    if position == None:
                        self.prepend_node(current_node)
                    else:
                        self.insert_node_after(position, current_node)
                # Advance to the next node
                current_node = next_node

    def print(self):
        current = self.head
        while current.next is not None:
            print(current.data, end=", ")
            current = current.next
        print(current.data)


class SinglyLinkedNode:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None