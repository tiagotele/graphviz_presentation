from graph_tool.all import *
from numpy.random import *  # for random sampling

g, pos = triangulation(random((500, 2)) * 4, type="delaunay")
tree = min_spanning_tree(g)
g.set_edge_filter(tree)


bv, be = betweenness(g)
be.a /= be.a.max() / 5
graph_draw(g, pos=pos, vertex_fill_color=bv, edge_pen_width=be,
           output="filtered-bt.pdf")