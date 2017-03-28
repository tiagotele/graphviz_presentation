#!/usr/bin/python
# -*- coding: latin-1 -*-
from graph_tool.all import *

g = Graph(directed=True)

vertices = g.add_vertex(8)

# print vertices
v_prop = g.new_vertex_property("string")
v_prop[0] = 'Fortaleza'
v_prop[1] = 'Maracanaú'
v_prop[2] = 'Maranguape'
v_prop[3] = 'Caucaia'
v_prop[4] = 'Sobral'
v_prop[5] = 'Tianguá'
v_prop[6] = 'Juazeiro'
v_prop[7] = 'Crato'

e1 = g.add_edge(0,1)
g.add_edge(1,0)
e2 = g.add_edge(0,2)
g.add_edge(2,0)
e3 = g.add_edge(0,3)
e4 = g.add_edge(4,5)
e5 = g.add_edge(4,0)
e6 = g.add_edge(6,7)
e7 = g.add_edge(6,0)
# e6 = g.add_edge(8,9)

e_prop = g.new_edge_property("int")
e_prop[e1] = '10'
e_prop[e2] = '10'
e_prop[e3] = '20'
e_prop[e4] = '20'
e_prop[e5] = '50'
e_prop[e6] = '50'
e_prop[e7] = '50'

graph_draw(g,vertex_text=v_prop,edge_text=e_prop ,vertex_font_size=18, output_size=(800,800),output="graph.png")
g.save("tiago.dot")
