import matplotlib.pyplot as plt
import networkx as nx
from graphviz import render
from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH
import copy
import numpy as np

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
graph1 = nx.DiGraph(name="Graph 1")
#Graph edges
graph1.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 21), (0, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 21),
                      (0, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18,19), (19, 20), (20, 21)])

graph1.nodes[0]['Activity'] = 'DUMMY'
graph1.nodes[1]['Activity'] = 'DUMMY'
graph1.nodes[2]['Activity'] = 'DUMMY'
graph1.nodes[3]['Activity'] = 'DUMMY'
graph1.nodes[4]['Activity'] = 'DUMMY'
graph1.nodes[5]['Activity'] = 'DUMMY'
graph1.nodes[6]['Activity'] = 'DUMMY'
graph1.nodes[7]['Activity'] = 'DUMMY'
graph1.nodes[8]['Activity'] = 'DUMMY'
graph1.nodes[9]['Activity'] = 'DUMMY'
graph1.nodes[10]['Activity'] = 'DUMMY'
graph1.nodes[11]['Activity'] = 'DUMMY'
graph1.nodes[12]['Activity'] = 'DUMMY'
graph1.nodes[13]['Activity'] = 'DUMMY'
graph1.nodes[14]['Activity'] = 'DUMMY'
graph1.nodes[15]['Activity'] = 'DUMMY'
graph1.nodes[16]['Activity'] = 'DUMMY'
graph1.nodes[17]['Activity'] = 'DUMMY'
graph1.nodes[18]['Activity'] = 'DUMMY'
graph1.nodes[19]['Activity'] = 'DUMMY'
graph1.nodes[20]['Activity'] = 'DUMMY'
graph1.nodes[21]['Activity'] = 'DUMMY'

# nx.write_gexf(graph1, "test.gexf")
#
# graph123 = nx.DiGraph(nx.read_gexf("test.gexf"))
# print("NO - " + str(graph123))
# graph1 =  nx.DiGraph(nx.read_gexf("test.gexf"))

graph2 = nx.DiGraph(name="Graph 1")
#Graph edges
graph2.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 21), (0, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 21),
                      (0, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18,19), (19, 20), (20, 21), (2, 9), (4, 11), (12, 7), (15, 9), (17, 11)])

graph2.nodes[0]['Activity'] = 'Check sample not leaked – unbag and label sample & consumables then transfer into the safety cabinet. If leaking transfer to safety cabinet before un-bagging.'
graph2.nodes[1]['Activity'] = 'DUMMY'
graph2.nodes[2]['Activity'] = 'DUMMY'
graph2.nodes[3]['Activity'] = 'DUMMY'
graph2.nodes[4]['Activity'] = 'DUMMY'
graph2.nodes[5]['Activity'] = 'DUMMY'
graph2.nodes[6]['Activity'] = 'DUMMY'
graph2.nodes[7]['Activity'] = 'DUMMY'
graph2.nodes[8]['Activity'] = 'DUMMY'
graph2.nodes[9]['Activity'] = 'DUMMY'
graph2.nodes[10]['Activity'] = 'DUMMY'
graph2.nodes[11]['Activity'] = 'DUMMY'
graph2.nodes[12]['Activity'] = 'DUMMY'
graph2.nodes[13]['Activity'] = 'DUMMY'
graph2.nodes[14]['Activity'] = 'DUMMY'
graph2.nodes[15]['Activity'] = 'DUMMY'
graph2.nodes[16]['Activity'] = 'DUMMY'
graph2.nodes[17]['Activity'] = 'DUMMY'
graph2.nodes[18]['Activity'] = 'DUMMY'
graph2.nodes[19]['Activity'] = 'DUMMY'
graph2.nodes[20]['Activity'] = 'DUMMY'
graph2.nodes[21]['Activity'] = 'DUMMY'

#####################################################

#Graph Nodes
GENS1 = nx.DiGraph(name="GENS1")
#Graph edges
GENS1.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14),
(2, 19), (19, 20), (20, 14), (2, 16), (16, 17), (17, 18), (18, 14), (9, 21), (21, 14), (11, 23), (23, 14), (12, 22), (22, 14), (1, 15), (15, 14),
(12, 22), (22, 14), (1, 15), (15, 14)])

#Set edge labels
attrs = {(2, 19): {'choice': 'Yes'}, (2, 16): {'choice': 'Yes'}, (2, 3): {'choice': 'No'}, (2, 16): {'choice': 'Yes'},
         (11, 12): {'choice': 'Yes'}, (11, 23): {'choice': 'No'}}
nx.set_edge_attributes(GENS1, attrs)

