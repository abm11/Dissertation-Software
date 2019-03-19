import matplotlib.pyplot as plt
import networkx as nx
import sys

#####################UPDATE##############################
try:
    import pygraphviz
    from networkx.drawing.nx_agraph import write_dot
    print("using package pygraphviz")
except ImportError:
    try:
        import pydot
        from networkx.drawing.nx_pydot import write_dot
        print("using package pydot")
    except ImportError:
        print()
        print("Both pygraphviz and pydot were not found ")
        print("see  https://networkx.github.io/documentation/latest/reference/drawing.html")
        print()
        raise

########################UPDATETETET#############

#Graph Nodes
GENS1 = nx.DiGraph()
GENS1.add_node(0,pos=(3,14))
GENS1.add_node(1,pos=(3,13))
GENS1.add_node(2,pos=(2,12))
GENS1.add_node(3,pos=(3,11))
GENS1.add_node(4,pos=(3,10))
GENS1.add_node(5,pos=(3,9))
GENS1.add_node(6,pos=(3,8))
GENS1.add_node(7,pos=(3,7))
GENS1.add_node(8,pos=(3,6))
GENS1.add_node(9,pos=(3,5))
GENS1.add_node(10,pos=(3,4))
GENS1.add_node(11,pos=(3,3))
GENS1.add_node(12,pos=(3,2))
GENS1.add_node(13,pos=(3,1))
GENS1.add_node(14,pos=(3,0))
GENS1.add_node(15,pos=(7,0))
GENS1.add_node(16,pos=(1,11))
GENS1.add_node(17,pos=(1,10))
GENS1.add_node(18,pos=(1,9))
GENS1.add_node(19,pos=(0,11))
GENS1.add_node(20,pos=(0,10))
GENS1.add_node(21,pos=(6,1))
GENS1.add_node(22,pos=(4,1))
GENS1.add_node(23,pos=(5,1))

#Graph edges
GENS1.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14),
(2, 19), (19, 20), (20, 14), (2, 16), (16, 17), (17, 18), (18, 14), (9, 21), (21, 14), (11, 23), (23, 14), (12, 22), (22, 14), (1, 15), (15, 14),
(12, 22), (22, 14), (1, 15), (15, 14)])

pos=nx.get_node_attributes(GENS1,'pos')
plt.figure(1)
plt.title("ENS1")

nx.draw(GENS1, pos, with_labels=True)
write_dot(GENS1, "GENS1")

########################################################################################################################

#Graph Nodes
GENS2 = nx.DiGraph()
GENS2.add_node(0,pos=(2,9))
GENS2.add_node(1,pos=(1,8))
GENS2.add_node(2,pos=(1,7))
GENS2.add_node(3,pos=(1,6))
GENS2.add_node(4,pos=(1,5))
GENS2.add_node(5,pos=(0,4))
GENS2.add_node(6,pos=(1,4))
GENS2.add_node(7,pos=(3,8))
GENS2.add_node(8,pos=(3,7))
GENS2.add_node(9,pos=(3,6))
GENS2.add_node(10,pos=(3,5))
GENS2.add_node(11,pos=(3,4))
GENS2.add_node(12,pos=(3,3))
GENS2.add_node(13,pos=(4,2))
GENS2.add_node(14,pos=(2,2))
GENS2.add_node(15,pos=(2,1))
GENS2.add_node(16,pos=(2,0))

#Graph edges
GENS2.add_edges_from([(0, 1), (0, 7), (1, 2), (2, 3), (3, 4), (4, 6), (4, 5), (5, 16), (6, 8), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 14), (12, 13), (13, 16), (14, 15), (15, 16)])

pos=nx.get_node_attributes(GENS2,'pos')
plt.figure(2)
plt.title("ENS2")
nx.draw(GENS2, pos, with_labels=True)
write_dot(GENS2, "GENS2")
########################################################################################################################

