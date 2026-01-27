from chapter2.DoublyLinkedNode import DoublyLinkedNode

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, item):
		self.append_node(DoublyLinkedNode(item))

	def append_node(self, new_node):
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			new_node.previous = self.tail
			self.tail = new_node

	def prepend(self, item):
		self.prepend_node(DoublyLinkedNode(item))

	def prepend_node(self, new_node):
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			new_node.next = self.head
			self.head.previous = new_node
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
			new_node.previous = self.tail
			self.tail = new_node
		else:
			successor = current_node.next
			new_node.next = successor
			new_node.previous = current_node
			current_node.next = new_node
			successor.previous = new_node

	def remove(self, item_to_remove):
		node_to_remove = self.search(item_to_remove)
		if node_to_remove is not None:
			self.remove_node(node_to_remove)
			return True
		return False

	def remove_node(self, current_node):
		successor = current_node.next
		predecessor = current_node.previous

		if successor is not None:
			successor.previous = predecessor
		if predecessor is not None:
			predecessor.next = successor

		if current_node == self.head:
			self.head = successor
		if current_node == self.tail:
			self.tail = predecessor

	def sort(self):
		if self.head is not None:
			current_node = self.head.next
			while current_node is not None:
				next_node = current_node.next
				search_node = current_node.previous
				while search_node is not None and search_node.data > current_node.data:
					search_node = search_node.previous
				if search_node is None:
					self.remove_node(current_node)
					current_node.previous = None
					self.prepend_node(current_node)
				elif search_node.next is not current_node:
					self.remove_node(current_node)
					self.insert_node_after(search_node, current_node)
				current_node = next_node

	def print(self):
		current = self.head
		while current.next is not None:
			print(current.data, end=", ")
			current = current.next
		print(current.data)

	def print_reverse(self):
		current = self.tail
		while current.previous is not None:
			print(current.data, end=", ")
			current = current.previous
		print(current.data)