#Node activity's
GENS1.nodes[0]['Activity'] = 'Faeces samples processed as per PR2062 and associated process map as standard of care.'
GENS1.nodes[1]['Activity'] = 'Sample worklist prepared by either:•	WinPath worklists searched for known positive samples•	Selection of samples with suggestive clinical details•	NEQAS•	Spiking known culture negative stools with bacterial targets'
GENS1.nodes[2]['Activity'] = 'Any indication sample High Risk?'
GENS1.nodes[3]['Activity'] = 'Samples located in B floor walk in fridge'
GENS1.nodes[4]['Activity'] = 'Class 1 safety cabinet is cleaned with Trigene followed by DNAzap'
GENS1.nodes[5]['Activity'] = '1mL STAR buffer to a sterile molecular grade microcentrifuge tube.  Add 100uL liquid stool or rice sized portion if solid.  Vortex for 1 min'
GENS1.nodes[6]['Activity'] = 'Incubate for 15 min at RT, vortex after ~7 min and at 15 min.'
GENS1.nodes[7]['Activity'] = 'Centrifuge for 2 min at 6500rpm.'
GENS1.nodes[8]['Activity'] = 'Allow to stand at RT for 5 min'
GENS1.nodes[9]['Activity'] = 'Transfer 500uL of supernatant into a new a sterile molecular grade microcentrifuge tube.'
GENS1.nodes[10]['Activity'] = 'Store remaining buffer/stool mixtures in a rack inside a sealed container until PCR proves no CL3 pathogen present.'
GENS1.nodes[11]['Activity'] = 'PCR shows sample contains CL3 pathogen?'
GENS1.nodes[12]['Activity'] = 'Transfer sealed box into CL3 and dispose of samples in sharps bin.'
GENS1.nodes[13]['Activity'] = 'Disinfect transport box and rack with 10% distil before removal back into CL2'
GENS1.nodes[14]['Activity'] = 'FINISHED'
GENS1.nodes[15]['Activity'] = 'For spiked stools include on current worklist – follow ENS2 process map.'
##############################FINISH 16 LATER
GENS1.nodes[16]['Activity'] = '1.	Cysticercosis'
GENS1.nodes[17]['Activity'] = 'Samples located in CL3'
GENS1.nodes[18]['Activity'] = 'Process as per methods but within Cat 3 facility – follow ENS3 process map.'
##############################FINISH 19 LATER
GENS1.nodes[19]['Activity'] = '1.	Hydatid '
GENS1.nodes[20]['Activity'] = 'Do not include in this pathway'
GENS1.nodes[21]['Activity'] = 'Supernatants ready for use on the EasyMag'
GENS1.nodes[22]['Activity'] = 'Dispose using CL3 route'
GENS1.nodes[23]['Activity'] = 'Dispose using CL2 route'



# #PLAG#######################
# json.dump(dict(nodes=[[n, GENS1.node[n]] for n in GENS1.nodes()],
#                edges=[[u, v, GENS1.get_edge_data[u][v]] for u,v in GENS1.edges()]),
#           open('asdf', 'w'), indent=2)
#
# GENS1 = nx.DiGraph()
# d = json.load(open('asdf'))
# GENS1.add_nodes_from(d['nodes'])
# GENS1.add_edges_from(d['edges'])
# ############PLAG#########################
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

