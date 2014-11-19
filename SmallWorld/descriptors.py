from igraph import *
from Network import Network, readData
from matplotlib import pyplot as plt

def distribution(arr):
    distributions = { x : 0 for x in arr }
    for x in arr :
        distributions[x] += 1
    return distributions

def page_rank(g):
    page_rank = g.pagerank()
    print page_rank
    plt.plot(page_rank)
    plt.show()

def degree_distribution(g):
    degree_distribution = g.degree_distribution()
    print degree_distribution # better visualisation
    plot(degree_distribution)

def indegrees(g):
    indegrees = g.indegree()
    plt.plot(indegrees)
    plt.show()

def outdegrees(g):
    outdegrees = g.outdegree()
    plt.plot(outdegrees)
    plt.show()

def biconnected_components(g):
    result = g.biconnected_components()
    print result

def gomory_hu_tre(g):
    plot(g.gomory_hu_tree())

def other(g):
    print 'adhesion', g.adhesion()
    print 'cohesion', g.cohesion()
    print 'clique', g.omega()   # size of largest clique
    print 'independence', g.alpha() # size of largest independent vertex set

def closeness(g):
    result = g.closeness()
    plt.plot(result)
    plt.show()
    distr = distribution(result)
    plt.plot(distr.keys(), distr.values(), '*')
    plt.show()

if __name__ == "__main__":
    n = Network()
    data = readData("facebook_combined_short.txt", " ", n)
    g = n.toIGraph()

    page_rank(g)
    degree_distribution(g)
    # indegrees(g)
    # outdegrees(g)
    # other(g)
    # g.dyad_census() # divide (u, v) into 3 groups: symmetric, assymetric, no link - onlt directed graphs
    # print g.path_length_hist()
    # print g.components()
    # biconnected_components(g)
    # tree = gomory_hu_tre(g)
    # closeness(g)