import math

"""Min Binary Heap Data Structure"""

class MinHeap:

	def __init__(self, nums=None):
		self.heap = []
		if nums:
			self.build_heap(nums)

	def __repr__(self):
		return self.heap

	# Method returns the size of the heap
	def size(self):
		return len(self.heap)

	# Method returns the height of the binary heap which is the log_2(number of elements in the heap)
	def height(self):
		return math.ceil(math.log(len(self.heap)) / math.log(2))

	# Method returns boolean whether or not element is a leaf of the binary heap or not
	def is_leaf(self, elem):
		return elem > int(math.ceil((len(self.heap) -2)/ 2.0))
