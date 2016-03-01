""" Binary Search Tree """

class TreeNode:
	def __init__(self, data):
		self.value = data
		self.parent = None
		self.left = None
		self.right = None

	""" Getter and Setter Methods """
	def get_value(self):
		return self.value

	def get_left(self):
		return self.left

	def get_right(self):
		return self.right

	def get_parent(self):
		return self.parent 

	def set_left(self, node):
		self.left = node

	def set_right(self, node):
		self.right = node

	def set_parent(self, node):
		self.parent = node

	""" Check to see if a node is a leaf or root """
	def is_root(self):
		return self.parent == None

	def is_leaf(self):
		return self.right == self.left == None

class BinarySearchTree:
	def __init__(self):
		self.root = None
		self.size = 0

	def __len__(self):
		return self.size

	def __contains__(self, data):
		return self.search(data)

	""" Method returns if the tree is empty or not """
	def is_empty(self):
		return self.get_root() == None

	""" Method returns the root of the tree """
	def get_root(self):
		if self.root == None:
			return "No root in the tree"
		else:
			return self.root

	""" Insert Method for the tree """
	def insert(self, value):
		new_node = TreeNode(value)
		if self.root:
			node = self.root
			while node and node.value != value:
				parent = node
				if node.value < value:
					node = node.right
				else:
					node = node.left
			if parent.value > value:
				parent.set_left(new_node)
			else:
				parent.set_right(new_node)
			new_node.set_parent(parent)
		else:
			self.root = new_node
		self.size += 1
		return

	""" Binary Search method for the tree """
	def search(self, data):
		found = False
		current = self.root
		if current == None:
			return found
		else:
			while current and not found:
				if current.get_value() == data:
					found = True
				elif data > current.get_value():
					current = current.get_right()
				else:
					current = current.get_left()
			return found

	""" Tree Traversals """

	""" Traversal returns sorted list of values """
	def _inOrder(self, node, values):
		if node != None:
			self._inOrder(node.get_left(), values)
			values.append(node.get_value())
			self._inOrder(node.get_right(), values)

	def _preOrder(self, node, values):
		if node != None:
			values.append(node.get_value())
			self._preOrder(node.get_left(), values)
			self._preOrder(node.get_right(), values)

	def _postOrder(self, node, values):
		if node != None:
			self._postOrder(node.get_left(), values)
			self._postOrder(node.get_right(), values)
			values.append(node.get_value())

	""" Method to return a list of values of the binary search tree
	in a specific order """
	def get_values(self, order="in"):
		values = []
		if order == "in":
			self._inOrder(self.root, values)
		elif order == "pre":
			self._preOrder(self.root, values)
		else:
			self._postOrder(self.root, values)
		return values

	""" Reverse Sorted Order """
	def reverse_sort(self):
		return self.get_values()[::-1]

""" Running some tests """
def test():
	bst = BinarySearchTree()
	bst.insert(10)
	bst.insert(11)
	bst.insert(5)
	print(bst.root.get_right().get_value())
	print(len(bst))
	print(bst.search(11))
	print(bst.get_values("in"))
	print(bst.reverse_sort())

def main():
	test()

if __name__ == "__main__":
	main()
