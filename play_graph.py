from graph_tool.all import *

g = Graph(directed=True)
# ug = Graph(directed=False)

vertices = g.add_vertex(10)

for vertice in vertices:
	print vertice

# print vertices
v_prop = g.new_vertex_property("string")
v_prop[1] = 'foo'
v_prop[2] = 'bar'

e1 = g.add_edge(0,1)
e2 = g.add_edge(4,5)
e3 = g.add_edge(8,5)
e4 = g.add_edge(9,3)
e5 = g.add_edge(7,2)
e6 = g.add_edge(8,9)

e_prop = g.new_edge_property("string")
e_prop[e1] = 'edge 1'
e_prop[e2] = 'edge 2'


graph_draw(g,vertex_text=v_prop,edge_text=e_prop ,vertex_font_size=18, output_size=(900,900),output="graph.png")
