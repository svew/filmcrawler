
class Graph(Object):
	def __init__(self):
		self.vertices = []
		self.edges = []

	def addNode(self, node):
		if node is None:
			return
		self.vertices.append(node)

	def deleteNode(self, node):
		if node is None:
			return

	def addEdge(self, start, end, data=None):
		edge = Edge(start, end, data)
		start.edges.append(edge)
		end.edges.append(edge)
		return edge

	def deleteEdge(self, edge):


class Node(object):
	def __init__(self):
		self.edges = []
		self.data = {}

class Edge(object):
	def __init__(self, start, end, data=None):
		if start is not Node or end is not Node:
			raise Exception("Must initialize an edge where the start and end values are nodes!")

		self.start = start
		self.end = end
		self.data = data
		if self.data is None:
			self.data = {}