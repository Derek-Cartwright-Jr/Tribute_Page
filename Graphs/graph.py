"""Graph Data Structure"""

class Graph:
	def __init__(self):
		# set of nodes
		self.node_neighbors = {}

	def add_nodes(self, nodes):
		for node in nodes:
			if node not in self.node_neighbors:
				self.node_neighbors[node] = {}
			else:
				raise Exception("This node is already in the set")

	def add_edge(self, edge, wt):
		begin, end = edge
		if (end not in self.node_neighbors[begin] and begin not in self.node_neighbors[end]):
			self.node_neighbors[begin][end] = wt
			if begin!=end:
				self.node_neighbors[end][begin] = wt
		else:
			raise Exception("Edge (%s, %s) is already in the graph" %(begin, end))
	def add_edges(self, edges):
		for edge in edges:
			self.add_edge(edge)

	def has_node(self, node):
		return node in self.node_neighbors

	def has_edge(self, edge):
		begin, end = edge
		return end in self.node_neighbors.get(begin, [])

	def nodes(self):
		return self.node_neighbors.keys()
	
	def neighbors(self, node):
		if not self.has_node(node):
			raise "Node %s not in graph" % node
		return self.node_neighbors[node].keys()

	def del_node(self, node):
		for each in list(self.neighbors(node)):
			if each != node:
				self.del_edge((each, node))
		del(self.node_neighbors[node])