#Graph Nodes
GENS3 = nx.DiGraph()
GENS3.add_node(0,pos=(2,10))
GENS3.add_node(1,pos=(1,9))
GENS3.add_node(2,pos=(1,8))
GENS3.add_node(3,pos=(1,7))
GENS3.add_node(4,pos=(1,6))
GENS3.add_node(5,pos=(0,5))
GENS3.add_node(6,pos=(1,5))
GENS3.add_node(7,pos=(3,9))
GENS3.add_node(8,pos=(3,8))
GENS3.add_node(9,pos=(3,7))
GENS3.add_node(10,pos=(3,6))
GENS3.add_node(11,pos=(3,5))
GENS3.add_node(12,pos=(3,4))
GENS3.add_node(13,pos=(2,3))
GENS3.add_node(14,pos=(2,2))
GENS3.add_node(15,pos=(4,3))
GENS3.add_node(16,pos=(4,2))
GENS3.add_node(17,pos=(4,1))
GENS3.add_node(18,pos=(3,10))
GENS3.add_node(19,pos=(2,0))

#Graph edges
GENS3.add_edges_from([(0, 1), (0, 18), (1, 2), (2, 3), (3, 4), (4, 6), (4, 5),(5, 19), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (12, 15), (13, 14),  (14, 19), (15, 16), (16,17), (17, 19), (18,7)])

pos=nx.get_node_attributes(GENS3,'pos')
plt.figure(3)
plt.title("ENS3")
nx.draw(GENS3, pos, with_labels=True)
write_dot(GENS3, "GENS3")
########################################################################################################################

#Graph Nodes
PM1 = nx.DiGraph()
PM1.add_node(0,pos=(1,9))
PM1.add_node(1,pos=(1,8))
PM1.add_node(2,pos=(1,7))
PM1.add_node(3,pos=(1,6))
PM1.add_node(4,pos=(2,5))
PM1.add_node(5,pos=(3,4))
PM1.add_node(6,pos=(3,3))
PM1.add_node(7,pos=(3,2))
PM1.add_node(8,pos=(2,2))
PM1.add_node(9,pos=(0,5))
PM1.add_node(10,pos=(0,4))
PM1.add_node(11,pos=(2,0))

#Graph edges
PM1.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (3, 9), (4, 5), (4, 8), (5, 6), (6, 7), (6, 8), (7, 11), (8, 11), (9, 10), (10, 11)])

pos=nx.get_node_attributes(PM1,'pos')
plt.figure(4)
plt.title("Start of Enteric Process Map")
nx.draw(PM1, pos, with_labels=True)
write_dot(PM1, "PM1")
########################################################################################################################

#Graph Nodes
PM2 = nx.DiGraph()
PM2.add_node(0,pos=(3,12))
PM2.add_node(1,pos=(3,11))
PM2.add_node(2,pos=(0,10))
PM2.add_node(3,pos=(0,9))
PM2.add_node(4,pos=(0,8))
PM2.add_node(5,pos=(1,7))
PM2.add_node(6,pos=(0,7))
PM2.add_node(7,pos=(1,6))
PM2.add_node(8,pos=(0,6))
PM2.add_node(9,pos=(0,5))
PM2.add_node(10,pos=(0,4))
PM2.add_node(11,pos=(1,3))
PM2.add_node(12,pos=(0,2))
PM2.add_node(13,pos=(2,10))
PM2.add_node(14,pos=(2,9))
PM2.add_node(15,pos=(3,8))
PM2.add_node(16,pos=(3,7))
PM2.add_node(17,pos=(4,10))
PM2.add_node(18,pos=(5,10))
PM2.add_node(19,pos=(5,9))
PM2.add_node(20,pos=(5,8))
PM2.add_node(21,pos=(5,7))
PM2.add_node(22,pos=(4,6))
PM2.add_node(23,pos=(4,5))
PM2.add_node(24,pos=(4,4))
PM2.add_node(25,pos=(4,3))
PM2.add_node(26,pos=(6,6))
PM2.add_node(27,pos=(6,5))
PM2.add_node(28,pos=(7,3))
PM2.add_node(29,pos=(6,4))
PM2.add_node(30,pos=(6,3))
PM2.add_node(31,pos=(8,10))
PM2.add_node(32,pos=(8,9))
PM2.add_node(33,pos=(8,8))
PM2.add_node(34,pos=(8,7))
PM2.add_node(35,pos=(8,6))
PM2.add_node(36,pos=(8,5))
PM2.add_node(37,pos=(8,4))
PM2.add_node(38,pos=(8,3))
PM2.add_node(39,pos=(8,2))
PM2.add_node(40,pos=(7,1))
PM2.add_node(41,pos=(10,10))
PM2.add_node(42,pos=(10,9))
PM2.add_node(43,pos=(10,8))
PM2.add_node(44,pos=(10,7))
PM2.add_node(45,pos=(10,6))
PM2.add_node(46,pos=(10,5))
PM2.add_node(47,pos=(10,4))
PM2.add_node(48,pos=(10,3))
PM2.add_node(49,pos=(10,2))
PM2.add_node(50,pos=(10,1))
PM2.add_node(51,pos=(4,0))

