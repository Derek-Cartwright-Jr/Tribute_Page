"""Binary Search Tree data structure"""

class TreeNode:
	def __init__(self, value):
		self.parent = None
		self.right = None
		self.left = None
		self.value = value

	def __repr__(self):
		return str(self.value)

	# Method sets the left child of a node
	def set_left(self, node):
		self.left = node

	# Method sets the right child of a node
	def set_right(self, node):
		self.right = node

	# Method sets the parent of a node
	def set_parent(self, node):
		self.parent = node

	# Method checks to see if the node is a root
	def is_root(self):
		return not self.parent

	# Method checks to see if the node is a leaf
	def is_leaf(self):
		return not (self.right or self.left)

	# Method checks if node is a right child
	def is_right(self):
		return self.parent and self.parent.right == self

	# Method checks if node is a left child
	def is_left(self):
		return self.parent and self.parent.left == self

	# Method checks to see if the node has any children
	def any_children(self):
		return self.right or self.left

	# Method check to see if the node has both children
	def has_both(self):
		return self.right and self.left

class BinarySearchTree:
	def __init__(self):
		self.root = None
		self.size = 0

	# Method to retrieve the root of the binary search treeb
	def get_root(self):
		return self.root

	# Method to insert a tree node into the binary search tree
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

	# Method to search for a tree node value in the binary search tree
	def search(self, value):
		found = False
		node = self.root
		while node and not found:
			if node.value == value:
				found = True
			elif node.value < value:
				node = node.right
			else:
				node = node.left
		if node == None:
			return found
		else:
			return found, node

	# Method to delete a tree node in the binary search tree
	def delete(self, value):
		node = self.search(value)[1]
		if not node:
			return "Node doesn't exist in the tree."
		if not node.left or not node.right:
			node_spliced = node
		else:
			node_spliced = self.successor(node.value)
		if node_spliced.left:
			temp = node_spliced.left
		else:
			temp = node_spliced.right
		if temp:
			temp.set_parent(node_spliced.parent)
		if not node_spliced.parent:
			self.root = temp
		elif node_spliced == node_spliced.parent.left:
			node_spliced.parent.set_left(temp)
		else:
			node_spliced.parent.set_right(temp)

		if node != node_spliced:
			node.value = node_spliced.value
		return node_spliced

	# Method returns the successor of a tree node
	def successor(self, value):
		node = self.search(value)[1]
		if not node:
			return None
		if node.right:
			return self._maxmin(node.right, find_min=True)
		parent = node.parent
		while parent and parent.right == node:
			node = parent
			praent = parent.parent
		return parent

	# Method to get the maximum valued tree node
	def get_max(self):
		return self._maxmin(self.root, find_min=False)

	# Method to get the minimum valued tree node
	def get_min(self):
		return self._maxmin(self.root, find_min=True)

	# Helper method to find min and max values of the binary search tree
	def _maxmin(self, root, find_min=True):
		while (find_min and root.left) or (not find_min and root.right):
			if find_min:
				root = root.left
			else:
				root = root.right
		return root

	# Method to display the values of the binary search tree by default: inorder
	def disp_values(self, order="in"):
		values = []
		if order == "in":
			self._inorder(self.root, values)
		elif order == "pre":
			self._preorder(self.root, values)
		else:
			self._postorder(self.root, values)
		return values

	def leaves(self):
		leaves = []
		for node in self.disp_values():
			if node.is_leaf():
				leaves.append(node)
		return leaves

	# Helper method to traverse tree in order
	def _inorder(self, node, values):
		if node != None:
			self._inorder(node.left, values)
			values.append(node)
			self._inorder(node.right, values)

	# Helper method to traverse tree in pre order
	def _preorder(self, node, values):
		if node != None:
			values.append(node)
			self._preorder(node.left, values)
			self._preorder(node.right, values)

	# Helper method to traverse tree in post order
	def _postorder(self, node, values):
		if node != None:
			self._postorder(node.left, values)
			self._postorder(node.right, values)
			values.append(node)

	# Method is called by built in python function (in) to return the results of search
	def __contains__(self, value):
		return self.search(value)

# Running some tests
if __name__ == "__main__":
	bst = BinarySearchTree()
	bst.insert(23)
	bst.insert(12)
	bst.insert(32)
	bst.insert(25)
	bst.insert(1)
	bst.insert(8)
	print(bst.search(8))
	print(8 in bst)
	print(4 in bst)
	print(0 in bst)
	print(bst.delete(8))
	print(8 in bst)
	bst.insert(8)
	print(bst.disp_values())
	print(bst.disp_values(order="pre"))
	print(bst.disp_values(order="post"))
	print(bst.leaves())
	print(bst.get_max())
	print(bst.get_min())
	print(bst.get_root())

