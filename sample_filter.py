from graph_tool.all import *
from numpy.random import *  # for random sampling

g, pos = triangulation(random((500, 2)) * 4, type="delaunay")
tree = min_spanning_tree(g)
graph_draw(g, pos=pos, edge_color=tree, output="min_tree.pdf")
