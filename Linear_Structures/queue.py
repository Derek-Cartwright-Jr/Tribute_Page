""" Implementation of a queue data structure where the front item is
located at the far right and the back item is located at the far left."""

class Queue:
	def __init__(self, iteration=[]):
		self.items = []
		self.size = 0
		for item in iteration: self.enqueue(item)

	def __repr__(self):
		return str(self.items)

	def __len__(self):
		return self.size

	def __contains__(self, data):
		return self.search(data)

	""" Adds an item at the back of the queue """
	def enqueue(self, data):
		self.items.insert(0, data)
		self.size += 1

	""" Removes and returns the front item of the queue """
	def dequeue(self):
		return self.items.pop()
		self.size -= 1

	""" Returns if an element is in the queue """
	def search(self, data):
		return data in self.items

	""" Returns if queue is empty or not """
	def isEmpty(self):
		return self.items == []

	""" Returns the front of the queue """
	def seek(self):
		return self.items[-1]

	""" Returns the back of the queue """
	def end(self):
		return self.items[0]

""" Running some tests """
def test():
	q = Queue(range(0,100,10))
	print(q.seek())				# testing seek method
	print(q.end())				# testing end method
	print(q)					# testing __repr__ method
	print(q.isEmpty())			# testing isEmpty method
	print(len(q))				# testing __len__ method
	print(10 in q)				# testing __contains__ method
	for _ in range(len(q)):		# testing dequeue method
		print(q.dequeue())
	print(q)
	print(q.isEmpty())

def main():
	test()

if __name__ == "__main__":
	main()