#Graph edges
PM2.add_edges_from([(0, 1), (1, 2), (1, 13), (1, 17), (1, 18), (1, 31), (2, 3), (3, 4), (4, 5), (4, 6), (5, 51), (6, 7), (6, 8), (7, 51), (8, 9), (9, 10), (9, 11), (10,12),
(11, 12), (12, 51), (13, 14), (14, 15), (15, 16), (16, 51), (17, 15), (18, 19), (19, 20), (20, 21), (21, 22), (21, 26), (22, 23), (23, 24), (24, 25), (25, 51),
(26, 27), (27, 28), (27, 29), (28, 51), (29, 30), (30, 51), (31, 32), (32, 33), (33, 34), (34, 35), (35, 36), (36, 37), (37, 38), (38, 39),(39, 40), (39, 41), (40, 51),
(41, 42), (42, 43), (43, 44), (44, 45), (45, 46), (46, 47), (47, 48), (48, 49), (49, 50), (50, 51)])

pos=nx.get_node_attributes(PM2,'pos')
plt.figure(5)
plt.title("Routine Enteric Process map")
nx.draw(PM2, pos, with_labels=True)
write_dot(PM1, "PM1")
########################################################################################################################

#Graph Nodes
PM3 = nx.DiGraph()
PM3.add_node(0,pos=(5,12))
PM3.add_node(1,pos=(0,11))
PM3.add_node(2,pos=(0,10))
PM3.add_node(3,pos=(0,9))
PM3.add_node(4,pos=(0,3))
PM3.add_node(5,pos=(1,11))
PM3.add_node(6,pos=(1,10))
PM3.add_node(7,pos=(1,9))
PM3.add_node(8,pos=(1,8))
PM3.add_node(9,pos=(1,7))
PM3.add_node(10,pos=(2,5))
PM3.add_node(11,pos=(1,5))
PM3.add_node(12,pos=(2,4))
PM3.add_node(13,pos=(1,4))
PM3.add_node(14,pos=(1,3))
PM3.add_node(15,pos=(2,3))
PM3.add_node(16,pos=(3,11))
PM3.add_node(17,pos=(3,10))
PM3.add_node(18,pos=(3,9))
PM3.add_node(19,pos=(3,5))
PM3.add_node(20,pos=(4,11))
PM3.add_node(21,pos=(4,10))
PM3.add_node(22,pos=(4,9))
PM3.add_node(23,pos=(4,8))
PM3.add_node(24,pos=(4,7))
PM3.add_node(25,pos=(4,6))
PM3.add_node(26,pos=(4,5))
PM3.add_node(27,pos=(4,4))
PM3.add_node(28,pos=(4,3))
PM3.add_node(29,pos=(5,11))
PM3.add_node(30,pos=(5,10))
PM3.add_node(31,pos=(5,9))
PM3.add_node(32,pos=(5,3))
PM3.add_node(33,pos=(6,11))
PM3.add_node(34,pos=(6,10))
PM3.add_node(35,pos=(6,9))
PM3.add_node(36,pos=(6,8))
PM3.add_node(37,pos=(6,7))
PM3.add_node(38,pos=(6,6))
PM3.add_node(39,pos=(6,3))
PM3.add_node(40,pos=(7,5))
PM3.add_node(41,pos=(7,3))
PM3.add_node(42,pos=(8,11))
PM3.add_node(43,pos=(8,3))
PM3.add_node(44,pos=(10,11))
PM3.add_node(45,pos=(10,10))
PM3.add_node(46,pos=(10,9))
PM3.add_node(47,pos=(10,8))
PM3.add_node(48,pos=(10,7))
PM3.add_node(49,pos=(9,3))
PM3.add_node(50,pos=(10,3))
PM3.add_node(51,pos=(5,0))

