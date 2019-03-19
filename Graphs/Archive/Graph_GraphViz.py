from graphviz import Digraph

g = Digraph("G", filename="ENS1.gv")

nodeNum=0
while nodeNum< 24:
	g.node(str(nodeNum))
	nodeNum+=1

g.edge('0','1')


g.view()