#Node activity's
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
            graphName = value
        write_dot(self, 'SOP/' + graphName + '.gv')
        render('dot', 'png', 'SOP/' + graphName + '.gv')
        graphListPos = nx.nx_pydot.pydot_layout(self, prog='dot')
        edge_labels = nx.get_edge_attributes(self, 'choice')
        nx.draw_networkx_edge_labels(self, graphListPos, edge_labels=edge_labels, font_size=4)
        nx.draw(self, graphListPos, with_labels=True, node_size=150, font_size=8)
        plt.savefig('SOP/' + graphName + '.png', dpi=1000, bbox_inches='tight', pad_inches = 0, transparent = True)
        plt.clf()

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
        descFrame = Frame(root, width=sideFrameWidth, height=height)
        graphFrame = Frame(root, width=graphFrameWidth, height=height)
        complexFrame = Frame(root, bg = 'white', width=sideFrameWidth, height=height)

        descFrame.grid(row=0, column=0)
        graphFrame.grid(row=0, column=1)
        complexFrame.grid(row=0, column=2)

        # ///////////// ------- Canvas stuff
        graphCanvas = Canvas(graphFrame, bg='white', width=width / 2, height=height)
        graphCanvas.pack()
        graphCanvas.pack(fill=BOTH, expand=1)

        #Menu UI#####################################
        # Create the main menu object
        main_menu = Menu(root)
        # ----- VIEW MENU -----
        open_menu = Menu(main_menu, tearoff=0)

        # Add the pull down menu to the menu bar
        main_menu.add_cascade(label="Open", menu=open_menu)

        # Display the menu bar
        root.config(menu=main_menu)

        #Graph UI#########################################################
        pydotLayout = (nx.nx_pydot.pydot_layout(self, prog='dot'))
        maxWidth = 0
        maxHeight = 0
        paddedFrameWidth = graphFrameWidth - (graphFrameWidth / 8)
        paddedHeight = height - (height / 8)
        frameGraphLayout = {}

        #Calculate dimensions of DiGraph
        for node in pydotLayout:
            x = pydotLayout[node][0]
            if (x > maxWidth):
                maxWidth = x
            y = pydotLayout[node][1]
            if (y > maxHeight):
                maxHeight = y

        # Insert nodes as labels
        for node in pydotLayout:
            x = pydotLayout[node][0]
            xRel = (x) * (paddedFrameWidth / maxWidth)
            y = pydotLayout[node][1]
            yRel = (y) * (paddedHeight / maxHeight)
            yRel = paddedHeight - yRel
            widget = Label(graphCanvas, text=node, fg='white', bg='red')
            widget.place(x=xRel, y=yRel)
            frameGraphLayout[node]=xRel,yRel

        #
        edge_labels = nx.get_edge_attributes(self, 'choice')
        for node, yesNo in edge_labels.items():
            startLabelNode = node[0]
            endLabelNode = node[1]

            startLabelNodeX = frameGraphLayout[startLabelNode][0]
            startLabelNodeY = frameGraphLayout[startLabelNode][1]
            endLabelNodeX = frameGraphLayout[endLabelNode][0]
            endLabelNodeY = frameGraphLayout[endLabelNode][1]

            avgLabelNodeX = (startLabelNodeX+endLabelNodeX)/2
            avgLabelNodeY = (startLabelNodeY+endLabelNodeY)/2

            edgeLabel = Label(graphCanvas, text=yesNo, fg='black', bg='white')
            edgeLabel.place(x=avgLabelNodeX, y=avgLabelNodeY)

        #Insert edges as arrows
        edgeList = list(self.edges)
        #Iterate through edge list
        for edge in edgeList:
            startNode = edge[0]
            endNode = edge[1]
            #Set edge nodes coordinates
            startNodeX = frameGraphLayout[startNode][0]
            startNodeY = frameGraphLayout[startNode][1]
            endNodeX = frameGraphLayout[endNode][0]
            endNodeY = frameGraphLayout[endNode][1]
            #Draw edge/arrow
            graphCanvas.create_line(startNodeX, startNodeY, endNodeX, endNodeY, arrow=LAST)



        #Acivity UI
        UIActivities(self)

        #Complexity UI
        complexityHeader = Label(complexFrame, text = "Complexity measures", font=("TkDefaultFont", 25), bg='white')
        complexityHeader.place(x=sideFrameWidth/2, y=(height/16), anchor="center")

        cyclomaticNumberVal = cyclomaticNumber(self)
        cyclomaticLabel = Label(complexFrame, text = ("Cyclomatic complexity \n" + str(cyclomaticNumberVal)), bg='white',
                                font=("TkDefaultFont", 20))
        cyclomaticLabel.place(x=sideFrameWidth / 2, y=2*(height/8), anchor="center")

        restrictivenessVal = restrictiveness(self)
        restrictivenessLabel = Label(complexFrame, text=("Restrictiveness estimator\n" + str(restrictivenessVal)), bg='white',
                                font=("TkDefaultFont", 20))
        restrictivenessLabel.place(x=sideFrameWidth / 2, y=4 * (height / 8), anchor="center")

        numberofTreesVal = numberOfTrees(self)
        numberofTreesLabel = Label(complexFrame, text=("Number of trees\n" + str(numberofTreesVal)),
                                     bg='white',
                                     font=("TkDefaultFont", 20))
        numberofTreesLabel.place(x=sideFrameWidth / 2, y=6 * (height / 8), anchor="center")
        root.mainloop()

def UIActivities(self):
    listBox = Listbox()
    activityList = self.nodes
    for activity in activityList:
        sys.stdout.write(str(activity) + " - ")
        sys.stdout.flush()
        listBox.insert(activity, str(activity) + " - " + self.nodes[activity]['Activity'])
    listBox.grid(row=0, column=0, sticky="nsew")

