from igraph.drawing.graph import CytoscapeGraphDrawer
from Network import Network, readData

drawer = CytoscapeGraphDrawer()
n = Network()
data = readData("facebook_combined_short.txt", " ", n)
g = n.toIGraph()

# evcent(directed=True, scale=True, weights=None, return_eigenvalue=False,arpack_options=None)
# Calculates the eigenvector centralities of the vertices in a graph.
print g.evcent()

print g.vertex_disjoint_paths() #cohesion
print g.edge_disjoint_paths() #adhesion

# drawer.draw(g)