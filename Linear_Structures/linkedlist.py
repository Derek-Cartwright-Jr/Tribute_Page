class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	# Formal representation of each node in the linked list
	def __repr__(self):
		return str(self.data)
	# Setters and Getters

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setNext(self, node):
		self.next = node

class LinkedList:
	def __init__(self):
		self.head = None
		self.length = 0

	# Method to add a new node to the head of the list
	def append(self, data):
		node = Node(data)
		node.setNext(self.head)
		self.head = node
		self.length += 1

	# Method to search for data in the list
	def search(self, data):
		found = False
		current = self.head

		while current and not found:
			if current.data == data:
				found = True
			else:
				current = current.next

		return found

	# Method to remove a node from the list
	def delete(self, data):
		found = False
		current = self.head
		prev = None

		while current and not found:
			if current.getData() == data:
				found = True

			else:
				current = current.next

		if found:
			self.length -= 1
			if prev == None:
				self.head = self.head.next
			else:
				prev.setNext(current.next)

	# Method to return head of the list
	def getHead(self):
		return self.head

	# Method to return tail of the list
	def getTail(self):
		current = self.head
		while current.next:
			current = current.next
		return current

	# Method to return size of the list
	def size(self):
		return self.length

	# Method to reverse a linked list iteratively
	def reverse(self):
		current = self.head
		prev = None
		while current:
			current.next, current, prev = prev, current.next, current
		self.head = prev
		return self.head

	# Method that will describe the formal representation of the linked list
	def __repr__(self):
		current, nodes = self.head, []
		while current:
			nodes.append(str(current))
			current = current.next
		return '->'.join(nodes)

# Running some tests
if __name__ == "__main__":
	myList = LinkedList()
	myList.append(1)
	myList.append(2)
	myList.append(3)
	myList.append(4)
	myList.append(5)
	myList.append(6)
	print(myList)
	myList.delete(3)
	myList.delete(4)
	print(myList)
	print(myList.search(6))
	print(myList.getHead())
	print(myList.getTail())
	myList.reverse()
	print(myList)



