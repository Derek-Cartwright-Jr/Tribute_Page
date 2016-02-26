class Node:
	def __init__(self, data):
		self.data = data
		self.next = None 

	def __repr__(self):
		return str(self.data)

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, node):
		self.next = node

class LinkedList:
	def __init__(self, iterator=[]):
		self.head = None
		self.length = 0
		for item in iterator: self.add_head(item)

	""" Overriding built in function that gets called when we use len(LinkedList) 
	function to see the length of the linked list """
	def __len__(self):
		return self.length

	""" Overriding built in function that gets called when we want to search a 
	container for a specific object or data element """
	def __contains__(self, data):
		return self.search(data)

	""" Representation of our linked list class """
	def __repr__(self):
		current, items = self.head, []
		while current:
			items.append(str(current))
			current = current.get_next()
		return '->'.join(items)

	""" Returns the head (first data element) of the linked list """
	def get_head(self):
		return self.head

	""" Returns the last data element of the linked list """
	def get_tail(self):
		current = self.head
		while current.get_next():
			current = current.get_next()
		return current

	""" Add a data element to the front of the linked list """
	def add_head(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node
		self.length += 1

	""" Add a data element at the end of the linked list """
	def append(self, data):
		new_node = Node(data)
		current = self.head
		while current.get_next():
			current = current.get_next()
		current.set_next(new_node)

	""" Remove the last data element from the linked list """
	def pop(self):
		prev = None
		current = self.head
		while current.get_next():
			prev = current
			current = current.get_next()
		prev.set_next(current.get_next())
		current.set_next(None)
		self.length -= 1

	""" Removes a data element from the linked list """
	def remove(self, data):
		if len(self) == 0:
			return "No elements in the list"
		prev = None
		current = self.head
		found = False
		while current and not found:
			if current.get_data() == data:
				found = True
			else:
				prev = current 
				current = current.next
		if found:
			self.length -= 1
			if prev == None:
				self.head = self.head.get_next()
			else:
				prev.next = current.get_next()

	""" Search for an element in the linked list """
	def search(self, data):
		current = self.head
		found = False
		while current and not found:
			if current.get_data() == data:
				found = True
			else:
				current = current.get_next()

		return found, current.get_data()

	""" Reverses the linked list iteratively """
	def reverse(self):
		prev = None
		current = self.head
		while current:
			current.next, current, prev = prev, current.next, current
		self.head = prev
		return self.head

	""" Merge Sort Method to sort the linked list """
	def sort(self):
		if self.head == None or len(self) == 1:
			return self
			
		left = self._split()[0]
		right = self._split()[1]

		left.sort()
		right.sort()

		return self.merge(left, right)

	""" Helper Merge method """
	def _merge(self, left, right):
		if not len(left):
			return left
		elif not len(right):
			return right

		result = LinkedList()

		head_l = left.head
		head_r = right.head

		while(len(result) < len(left) + len(right)):
			if head_l.get_data() <= head_r.get_data():
				result.add_head(headl_l.get_data())
				head_l = head_l.get_next()
				left.length -= 1
			else:
				result.add_head(head_r.get_data())
				head_r = head_r.get_next()
				right.length -= 1

		return result
		

			
	""" Helper splitting method """
	def _split(self):
		current = self.head 
		count = 0
		middle = len(self)//2
		left_list = LinkedList()
		right_list = LinkedList()
		while count < middle:
			left_list.add_head(current.get_data())
			current = current.get_next()
			count += 1
		while current:
			right_list.add_head(current.get_data())
			current = current.get_next()
		left_list.reverse()
		right_list.reverse()
		return left_list, right_list

""" Running some tests """
def test():
		L = LinkedList(range(0, 100, 10))
		print(L)		
		print(len(L))	# testing __len__ function
		L.pop()			# testing pop method
		print(L)
		L.add_head(23)	# testing add_head method
		print(23 in L)	# testing __contains__
		print(L.search(23)) # testing search method
		print(L)		
		L.remove(23)	# testing remove method
		print(L)
		L.reverse()		# testing reverse method
		print(L)
		print(L.get_head()) # testing get_head method
		print(L.get_tail()) # testing get_tail method
		L.append(25)	# testing append method
		print(L)		
		


def main():
	test()

if __name__ == "__main__":
	main()





	