from igraph import plot
from Network import Network, readData

n = Network()
data = readData("facebook_combined_short.txt", " ", n)
# data = readData("p2p-Gnutella06.txt", "\t", n)

# n = Network([str(x) for x in [ 1,2,3,4,5,6,7,8,9]], 2, 0)
# n.addEdge("2", "8")

g = n.toIGraph()

print n.neighbours
print "nodes:", len(n.nodes)
print "edges:", len([x for k in n.neighbours for x in n.neighbours[k]])

print g.path_length_hist()
# betweenness = g.betweenness()
print g.components()
# print g.edge_betweenness()

visual_style = {}
layout = g.layout("circle")

visual_style["layout"] = layout
visual_style["bbox"] = (6400, 3600)

print "plotting evil"
plot(g, **visual_style)