def cyclomaticNumber(self):
    nodeNum = (self.number_of_nodes())
    edgeNum = (self.number_of_edges())
    cyclomaticNumber = (edgeNum-nodeNum)+1
    return(cyclomaticNumber)

def restrictiveness(self):
    # Global access for number of trees calculation method
    global adjacencyArray
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
    sys.stdout.write("\t")
    sys.stdout.flush()
    for eachColumm in range(nodeNum):
        sys.stdout.write(str(eachColumm) + "\t")
        sys.stdout.flush()
    print()
    for eachRow in adjacencyArray:
        sys.stdout.write(str(xAxis) + "\t")
        xAxis+=1
        for eachValue in eachRow:
            sys.stdout.write(str(eachValue)+ "\t")
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

    #Matrix is defined as the Reflexive transitive closure of the reachability matrix
    #Therefore a node can reach itself
    #Set diagonal elements to 1
    for i in range(len(reachabilityArray)):
        reachabilityArray[i][i] = 1

    # Simple output so that we can see the reachability array in CMD
    print("--------------------REACHABILITY MATRIX " + str(self) +" --------------------")
    xAxis = 0
    sys.stdout.write("\t")
    sys.stdout.flush()
    for eachColumm in range(nodeNum):
        sys.stdout.write(str(eachColumm) + "\t")
        sys.stdout.flush()
    print()
    for eachRow in reachabilityArray:
        sys.stdout.write(str(xAxis) + "\t")
        xAxis+=1
        for eachValue in eachRow:
            sys.stdout.write(str(eachValue)+ "\t")
            sys.stdout.flush()
        print()

    #Restrictivness Estimator
    #Convert reachabilityArray into 1D array/single list
    reachabilityList = []
    for eachRow in reachabilityArray:
        xAxis+=1
        for eachValue in eachRow:
            reachabilityList.append(eachValue)

    restrictivenessEstimator = (((2*(sum(reachabilityList)))-6*(nodeNum-1))/((nodeNum-2)*(nodeNum-3)))
    #Round to 3 decimal place - Update to sig fig?????
    restrictivenessEstimator = round(restrictivenessEstimator, 3)
    return restrictivenessEstimator

def numberOfTrees(self):
    #Matrix for diagonal array?
    diagArray = copy.deepcopy(adjacencyArray)

    #Diagonal elements = Sum of row
    for i in range(len(diagArray)):
        diagArray[i][i] = sum(diagArray[i])

    #Set negative values
    dArray = copy.deepcopy(adjacencyArray)
    for i in range(len(dArray)):
        for j in range(len(dArray[i])):
            dArray[i][j] = -(dArray[i][j])

    #Merge values into single matrix
    for i in range(len(dArray)):
        dArray[i][i] = copy.deepcopy(diagArray[i][i])

    numpyArray = np.array(dArray)
    for i in range(len(diagArray)):
        diagArray[i][i] = sum(diagArray[i])

    #Networkx has no function to calculate sink node
    #However the sink node will have an adjacency of 0
    #We can use this to determine the sink node
    for i in range(len(adjacencyArray)):
        if (sum(diagArray[i])) == 0:
            sinkNode=i

    #Calculate minor of sink node (delete row and column), creates minor matrix
    numpyArray = np.delete(numpyArray, (sinkNode), axis=0)
    numpyArray = np.delete(numpyArray, (sinkNode), axis=1)
    #Number of trees = determinant of minor matrix
    treeNumber = int(round((np.linalg.det(numpyArray)), 0))
    return treeNumber

# Simple output so that we can see the reachability array in CMD
    print("--------------------D MATRIX" + str(self) +" --------------------")
    xAxis = 0
    sys.stdout.write("\t")
    sys.stdout.flush()
    for eachColumm in range(nodeNum):
        sys.stdout.write(str(eachColumm) + "\t")
        sys.stdout.flush()
    print()
    for eachRow in numpyArray:
        sys.stdout.write(str(xAxis) + "\t")
        xAxis+=1
        for eachValue in eachRow:
            sys.stdout.write(str(eachValue)+ "\t")
            sys.stdout.flush()
        print()

##############################PLAG################################################

def main():
    # DiGraphUI.graphDrawGen(GENS3)
    # DiGraphUI.cyclomaticNumber(PM1)
    # DiGraphUI.restrictiveness(PM1)
    DiGraphUI.UIGraph(GENS1)
    # DiGraphUI.Activities(PM1)
    DiGraphUI.graphDrawGen(GENS1)

if __name__ == "__main__":
    main()

#SORT OUT CLASSES AND STUFF
#SHARE VARIABLES BETWEEN METHODS - Global?
#COUNT FROM 0 OR 1?
#CHECK ?s