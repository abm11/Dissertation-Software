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

########################################################################################################################

class DiGraphUI:

    def __init__(self, selectedGraph):
        self.selectedGraph = selectedGraph

    def graphDrawGen(self):
        for key, value in self.graph.items():
            print(key, value)
            graphName = value
            print(graphName)
        write_dot(self, 'SOP/' + graphName + '.gv')
        render('dot', 'png', 'SOP/' + graphName + '.gv')
        graphListPos = nx.nx_pydot.pydot_layout(self, prog='dot')
        nx.draw(self, graphListPos, with_labels=True)
        plt.savefig('SOP/' + graphName + '.png', dpi=1000)
        plt.clf()

    ########################Framework for restrictiveness
    ########################TRANSITIVE MATRIX PLAG#######################


    def UIGraph(self):
        root = Tk()
        root.title('Model Definition')
        root.state("zoomed")  # to make it full screen
        root.title("Vehicle Window Fitting - Management System")

        # Values for obtaining scree size
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry('%sx%s' % (width, height))

        #Base values to ensure relative positioning within interface
        graphFrameWidth = width / 2
        sideFrameWidth = width / 4

        # Create the main container (Super container)
        descFrame = Frame(root, bg='red', width=sideFrameWidth, height=height)
        graphFrame = Frame(root, bg='green', width=graphFrameWidth, height=height)
        complexFrame = Frame(root, bg='blue', width=sideFrameWidth, height=height)

        descFrame.grid(row=0, column=0)
        graphFrame.grid(row=0, column=1)
        complexFrame.grid(row=0, column=2)

        # ///////////// ------- Canvas stuff
        graphCanvas = Canvas(graphFrame, bg='white', width=width / 2, height=height)
        graphCanvas.pack()
        graphCanvas.pack(fill=BOTH, expand=1)

        ####################################################

        pydotLayout = (nx.nx_pydot.pydot_layout(self, prog='dot'))
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
            widget = Label(graphCanvas, text=node, fg='white', bg='red')
            widget.place(x=xRel, y=yRel)
            frameGraphLayout[node]=xRel,yRel


        edgeList = list(self.edges)
        for edge in edgeList:
            startNode = edge[0]
            endNode = edge[1]

            startNodeX = frameGraphLayout[startNode][0]
            startNodeY = frameGraphLayout[startNode][1]
            endNodeX = frameGraphLayout[endNode][0]
            endNodeY = frameGraphLayout[endNode][1]
            # print ("BEGIN - " + str(startNodeX) + " " + str(startNodeY))
            # print ("END - " + str(endNodeX) + " " + str(endNodeY))

            graphCanvas.create_line(startNodeX, startNodeY, endNodeX, endNodeY, arrow=LAST)

        UIActivities(self)

        #Complexity UI
        complexityHeader = Label(complexFrame, text = "Complexity measures", font=("TkDefaultFont", 25))
        complexityHeader.place(x=sideFrameWidth/2, y=height/20, anchor="center")

        cyclomaticNumberVal = cyclomaticNumber(self)
        cyclomaticLabel = Label(complexFrame, text = ("Cyclomatic complexity \n" + str(cyclomaticNumberVal)),
                                font=("TkDefaultFont", 20))
        cyclomaticLabel.place(x=sideFrameWidth/2, y=height/8, anchor="center")

        restrictivenessVal = restrictiveness(self)
        restrictivenessLabel = Label(complexFrame, text=("Cyclomatic complexity \n" + str(restrictivenessVal)),
                                font=("TkDefaultFont", 20))
        restrictivenessLabel.place(x=sideFrameWidth / 2, y=2*(height/8), anchor="center")

        root.mainloop()

#To work with class, must be outside of class?
#ASK JAMIE
    # UI for activities :
def UIActivities(self):
    listBox = Listbox()
    activityList = self.nodes
    for activity in activityList:
        sys.stdout.write(str(activity) + " - ")
        sys.stdout.flush()
        print(self.nodes[activity]['Activity'])
        listBox.insert(activity, str(activity) + " - " + self.nodes[activity]['Activity'])
    listBox.grid(row=0, column=0, sticky="nsew")