#Graph edges
PM3.add_edges_from([(0, 1), (0,5), (0,16), (0,20), (0,29), (0,33), (0,42), (0,44), (1,2), (2,3), (3,4), (4,51), (5,6),
                    (6,7), (7,8), (8,9), (9,10), (9,11), (10, 51), (11,12), (11,13), (12,13), (13,14), (13,15), (14,51), (15,51), (16,17),
                    (17,18), (18,19), (19,51), (20,21), (21,22), (22,23), (23,24), (24,25), (25,26), (26,27), (27,28), (27,28), (28,51), (29,30), (30,31),
                    (31,32), (32,51), (33,34), (34,35), (35,36), (36,37), (37,38), (38,39), (38,40), (39,51), (40,41), (41,51), (42,43), (43,51),
                    (44,45), (45,46), (46,47), (47,48), (48,49), (48,50), (49,51), (50,51)])

pos=nx.get_node_attributes(PM3,'pos')
plt.figure(6)
plt.title("Enterics Extras Process Map")
nx.draw(PM3, pos, with_labels=True)
write_dot(PM3, "PM3")


########################################################################################################################

#List graphs
graph_list = [GENS1, GENS2, GENS3, PM1, PM2, PM3]
for graphList in graph_list:
#     nodeNum = (x.number_of_nodes())
#     edgeNum = (x.number_of_edges())
#     print()
#     print("Number of nodes = " + str(nodeNum) + " Number of edges = "+ str(edgeNum))
#     cyclomaticNumber = (edgeNum-nodeNum)+1
#     print("Cyclomatic number = " + str(cyclomaticNumber))
#     cyclomaticComplexity = 2*(edgeNum - nodeNum + 2)
#     print("Cyclomatic complexity = " + str(cyclomaticComplexity))
#     if cyclomaticComplexity<20:
#         print ("Process is low complexity")
#     elif cyclomaticComplexity>20 and cyclomaticComplexity<40:
#         print ("Process is medium complexity")
#     elif cyclomaticComplexity>60:
#         print ("Process is high complexity")
#     print()


######################Framework for restrictiveness
    print("--------------------ADJACENCY MATRIX " + str(graphList) +" --------------------")
    graphListEdges = (list(graphList.edges))
    nodeNum = (graphList.number_of_nodes()) 

    arrayAdjacency = [[0 for x in range(nodeNum)] for y in range(nodeNum)]

    print("   0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24")

    xAxis=0

    for x in graphListEdges:
        coord=[]
        for c in x:
            coord.append(c)
        arrayAdjacency [coord[0]][coord[1]] = 1

    for r in arrayAdjacency:
        sys.stdout.write(str(xAxis)+ "  ")
        sys.stdout.flush()
        xAxis=xAxis+1
        for c in r:
            sys.stdout.write(str(c)+ "  ")
            sys.stdout.flush()
        print()
    print()


    #################Reachability##################
    print("--------------------REACHABILITY MATRIX " + str(graphList) +" --------------------")
    arrayReach = [row[:] for row in arrayAdjacency]

    # Prints transitive closure of graph[][] using Floyd Warshall algorithm 
    for k in range(len(arrayReach)): 
            
        # Pick all vertices as source one by one 
        for i in range(len(arrayReach)): 
                
            # Pick all vertices as destination for the 
            # above picked source 
            for j in range(len(arrayReach)): 
                    
                # If vertex k is on a path from i to j,  
                    # then make sure that the value of reach[i][j] is 1 
                arrayReach[i][j] = arrayReach[i][j] or (arrayReach[i][k] and arrayReach[k][j]) 
    
    #Can array reach itself?

    #Printing X and Y axis
    sys.stdout.write("   0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24")
    sys.stdout.flush()
    print()
    xAxis=0 

    for r in arrayReach:
        sys.stdout.write(str(xAxis)+ "  ")
        sys.stdout.flush()
        xAxis=xAxis+1
        for c in r:
            sys.stdout.write(str(c)+ "  ")
            sys.stdout.flush()
        print()

    print(),print()


plt.show()