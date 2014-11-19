from Network import Network, readData
from igraph import plot
import matplotlib.pyplot as plt

n = Network()
data = readData("facebook_combined_short.txt", " ", n)
g = n.toIGraph(directed = False)

visual_style = {}
layout = g.layout("circle")

visual_style["layout"] = layout
visual_style["bbox"] = (12800, 7200)

print "plotting evil"
plot(g, **visual_style)

print "Diameter:" + str(g.diameter())

avg_path = g.average_path_length(directed=False)
print "Avg path len:" + str(avg_path)
print g.path_length_hist()

plt.hist(g.closeness())
plt.show()

plt.hist(g.eccentricity())
plt.show()

plt.hist(g.betweenness())
plt.show()