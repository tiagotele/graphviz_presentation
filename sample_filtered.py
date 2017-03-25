from graph_tool.all import *
from numpy.random import *  # for random sampling

g, pos = triangulation(random((500, 2)) * 4, type="delaunay")
tree = min_spanning_tree(g)
g.set_edge_filter(tree)
graph_draw(g, pos=pos, output="min_tree_filtered.pdf")
