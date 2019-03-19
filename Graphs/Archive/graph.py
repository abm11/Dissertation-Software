import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()
# G.add_nodes_from([1, 15])
H = nx.path_graph(24)
G.add_nodes_from(H)
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14),
(2, 19), (19, 20), (20, 14),
(2, 16), (16, 17), (17, 18), (18, 14),
(9, 21), (21, 14), (11, 23), (23, 14),
(12, 22), (22, 14), (1, 15), (15, 14),
(12, 22), (22, 14), (1, 15), (15, 14)])
pos = nx.spring_layout(G)
plt.figure(1)
nx.draw(G, pos, with_labels=True)

nodeNum = (G.number_of_nodes())
edgeNum = (G.number_of_edges())
print ("\n")
print ("Number of nodes = " + str(nodeNum) + " Number of edges = "+ str(edgeNum))
cyclomaticNumber = (edgeNum-nodeNum)+1
print ("Cyclomatic number = " + str(cyclomaticNumber))
cyclomaticComplexity = 2*(edgeNum - nodeNum + 2)
print ("Cyclomatic complexity = " + str(cyclomaticComplexity))
if cyclomaticComplexity<20:
    print ("Process is low complexity")
elif cyclomaticComplexity>20 and cyclomaticComplexity<40:
    print ("Process is medium complexity")
elif cyclomaticComplexity>60:
    print ("Process is high complexity")
print ("\n")
A = nx.DiGraph()
# G.add_nodes_from([1, 15])
B = nx.path_graph(21)
A.add_nodes_from(B)
A.add_edges_from([(0, 1), (1, 20), (2, 3), (3, 4), (17, 4), (4, 5), (2, 9), (6, 7), (7, 8), (8, 9), (9, 20), (10, 11), (11, 12), (12, 13), (13, 14),
(8, 19), (19, 20), (20, 14),
(2, 16), (13, 17), (17, 18), (12, 14), (17, 22)])
pos = nx.spring_layout(G)

nodeNumA = (A.number_of_nodes())
edgeNumA = (A.number_of_edges())
print ("Number of nodes = " + str(nodeNumA) + " Number of edges = "+ str(edgeNumA))
cyclomaticNumberA = (edgeNumA-nodeNumA)+1
print ("Cyclomatic number = " + str(cyclomaticNumberA))
cyclomaticComplexityA = 2*(edgeNumA - nodeNumA + 2)
print ("Cyclomatic complexity = " + str(cyclomaticComplexityA))
if cyclomaticComplexityA<20:
    print ("Process is low complexity")
elif cyclomaticComplexityA>20 and cyclomaticComplexity<40:
    print ("Process is medium complexity")
elif cyclomaticComplexityA>60:
    print ("Process is high complexity")
print ("\n")

# nx.draw_networkx_edge_labels(G,pos,edge_labels={(2, 19):'Yes', (2, 16):'Yes', (2, 3):'No', (11, 23):'No', (11, 12):'Yes'},font_color='red')
plt.figure(2)
nx.draw(B, pos, with_labels=True)
plt.show()
