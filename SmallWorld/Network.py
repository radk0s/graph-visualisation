from igraph import *
import random

class Network(object):
	def __init__(self, nodes = set(), edgeAmount = 0, p = 0):
		self.nodes = nodes
		if edgeAmount > 0 and edgeAmount >= len(nodes):
			raise Exception("Too many edges")
		shortcuts = (int) (p * len(nodes) * edgeAmount / 2)
		if shortcuts > len(nodes) * (len(nodes) - 1) - edgeAmount * len(nodes):
			raise Exception("Too many shortcuts: " + str(shortcuts))

		print self.nodes
		self.generateEdges(edgeAmount)
		self.generateShortcuts(shortcuts)

	def generateEdges(self, amount):
		self.neighbours = {x: set() for x in self.nodes}
		for i in xrange(0, len(self.nodes)):
			end = i + (amount + 1) / 2
			start = end - amount
			neighbours = [self.nodes[x % len(self.nodes)] for x in xrange(start, end + 1) if x != i]
			for n in neighbours:
				if not self.hasEdge(self.nodes[i], n):
					self.addEdge(self.nodes[i], n)

	def generateShortcuts(self, amount):
		print amount
		begins = list(self.nodes)
		edges = {}
		i = 0
		while i < amount:
			x = random.choice(begins)
			if x not in edges: edges[x] = []
			if len(self.neighbours[x]) + len(edges[x]) < len(self.nodes) -1:
				ends = [e for e in begins if not self.hasEdge(x, e)]
				y = random.choice(ends)
				while self.hasEdge(x, y): ends.remove(y); y = random.choice(ends)
				edges[x].append(y)
				self.addEdge(x, y)
				i += 1
			else:
				begins.remove(x)

	def hasEdge(self, n1, n2):
		return n1 in self.neighbours[n2] or n2 in self.neighbours[n1]

	def hasNode(self, node):
		return node in self.nodes

	def addEdge(self, n1, n2):
		if n1 not in self.nodes:
			self.nodes.add(n1)
			self.neighbours[n1] = set()
		if n2 not in self.nodes:
			self.nodes.add(n2)
			self.neighbours[n2] = set()
		if self.hasEdge(n1, n2):
			raise Exception("Already has edge " + str((n1, n2)))
		self.neighbours[n1].add(n2)
		self.neighbours[n2].add(n1)

	def getPathLengthsFromNode(self, node):
		if node not in self.nodes:
			raise Exception("Invalid node")
		distances = {}
		i = 1
		nodes = self.neighbours[node]
		while len(nodes) > 0:
			for n in nodes:
				distances[n] = i
			nodes = {n for x in nodes for n in self.neighbours[x] if n not in distances}
			i += 1
		del distances[node]
		return distances

	def getAllPathLengths(self):
		return {n: self.getPathLengthsFromNode(n) for n in self.nodes}

	def getAveragePathLengthFromNode(self, node):
		lengths = self.getPathLengthsFromNode(node)
		return sum(lengths.values()) / float(len(lengths))

	def getAveragePathLength(self):
		return sum([self.getAveragePathLengthFromNode(n) for n in self.nodes]) / float(len(self.nodes))

	def toIGraph(self):
		g = Graph()
		vertices = [str(x) for x in self.nodes]
		g.add_vertices(vertices)
		added = set()
		for (x, ns) in self.neighbours.iteritems():
			for y in ns:
				if (x, y) not in added and (y, x) not in added:
					g.add_edge(str(x), str(y))
					added.add((x, y))
		return g

def readData(f, delim, g):
	with open(f) as f:
		for line in f:
			if not line.startswith("#"):
				line = line.strip().split(delim)
				g.addEdge(line[0], line[1])
