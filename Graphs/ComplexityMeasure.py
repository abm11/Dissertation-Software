import matplotlib.pyplot as plt
import networkx as nx
from graphviz import render
from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import filedialog
import copy
import numpy as np
from tkinter.filedialog import askopenfilename
from tkinter import Tk
from win32api import GetMonitorInfo, MonitorFromPoint


class DiGraphUI:

    def __init__(self, selectedGraph):
        self.selectedGraph = selectedGraph

    def UIGraph(self):
        global root
        root = Tk()
        root.title('Graph Complexity - Visualiser and Calculator')
        root.state("zoomed")  # to make it full screen

        # Values for obtaining scree size
        monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
        work_area = monitor_info.get("Work")
        width = root.winfo_screenwidth()
        # Returns hiegh of window minus task bar and title bar
        height = work_area[3]-50
        # root.geometry('%sx%s' % (width, height))

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
        main_menu.add_cascade(label="Graph", menu=open_menu)
        #Lambda functions stops recursive exe of methods
        open_menu.add_command(label="Open", command=lambda : DiGraphUI.openGraph(self))
        # Display the menu bar
        root.config(menu=main_menu)

        # Graph UI
        # Sizes relative ot the display resolutiona re used to ensure UI deign works across multiple display resolutions
        pydotLayout = (nx.nx_pydot.pydot_layout(self, prog='dot'))
        maxWidth = 0
        maxHeight = 0

        paddedFrameWidth = graphFrameWidth - (graphFrameWidth / 8)
        paddedHeight = height - (height / 25)
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
        listBox = Listbox(root)
        activityList = self.nodes
        for node in pydotLayout:
            x = pydotLayout[node][0]
            xRel = (x) * (paddedFrameWidth / maxWidth)
            y = pydotLayout[node][1]
            yRel = ((y) * (paddedHeight / maxHeight)) - (maxHeight / 200)
            yRel = paddedHeight - yRel
            widget = Label(graphCanvas, text=node, fg='white', bg='red')
            widget.place(x=xRel, y=yRel)
            frameGraphLayout[node]=xRel,yRel
            ToolTipGen(widget, str(self.nodes[node]['Activity']))
            print (str(self.nodes[node]['Activity']))

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

        #Complexity UI
        graphName = Label(complexFrame, text = str(self), font=("TkDefaultFont", 25), bg='white')
        graphName.place(x=sideFrameWidth / 2, y=(height / 16), anchor="center")

        complexityHeader = Label(complexFrame, text = "Complexity measures", font=("TkDefaultFont", 25), bg='white')
        complexityHeader.place(x=sideFrameWidth / 2, y=2*(height / 16), anchor="center")

        cyclomaticNumberVal = DiGraphUI.cyclomaticNumber(self)
        cyclomaticLabel = Label(complexFrame, text = ("Cyclomatic complexity \n" + str(cyclomaticNumberVal)), bg='white',
                                font=("TkDefaultFont", 20))
        cyclomaticLabel.place(x=sideFrameWidth / 2, y=3*(height/8), anchor="center")
        ToolTipGen(cyclomaticLabel, \
                                    'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, '
                                    'consectetur, adipisci velit. Neque porro quisquam est qui dolorem ipsum '
                                    'quia dolor sit amet, consectetur, adipisci velit. Neque porro quisquam '
                                    'est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit.')

        restrictivenessVal = DiGraphUI.restrictiveness(self)
        restrictivenessLabel = Label(complexFrame, text=("Restrictiveness estimator\n" + str(restrictivenessVal)), bg='white',
                                font=("TkDefaultFont", 20))
        restrictivenessLabel.place(x=sideFrameWidth / 2, y=5 * (height / 8), anchor="center")

        numberofTreesVal = DiGraphUI.numberOfTrees(self)
        numberofTreesLabel = Label(complexFrame, text=("Number of trees\n" + str(numberofTreesVal)),
                                     bg='white',
                                     font=("TkDefaultFont", 20))
        numberofTreesLabel.place(x=sideFrameWidth / 2, y=7 * (height / 8), anchor="center")

        listBox = Listbox(root)
        activityList = self.nodes
        for activity in activityList:
            sys.stdout.write(str(activity) + " - ")
            sys.stdout.flush()
            listBox.insert(activity, str(activity) + " - " + self.nodes[activity]['Activity'])
        listBox.grid(row=0, column=0, sticky="nsew")
        # Declare as lambda to stop unintended execution
        root.protocol('WM_DELETE_WINDOW', lambda:sys.exit())
        root.mainloop()

    def graphDrawGen(self):
        for key, value in self.graph.items():
            graphName = value
        # Remove gv?
        # write_dot(self, 'Image-Graphs/' + graphName + '.gv') DROP ????
        render('dot', 'png', 'Image-Graphs/' + graphName + '.gv')
        graphListPos = nx.nx_pydot.pydot_layout(self, prog='dot')
        edge_labels = nx.get_edge_attributes(self, 'choice')
        nx.draw_networkx_edge_labels(self, graphListPos, edge_labels=edge_labels, font_size=4)
        nx.draw(self, graphListPos, with_labels=True, node_size=150, font_size=8)
        plt.savefig('SOP/' + graphName + '.png', dpi=1000, bbox_inches='tight', pad_inches=0, transparent=True)
        plt.clf()

    def cyclomaticNumber(self):
        nodeNum = (self.number_of_nodes())
        edgeNum = (self.number_of_edges())
        cyclomaticNumber = (edgeNum - nodeNum) + 1
        return (cyclomaticNumber)

    def restrictiveness(self):
        # Global access for number of trees calculation method
        global adjacencyArray
        # Obtain list of edges
        graphListEdges = (list(self.edges))
        # Obtain number of nodes
        nodeNum = (self.number_of_nodes())
        # Build 2D array of size nodenum- Iterate through all values, setting them to 0 (no adjacency)
        adjacencyArray = [[0 for x in range(nodeNum)] for y in range(nodeNum)]
        # Iterate through list of edges
        for eachEdge in graphListEdges:
            # Init coordinate list
            coord = []
            # Iterate through node pairs that compose edges
            for eachNode in eachEdge:
                # Append node to list
                coord.append(eachNode)
            # Call coordinate variables from cordinate list, then set each subsequent adjacency array value to 1 for each coordiante value pair
            adjacencyArray[coord[0]][coord[1]] = 1

        # Simple output so that we can see the adjacency array in CMD
        print("--------------------ADJACENCY MATRIX " + str(self) + " --------------------")
        xAxis = 0
        sys.stdout.write("\t")
        sys.stdout.flush()
        for eachColumm in range(nodeNum):
            sys.stdout.write(str(eachColumm) + "\t")
            sys.stdout.flush()
        print()
        for eachRow in adjacencyArray:
            sys.stdout.write(str(xAxis) + "\t")
            xAxis += 1
            for eachValue in eachRow:
                sys.stdout.write(str(eachValue) + "\t")
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
                    reachabilityArray[start][end] = reachabilityArray[start][end] or (
                                reachabilityArray[start][all] and reachabilityArray[all][end])

        # Matrix is defined as the Reflexive transitive closure of the reachability matrix
        # Therefore a node can reach itself
        # Set diagonal elements to 1
        for i in range(len(reachabilityArray)):
            reachabilityArray[i][i] = 1

        # Simple output so that we can see the reachability array in CMD
        print("--------------------REACHABILITY MATRIX " + str(self) + " --------------------")
        xAxis = 0
        sys.stdout.write("\t")
        sys.stdout.flush()
        for eachColumm in range(nodeNum):
            sys.stdout.write(str(eachColumm) + "\t")
            sys.stdout.flush()
        print()
        for eachRow in reachabilityArray:
            sys.stdout.write(str(xAxis) + "\t")
            xAxis += 1
            for eachValue in eachRow:
                sys.stdout.write(str(eachValue) + "\t")
                sys.stdout.flush()
            print()

        # Restrictivness Estimator
        # Convert reachabilityArray into 1D array/single list
        reachabilityList = []
        for eachRow in reachabilityArray:
            xAxis += 1
            for eachValue in eachRow:
                reachabilityList.append(eachValue)

        restrictivenessEstimator = (
                    ((2 * (sum(reachabilityList))) - 6 * (nodeNum - 1)) / ((nodeNum - 2) * (nodeNum - 3)))
        # Round to 3 decimal place
        restrictivenessEstimator = round(restrictivenessEstimator, 3)
        return restrictivenessEstimator

    def numberOfTrees(self):
        # Copy adjacency array
        diagArray = copy.deepcopy(adjacencyArray)

        # Diagonal elements = Sum of row
        for i in range(len(diagArray)):
            diagArray[i][i] = sum(diagArray[i])

        # Set negative values
        dArray = copy.deepcopy(adjacencyArray)
        for i in range(len(dArray)):
            for j in range(len(dArray[i])):
                dArray[i][j] = -(dArray[i][j])

        # Merge values into single matrix
        for i in range(len(dArray)):
            dArray[i][i] = copy.deepcopy(diagArray[i][i])

        # Networkx has no function to calculate sink node
        # However the sink node will have an adjacency of 0
        # We can use this to determine the sink node
        for i in range(len(adjacencyArray)):
            if (sum(diagArray[i])) == 0:
                sinkNode = i

        # Convert array to numpy to carry out minor and determinant
        numpyArray = np.array(dArray)
        for i in range(len(diagArray)):
            diagArray[i][i] = sum(diagArray[i])

        # Calculate minor of sink node (delete row and column), creates minor matrix
        numpyArray = np.delete(numpyArray, (sinkNode), axis=0)
        numpyArray = np.delete(numpyArray, (sinkNode), axis=1)
        # Number of trees = determinant of minor matrix
        treeNumber = int(round((np.linalg.det(numpyArray)), 0))
        return treeNumber

        # Simple output so that we can see the reachability array in CMD
        print("--------------------D MATRIX" + str(self) + " --------------------")
        xAxis = 0
        sys.stdout.write("\t")
        sys.stdout.flush()
        for eachColumm in range(nodeNum):
            sys.stdout.write(str(eachColumm) + "\t")
            sys.stdout.flush()
        print()
        for eachRow in numpyArray:
            sys.stdout.write(str(xAxis) + "\t")
            xAxis += 1
            for eachValue in eachRow:
                sys.stdout.write(str(eachValue) + "\t")
                sys.stdout.flush()
            print()

    def YAMLGenerator(graph):
        nx.write_yaml(graph, "YAML-graphs/"+str(graph)+".YAML")

    def YAMLReader(filename):
        YAMLGraph = nx.read_yaml(filename)
        return YAMLGraph

    def openGraph(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("YAML files", "yaml"),))
        if filename == '':
            return
        root.destroy()
        DiGraphUI.UIGraph(DiGraphUI.YAMLReader(filename))

    ###################PLAG#####################
class ToolTipGen(object):
    def __init__(self, widget, text='widget info'):
        self.waittime = 0  # miliseconds
        self.wraplength = 200  # pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hideTip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showTip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showTip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() +25
        y += self.widget.winfo_rooty() +20
        # creates a top level window
        self.tw = Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify='left',
                         background="#ffffff", relief='solid', borderwidth=1,
                         wraplength=self.wraplength)
        label.pack(ipadx=1)

    def hideTip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()
#####################################

def main():

    Tk().withdraw()
    global filename
    filename = askopenfilename()
    DiGraphUI.UIGraph(DiGraphUI.YAMLReader(filename))

if __name__ == "__main__":
    main()

#SHARE VARIABLES BETWEEN METHODS - Global?
#COUNT FROM 0 OR 1? - 1
#CHECK ?s
#Var/meth naming conventions?