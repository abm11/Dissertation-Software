import matplotlib.pyplot as plt
import networkx as nx
import sys
from graphviz import render
from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import font
#####################PLAG##############################
try:
    import pygraphviz
    from networkx.drawing.nx_agraph import write_dot
except ImportError:
    try:
        import pydot
        from networkx.drawing.nx_pydot import write_dot
    except ImportError:
        print("Import Fail")
        raise

########################PLAG#############

#Graph Nodes
GENS1 = nx.DiGraph(name="GENS1")
#Graph edges
GENS1.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14),
(2, 19), (19, 20), (20, 14), (2, 16), (16, 17), (17, 18), (18, 14), (9, 21), (21, 14), (11, 23), (23, 14), (12, 22), (22, 14), (1, 15), (15, 14),
(12, 22), (22, 14), (1, 15), (15, 14)])

########################################################################################################################

#Graph Nodes
GENS2 = nx.DiGraph(name="GENS2")
#Graph edges
GENS2.add_edges_from([(0, 1), (0, 7), (1, 2), (2, 3), (3, 4), (4, 6), (4, 5), (5, 16), (6, 8), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 14), (12, 13), (13, 16), (14, 15), (15, 16)])

########################################################################################################################

#Graph Nodes
GENS3 = nx.DiGraph(name="GENS3")
#Graph edges
GENS3.add_edges_from([(0, 1), (0, 18), (1, 2), (2, 3), (3, 4), (4, 6), (4, 5),(5, 19), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (12, 15), (13, 14),  (14, 19), (15, 16), (16,17), (17, 19), (18,7)])

########################################################################################################################

#Graph Nodes
PM1 = nx.DiGraph(name="PM1")
#Graph edges
PM1.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (3, 9), (4, 5), (4, 8), (5, 6), (6, 7), (6, 8), (7, 11), (8, 11), (9, 10), (10, 11)])


PM1.nodes[0]['Activity'] ='Faeces / perianal swabs / artefacts arrive in reception placed in plastic box'
PM1.nodes[1]['Activity'] = 'Box sealed and transported from reception through corridors on A-floor / up internal stairs to Enterics'
PM1.nodes[2]['Activity'] ='MLA staff check specimen details against request and code sample'
PM1.nodes[3]['Activity'] ='Any indication sample High Risk: '
PM1.nodes[4]['Activity'] ='Inpatient'
PM1.nodes[5]['Activity'] ='From SRU ESSU/AMU/B3ED/LJU/CAU NG2/C31/D57 Toghill or Fletcher wards'
PM1.nodes[6]['Activity'] ='Check on NOTIS Is date of admission greater than 3 days'
PM1.nodes[7]['Activity'] ='Code for C diff only +extras (no culture) and follow C diff process'
PM1.nodes[8]['Activity'] ='Follow routine Process'
PM1.nodes[9]['Activity'] ='Transfer to Cat 3 in High risk transport box.'
PM1.nodes[10]['Activity'] ='Process as per methods but within Cat 3 facility – C.diff separate method'
PM1.nodes[11]['Activity'] ='FINISH'

########################################################################################################################

#Graph Nodes
PM2 = nx.DiGraph(name="PM2")
#Graph edges
PM2.add_edges_from([(0, 1), (1, 2), (1, 13), (1, 17), (1, 18), (1, 31), (2, 3), (3, 4), (4, 5), (4, 6), (5, 51), (6, 7), (6, 8), (7, 51), (8, 9), (9, 10), (9, 11), (10,12),
(11, 12), (12, 51), (13, 14), (14, 15), (15, 16), (16, 51), (17, 15), (18, 19), (19, 20), (20, 21), (21, 22), (21, 26), (22, 23), (23, 24), (24, 25), (25, 51),
(26, 27), (27, 28), (27, 29), (28, 51), (29, 30), (30, 51), (31, 32), (32, 33), (33, 34), (34, 35), (35, 36), (36, 37), (37, 38), (38, 39),(39, 40), (39, 41), (40, 51),
(41, 42), (42, 43), (43, 44), (44, 45), (45, 46), (46, 47), (47, 48), (48, 49), (49, 50), (50, 51)])

########################################################################################################################

PM3 = nx.DiGraph(name="PM3")
#Graph edges
PM3.add_edges_from([(0, 1), (0,5), (0,16), (0,20), (0,29), (0,33), (0,42), (0,44), (1,2), (2,3), (3,4), (4,51), (5,6),
                    (6,7), (7,8), (8,9), (9,10), (9,11), (10, 51), (11,12), (11,13), (12,13), (13,14), (13,15), (14,51), (15,51), (16,17),
                    (17,18), (18,19), (19,51), (20,21), (21,22), (22,23), (23,24), (24,25), (25,26), (26,27), (27,28), (27,28), (28,51), (29,30), (30,31),
                    (31,32), (32,51), (33,34), (34,35), (35,36), (36,37), (37,38), (38,39), (38,40), (39,51), (40,41), (41,51), (42,43), (43,51),
                    (44,45), (45,46), (46,47), (47,48), (48,49), (48,50), (49,51), (50,51)])

####################################LIST STUFF#########################################################
#Learn to feed list into function


def graphDrawGen(graph_list):
    for graphList in graph_list:
        for key, value in graphList.graph.items() :
            graphName = value
            print(graphName)
        write_dot(graphList, 'SOP/' + graphName + '.gv')
        render('dot', 'png', 'SOP/' + graphName +'.gv')
        graphListPos = nx.nx_pydot.pydot_layout(graphList, prog='dot')
        nx.draw(graphList, graphListPos, with_labels=True)
        plt.savefig('SOP/' + graphName + '.png', dpi=1000)
        plt.clf()

