class Stack:
	def __init__(self, iteration=[]):
		self.items = []
		self.size = 0
		for item in iteration: self.push(item)

	def __contains__(self, data):
		return data in self.items

	def __len__(self):
		return self.size

	def __repr__(self):
		return str(self.items)

	""" Pushes an item on the top of the stack """
	def push(self, data):
		self.items.append(data)

	def pop(self):
		return self.items.pop()

	""" Returns the top element on the stack """
	def seek(self):
		return self.items[-1]

	""" Returns the bottom element of the stack """
	def bottom(self):
		return self.items[0]

	""" Returns whether or not there are any items on the stack """
	def isEmpty(self):
		return self.items == []

def test():
	s = Stack(range(0,100,10))
	print(s)				# testing __repr__ method
	print(s.isEmpty())		# testing isEmpty
	for _ in range(len(s)): # testing pop function
		print(s.pop())
	print(s.isEmpty())		# testing isEmpty
	for num in range(0, 200, 10): # testing push method
		s.push(num)
	print(len(s))			# testing __len__ method
	print(s.seek())			# testing seek method
	print(s.bottom())		# testing bottom method
	print(20 in s)			# testing __contains__ method

def main():
	test()

if __name__ == "__main__":
	main()