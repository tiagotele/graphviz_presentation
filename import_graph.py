from graph_tool.all import *

g = load_graph("price.xml.gz")

graph_draw(g,vertex_text=g.vertex_index, vertex_font_size=18, output_size=(200,200),output="graph_restored.png")