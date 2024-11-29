class Stack:
	def __init__(self):
		self.stack = []

	# Push an item onto the stack
	def push(self, item):
		self.stack.append(item)

	# Pop an item from the stack
	def pop(self):
		if not self.is_empty():
			return self.stack.pop()
		else:
			return "Stack is empty!"

	# Check if the stack is empty
	def is_empty(self):
		return len(self.stack) == 0

	# Get the size of the stack
	def size(self):
		return len(self.stack)
	
	# Peek at the top item of the stack
	def peek(self):
		if not self.is_empty():
			return self.stack[-1]
		else:
			return "Stack is empty!"

		