def cyclomaticNumber(self):
    nodeNum = (self.number_of_nodes())
    edgeNum = (self.number_of_edges())
    cyclomaticNumber = (edgeNum-nodeNum)+1
    return(cyclomaticNumber)

def restrictiveness(self):

    #Obtain list of edges
    graphListEdges = (list(self.edges))
    #Obtain number of nodes
    nodeNum = (self.number_of_nodes())
    #Build 2D array of size nodenum- Iterate through all values, setting them to 0 (no adjacency)
    adjacencyArray = [[0 for x in range(nodeNum)] for y in range(nodeNum)]
    #Iterate through list of edges
    for eachEdge in graphListEdges:
        # Init coordinate list
        coord=[]
        # Iterate through node pairs that compose edges
        for eachNode in eachEdge:
            #Append node to list
            coord.append(eachNode)
        #Call coordinate variables from cordinate list, then set each subsequent adjacency array value to 1 for each coordiante value pair
        adjacencyArray [coord[0]][coord[1]] = 1

    #Simple output so that we can see the adjacency array in CMD
    print("--------------------ADJACENCY MATRIX " + str(self) +" --------------------")
    xAxis = 0
    sys.stdout.write("   ")
    sys.stdout.flush()
    for eachColumm in range(nodeNum):
        sys.stdout.write(str(eachColumm) + "  ")
        sys.stdout.flush()
    print()
    for eachRow in adjacencyArray:
        sys.stdout.write(str(xAxis) + "  ")
        xAxis+=1
        for eachValue in eachRow:
            sys.stdout.write(str(eachValue)+ "  ")
            sys.stdout.flush()
        print()

    ################REACHABILITY MATRIX PLAG ##################
    # Init the reachability matrix, using the adjacency array
    reachabilityArray = [value[:] for value in adjacencyArray]
    # Select all nodes from the array
    for all in range(len(reachabilityArray)):
        # Select all nodes as the start of the path
        for start in range(len(reachabilityArray)):
            # Select all nodes as the end of the path
            for end in range(len(reachabilityArray)):
                # If we are on the shortest path available from start node to end node, then update the reachability array (with 1)
                reachabilityArray[start][end] = reachabilityArray[start][end] or (reachabilityArray[start][all] and reachabilityArray[all][end])

    # Simple output so that we can see the reachability array in CMD
    print("--------------------ADJACENCY MATRIX " + str(self) +" --------------------")
    xAxis = 0
    sys.stdout.write("   ")
    sys.stdout.flush()
    for eachColumm in range(nodeNum):
        sys.stdout.write(str(eachColumm) + "  ")
        sys.stdout.flush()
    print()
    for eachRow in reachabilityArray:
        sys.stdout.write(str(xAxis) + "  ")
        xAxis+=1
        for eachValue in eachRow:
            sys.stdout.write(str(eachValue)+ "  ")
            sys.stdout.flush()
        print()

    #Restrictivness Estimator
    print(reachabilityArray[0])
    #Convert reachabilityArray into 1D array/single list
    reachabilityList = []
    for eachRow in reachabilityArray:
        xAxis+=1
        for eachValue in eachRow:
            reachabilityList.append(eachValue)

    # restrictivenessEstimator = ((2*(sum(reachabilityList)))-(6(nodeNum-1)))/((nodeNum-2)(nodeNum-3)))
    restrictivenessEstimator = (((2*(sum(reachabilityList)))-6*(nodeNum-1))/(nodeNum-2)*(nodeNum-3))
    return restrictivenessEstimator

def main():

    print(type(PM1))
    DiGraphUI.graphDrawGen(GENS3)
    # DiGraphUI.cyclomaticNumber(PM1)
    # DiGraphUI.restrictiveness(PM1)
    # DiGraphUI.UIGraph(PM1)
    # DiGraphUI.Activities(PM1)

if __name__ == "__main__":
    main()