#########################CYCLOMATIC NUMBER#########################
def cyclomaticNumber(graph):
    nodeNum = (graph.number_of_nodes())
    edgeNum = (graph.number_of_edges())
    cyclomaticNumber = (edgeNum-nodeNum)+1
    return cyclomaticNumber

########################Framework for restrictiveness
########################TRANSITIVE MATRIX PLAG#######################
def restrictiveness(graphList):
    print("--------------------ADJACENCY MATRIX " + str(graphList) +" --------------------")
    graphListEdges = (list(graphList.edges))
    nodeNum = (graphList.number_of_nodes())

    adjacencyArray = [[0 for x in range(nodeNum)] for y in range(nodeNum)]

    print("   0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24")

    xAxis=0

    for x in graphListEdges:
        coord=[]
        for c in x:
            coord.append(c)
        adjacencyArray [coord[0]][coord[1]] = 1

    #Simple output so that we can see the adjacency array in CMD
    for r in adjacencyArray:
        sys.stdout.write(str(xAxis)+ "  ")
        sys.stdout.flush()
        xAxis=xAxis+1
        for c in r:
            print(str(c)+ "  ")
            sys.stdout.write(str(c)+ "  ")
            sys.stdout.flush()
        print()
    print()
#
#
#     #################REACHABILITY MATRIX PLAG ##################
#     print("--------------------REACHABILITY MATRIX " + str(graphList) +" --------------------")
#     arrayReach = [row[:] for row in arrayAdjacency]
#
#     # Prints transitive closure of graph[][] using Floyd Warshall algorithm
#     for k in range(len(arrayReach)):
#
#         # Pick all vertices as source one by one
#         for i in range(len(arrayReach)):
#
#             # Pick all vertices as destination for the
#             # above picked source
#             for j in range(len(arrayReach)):
#
#                 # If vertex k is on a path from i to j,
#                     # then make sure that the value of reach[i][j] is 1
#                 arrayReach[i][j] = arrayReach[i][j] or (arrayReach[i][k] and arrayReach[k][j])
#
#     #Can array reach itself?
#
#     #Printing X and Y axis
#     sys.stdout.write("   0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24")
#     sys.stdout.flush()
#     print()
#     xAxis=0
#
#
#     for r in arrayReach:
#         sys.stdout.write(str(xAxis)+ "  ")
#         sys.stdout.flush()
#         xAxis=xAxis+1
#         for c in r:
#             sys.stdout.write(str(c)+ "  ")
#             sys.stdout.flush()
#         print()p
#
#     print(),print()
#-------------------------------Graph Shit--------------------------------
root = Tk()
root.title('Model Definition')
root.state("zoomed")  #to make it full screen
root.title("Vehicle Window Fitting - Management System")

#Values for obtaining scree size
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%sx%s' % (width, height))

graphFrameWidth = width/2
sideFrameWidth = width/4

# Create the main container (Super container)
descFrame = Frame(root, bg='red',width=sideFrameWidth, height=height)
graphFrame = Frame(root, bg='green',width=graphFrameWidth, height=height)
complexFrame = Frame(root, bg='blue',width=sideFrameWidth, height=height)

descFrame.grid(row=0, column=0)
graphFrame.grid(row=0, column=1)
complexFrame.grid(row=0, column=2)

#///////////// ------- Canvas stuff
c = Canvas(graphFrame, bg='white', width=width/2, height=height)
c.pack()
c.pack(fill=BOTH, expand=1)

#------------Circle builder PLAG------------------
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle
#------------------PLAG-----------------

def UIGraph(graph):
    pydotLayout = (nx.nx_pydot.pydot_layout(graph, prog='dot'))
    maxWidth = 0
    maxHeight = 0
    paddedFrameWidth = graphFrameWidth - (graphFrameWidth / 8)
    paddedHeight = height - (height / 8)
    frameGraphLayout = {}

    for node in pydotLayout:
        x = pydotLayout[node][0]
        if (x > maxWidth):
            maxWidth = x
        y = pydotLayout[node][1]
        if (y > maxHeight):
            maxHeight = y

    for node in pydotLayout:
        x = pydotLayout[node][0]
        xRel = (x) * (paddedFrameWidth / maxWidth)
        y = pydotLayout[node][1]
        yRel = (y) * (paddedHeight / maxHeight)
        yRel = paddedHeight - yRel
        widget = Label(c, text=node, fg='white', bg='red')
        widget.place(x=xRel, y=yRel)
        frameGraphLayout[node]=xRel,yRel

    print(frameGraphLayout)

    edgeList = list(graph.edges)
    for edge in edgeList:
        startNode = edge[0]
        endNode = edge[1]

        startNodeX = frameGraphLayout[startNode][0]
        startNodeY = frameGraphLayout[startNode][1]
        endNodeX = frameGraphLayout[endNode][0]
        endNodeY = frameGraphLayout[endNode][1]
        print ("BEGIN - " + str(startNodeX) + " " + str(startNodeY))
        print ("END - " + str(endNodeX) + " " + str(endNodeY))

        c.create_line(startNodeX, startNodeY, endNodeX, endNodeY, arrow=LAST)


# UI for activities :
def UIActivities(graph):
    listBox = Listbox()
    activityList = graph.nodes
    for activity in activityList:
        sys.stdout.write(str(activity) + " - ")
        sys.stdout.flush()
        print(PM1.nodes[activity]['Activity'])
        listBox.insert(activity, str(activity) + " - " + PM1.nodes[activity]['Activity'])
    listBox.grid(row=0, column=0, sticky="nsew")

def main():
    UIActivities(PM1)
    UIGraph(PM1)
    root.mainloop()

main()


