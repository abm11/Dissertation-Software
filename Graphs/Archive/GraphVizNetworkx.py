import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import sys
from graphviz import render
from networkx.drawing.nx_agraph import graphviz_layout

try:
    import pygraphviz
    from networkx.drawing.nx_agraph import write_dot
    print("using package pygraphviz")
except ImportError:
    try:
        import pydot
        from networkx.drawing.nx_pydot import write_dot
    except ImportError:
        print("Import Fail")
        raise

PM3 = nx.DiGraph()

#Node Generator # Can be OO
nodeNum = 0
while nodeNum < 52:
	PM3.add_node(nodeNum)
	nodeNum += 1

#Graph edges
PM3.add_edges_from([(0, 1), (0,5), (0,16), (0,20), (0,29), (0,33), (0,42), (0,44), (1,2), (2,3), (3,4), (4,51), (5,6),
                    (6,7), (7,8), (8,9), (9,10), (9,11), (10, 51), (11,12), (11,13), (12,13), (13,14), (13,15), (14,51), (15,51), (16,17),
                    (17,18), (18,19), (19,51), (20,21), (21,22), (22,23), (23,24), (24,25), (25,26), (26,27), (27,28), (27,28), (28,51), (29,30), (30,31),
                    (31,32), (32,51), (33,34), (34,35), (35,36), (36,37), (37,38), (38,39), (38,40), (39,51), (40,41), (41,51), (42,43), (43,51),
                    (44,45), (45,46), (46,47), (47,48), (48,49), (48,50), (49,51), (50,51)])


# write_dot(PM3, "SOP/PM3.gv")
# render('dot', 'png', 'SOP/PM3.gv')
#
# pos = nx.nx_pydot.pydot_layout(PM3)
pos = nx.nx_pydot.pydot_layout(PM3, prog='dot')

nx.draw(PM3, pos)
plt.show()