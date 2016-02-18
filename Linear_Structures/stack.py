class Stack:
	# Stack data structure
	def __init__(self):
		self.items = []

	# Method to check the size of the stack
	def size(self):
		return len(self.items)

	# Method to check if the stack is empty
	def isEmpty(self):
		return len(self.items) == 0

	# Method to push item to the top of the stack
	def push(self, item):
		self.items.append(item)

	# Method to pop the top most item of the stack
	def pop(self):
		return self.items.pop()

	# Method to seek the top of the stack
	def seek(self):
		if self.isEmpty(): return None
		return self.items[-1]

	# Method to reverse a string using a stack
	def stringReverse(s):
		stack = Stack()
		reversed = []
		for char in s:
			stack.push(char)
		while not stack.isEmpty():
			reversed.append(stack.pop())
		return "".join(reversed)

# Running tests
if __name__ == "__main__":
	myStack = Stack()
	print(myStack.isEmpty())
	for num in range(0, 100, 10):
		myStack.push(num)
	print(myStack.size())
	print(myStack.seek())
	print(myStack.pop())
	print(myStack.size())
	print(myStack.seek())
	print(myStack.isEmpty())





