graph-visualisation
===================
## iGraph
###Windows installation:
from http://www.lfd.uci.edu/~gohlke/pythonlibs/ download and install:
- Python-igraph
- Pycairo


###Ubuntu installation
 `sudo apt-get install build-essential python-dev`

 `sudo pip install python-igraph`

Histogram dependencies:

 `sudo apt-get install libfreetype6-dev`

 `sudo pip install matplotlib`
 
###Excercise

1. Choose networks from datasets folder (fb - directed graphs, gplus & twitter - directed).
2. Analyze graph properties (example in graph-visualisation/SmallWorld/network_properties.py).
3. Calculate other properties like pageRank, modularity etc. Try plot graph using different layouts (http://igraph.org/python/doc/python-igraph.pdf).
4. Install Gephi http://gephi.github.io/, analyze networks and compare results.

