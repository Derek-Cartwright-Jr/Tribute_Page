""" Graph Data Structure
Methods include: add_nodes, add_node, add_edges, add_edge, has_node,
has_edge, nodes, edges, neighbors, del_node, del_edge, node_order, set_edge_weight,
get_edge_weight"""

class graph:

	DEFAULT_WEIGHT = 1
	DIRECTED = False

	def __init__(self):
		self.node_neighbors = {}

	# Method adds a node to the graph
	def add_node(self, node):
		if node not in self.node_neighbors:
			self.node_neighbors[node] = {}
		else:
			raise Exception("Node %s is already in graph" % node)

	# Method that takes a list of nodes and adds them to our graph
	def add_nodes(self, nodes):
		for node in nodes:
			self.add_node(node)

	# Method checks whether a node exists in the graph or not
	def has_node(self, node):
		return node in self.node_neighbors

	# Method add an edge to the graph connecting two nodes together
	def add_edge(self, edge, wt=DEFAULT_WEIGHT, label=""):
		(u, v) = edge
		if (v not in self.node_neighbors[u] and u not in self.node_neighbors[v]):
			self.node_neighbors[u][v] = wt
			if u!=v:
				self.node_neighbors[v][u] = wt
		else:
			raise Exception("Edge (%s %s) already added in the graph" %(u, v))

	# Method adds multiples edges which will be in the form of a list of tuples
	def add_edges(self, edges):
		for edge in edges:
			self.add_edge(edge)

	# Method returns a list of nodes that are in the graph
	def nodes(self):
		return self.node_neighbors.keys()

	# Method checks wether an edge exists in the graph or not.
	def has_edge(self, edge):
		(u, v) = edge
		return v in self.node_neighbors.get(u, [])

	# Method returns a list of neighbors for a node
	def neighbors(self, node):
		if not self.has_node(node):
			raise "Node %s not in graph" % node
		return self.node_neighbors[node].keys()

	# Method deletes node from the graph
	def delete_node(self, node):
		for each in list(self.neighbors(node)):
			if each != node:
				self.del_edge((each, node))
		del(self.node_neighbors[node])

	# Method deletes edge from a graph
	def delete_edge(self, edge):
		(u, v) = edge
		if not self.has_edge(edge):
			raise Exception("Edge (%s %s) not an existing edge" % (u,v))
		del self.node_neighbors[u][v]
		if u != v:
			del self.node_neighbors[v][u]

	# Method that returns the degree of a node
	def node_order(self, node):
		return len(self.neighbors(node))

	# Method returns a list of edges in the graph
	def edges(self):
		edge_list = []
		for node in self.nodes():
			edges = [(node, each) for each in self.neighbors(node)]
			edge_list.extend(edges)
		return edge_list

	

