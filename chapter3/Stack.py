class Stack:
	def __init__(self):
		self.top = None

	def push(self, new_data):
		self.top = StackNode(new_data, self.top)
		return True

	def pop(self):
		# Copy top node's data
		popped_item = self.top.data
		
		# Remove top node
		self.top = self.top.next
		
		# Return the popped item
		return popped_item

# Node to store an item in a linked-list-based stack
class StackNode:
	def __init__(self, data_value, next_node):
		self.data = data_value
		self.next = next_node