class Queue:
	# Queue data structure
	def __init__(self):
		self.items = []

	# Method to enqueue items to the end of the queue
	def enqueue(self, item):
		self.items.insert(0, item)

	# Method to dequeue front item of the queue
	def dequeue(self):
		self.items.pop()

	# Method returns if the queue is empty
	def isEmpty(self):
		return len(self.items) == 0

	def peek(self):
		return self.items[-1]

	# Method returns the size of the queue
	def size(self):
		return len(self.items)

# Running tests
if __name__ == "__main__":

	myQueue = Queue()
	for num in range(0, 100, 10):
		myQueue.enqueue(num)
	print(myQueue.peek())
	print(myQueue.size())
	print(myQueue.dequeue())
	print(myQueue.size())
