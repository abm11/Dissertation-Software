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

    def __init__(self, selected_graph):
        # Assign selected graph to self
        self.selected_graph = selected_graph

    def ui_graph(self):
        ################################################################################################################
        #                                       Build UI
        # Initialize UI
        global root
        root = Tk()
        root.title('Graph Complexity - Visualiser and Calculator')
        root.state("zoomed")  # to make it full screen

        # Obtain screen size
        monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
        work_area = monitor_info.get("Work")
        width = root.winfo_screenwidth()

        # Returns height of window minus task bar and title bar
        height = work_area[3]-50

        # Base values to ensure relative positioning within interface
        graph_frame_width = width / 2
        side_frame_width = width / 4

        # Create the main container (Super container)
        desc_frame = Frame(root, width=side_frame_width, height=height)
        graph_frame = Frame(root, width=graph_frame_width, height=height)
        complex_frame = Frame(root, bg='white', width=side_frame_width, height=height)

        # Arrange frames
        desc_frame.grid(row=0, column=0)
        graph_frame.grid(row=0, column=1)
        complex_frame.grid(row=0, column=2)

        # Build canvas - used to display directed graph
        graph_canvas = Canvas(graph_frame, bg='white', width=width / 2, height=height)
        graph_canvas.pack()
        graph_canvas.pack(fill=BOTH, expand=1)

        # Create the main menu object
        main_menu = Menu(root)
        open_menu = Menu(main_menu, tearoff=0)

        # Add the pull down menu to the menu bar
        main_menu.add_cascade(label="Graph", menu=open_menu)
        # Lambda functions stops recursive exe of methods
        open_menu.add_command(label="Open", command=lambda:DiGraphUI.open_graph(self))
        # Display the menu bar
        root.config(menu=main_menu)

        # Sizes relative to the display resolution used to ensure UI deign works across multiple display resolutions
        padded_frame_width = graph_frame_width - (graph_frame_width / 8)
        padded_height = height - (height / 25)

        # Counter for measuring size of NetworkX graph/pydot layoutPyDot produced directional node graph
        max_width = 0
        max_height = 0
        pydot_layout = (nx.nx_pydot.pydot_layout(self, prog='dot'))
        # Calculate dimensions of DiGraph, to build/size TkInter interface
        # No library function for it, so must extract values manually
        for node in pydot_layout:
            x = pydot_layout[node][0]
            if x > max_width:
                max_width = x
            y = pydot_layout[node][1]
            if y > max_height:
                max_height = y

        # Extract nodes from NetworkX graph/pydot layout, then insert as labels/widgets in TkInter interface
        frame_graph_layout = {}
        for node in pydot_layout:
            # Extract x and y location, then set relative location in TkInter interface
            x = pydot_layout[node][0]
            x_relative = x * (padded_frame_width / max_width)
            y = pydot_layout[node][1]
            y_relative = (y * (padded_height / max_height)) - (max_height / 200)
            y_relative = padded_height - y_relative
            # Set visuals/aesthetics
            widget = Label(graph_canvas, text=node, fg='white', bg='red')
            widget.place(x=x_relative, y=y_relative)
            frame_graph_layout[node] = x_relative, y_relative
            # Add tool tip to label/node
            ToolTipGen(widget, str(self.nodes[node]['Activity']))

        # Extract choice variables (yes/no edges) from NetworkX graph
        edge_labels = nx.get_edge_attributes(self, 'choice')
        for node, yesNo in edge_labels.items():
            # Extract x and y location, then set relative location in TkInter interface
            start_label_node = node[0]
            end_label_node = node[1]
            start_label_node_x = frame_graph_layout[start_label_node][0]
            start_label_node_y = frame_graph_layout[start_label_node][1]
            end_label_node_x = frame_graph_layout[end_label_node][0]
            end_label_node_y = frame_graph_layout[end_label_node][1]
            avg_label_node_x = (start_label_node_x+end_label_node_x)/2
            avg_label_node_y = (start_label_node_y+end_label_node_y)/2
            # Set visuals/aesthetics
            edge_label = Label(graph_canvas, text=yesNo, fg='black', bg='white')
            edge_label.place(x=avg_label_node_x, y=avg_label_node_y)

        # Insert edges as arrows
        edge_list = list(self.edges)
        # Iterate through edge list
        for edge in edge_list:
            start_node = edge[0]
            end_node = edge[1]
            # Set edge nodes coordinates
            start_node_x = frame_graph_layout[start_node][0]
            start_node_y = frame_graph_layout[start_node][1]
            end_node_x = frame_graph_layout[end_node][0]
            end_node_y = frame_graph_layout[end_node][1]
            # Draw edge/arrow
            graph_canvas.create_line(start_node_x, start_node_y, end_node_x, end_node_y, arrow=LAST)

        ################################################################################################################
        #                                       Complexity UI
        # Add graph name to complexity UI space
        graph_name = Label(complex_frame, text=str(self), font=("TkDefaultFont", 25), bg='white')
        graph_name.place(x=side_frame_width / 2, y=(height / 16), anchor="center")

        # Add complexity header/title
        complexity_header = Label(complex_frame, text="Complexity measures", font=("TkDefaultFont", 25), bg='white')
        complexity_header.place(x=side_frame_width / 2, y=2*(height / 16), anchor="center")

        # Add cylcomatic number + UI for it
        cyclomatic_number_val = DiGraphUI.cyclomatic_number(self)
        cyclomatic_label = Label(complex_frame, text=("Cyclomatic complexity \n" + str(cyclomatic_number_val)),
                                 bg='white', font=("TkDefaultFont", 20))
        cyclomatic_label.place(x=side_frame_width / 2, y=3*(height/8), anchor="center")
        ToolTipGen(cyclomatic_label, 'A measure of connectedness of the graph.')

        # Add restrictiveness estimator number + UI for it
        restrictiveness_val = DiGraphUI.restrictiveness(self)
        restrictiveness_label = Label(complex_frame, text=("Restrictiveness estimator\n" + str(restrictiveness_val)),
                                      bg='white', font=("TkDefaultFont", 20))
        restrictiveness_label.place(x=side_frame_width / 2, y=5 * (height / 8), anchor="center")
        ToolTipGen(restrictiveness_label, 'A measure of complexity, in respect to RCPSP.\n'
                                           'With RCPSP being related to limited resources for activities of known'
                                           ' durations, linked by precedence relations.')

        # Add number of trees+ UI for it
        number_of_trees_val = DiGraphUI.number_of_trees(self)
        number_of_trees_label = Label(complex_frame, text=("Number of trees\n" + str(number_of_trees_val)),
                                     bg='white', font=("TkDefaultFont", 20))
        number_of_trees_label.place(x=side_frame_width / 2, y=7 * (height / 8), anchor="center")
        ToolTipGen(number_of_trees_label, 'The number of distinct trees in the graph.\n'
                                          'A tree being any two reachable nodes, connected by a path.')

        ################################################################################################################
        #                                       Activity list UI
        # Extract list of activities from NetworkX graph object
        list_box = Listbox(root)
        activity_list = self.nodes
        # Iterate/extract activities, insert into UI box
        for activity in activity_list:
            # sys.stdout.write(str(activity) + " - ")
            # sys.stdout.flush()
            list_box.insert(activity, str(activity) + " - " + self.nodes[activity]['Activity'])
        list_box.grid(row=0, column=0, sticky="nsew")
        # Declare as lambda to stop unintended execution
        root.protocol('WM_DELETE_WINDOW', lambda: sys.exit())
        root.mainloop()

    # Disused method for plotting graph in matplotlib, may be useful for for 
    # future diagnostic use, visualisation of data, etc 
    def graph_draw_gen(self):
        for key, value in self.graph.items():
            graph_name = value
        # write_dot(self, 'Image-Graphs/' + graph_name + '.gv') DROP ????
        render('dot', 'png', 'Image-Graphs/' + graph_name + '.gv')
        graphListPos = nx.nx_pydot.pydot_layout(self, prog='dot')
        edge_labels = nx.get_edge_attributes(self, 'choice')
        nx.draw_networkx_edge_labels(self, graphListPos, edge_labels=edge_labels, font_size=4)
        nx.draw(self, graphListPos, with_labels=True, node_size=150, font_size=8)
        plt.savefig('SOP/' + graph_name + '.png', dpi=1000, bbox_inches='tight', pad_inches=0, transparent=True)
        plt.clf()

    # Calculate adn return cyclomatic number
    def cyclomatic_number(self):
        node_num = (self.number_of_nodes())
        edge_num = (self.number_of_edges())
        cyclomatic_number = (edge_num - node_num) + 1
        return cyclomatic_number

    # Calculate and return restrictiveness estimator
    def restrictiveness(self):
        # Global access for number of trees calculation method
        global adjacencyArray
        # Obtain list of edges
        graphListEdges = (list(self.edges))
        # Obtain number of nodes
        node_num = (self.number_of_nodes())
        # Build 2D array of size node_num - Iterate through allElements values, setting them to 0 (no adjacency)
        adjacencyArray = [[0 for x in range(node_num)] for y in range(node_num)]
        # Iterate through list of edges
        for eachEdge in graphListEdges:
            # Init coordinate list
            coord = []
            # Iterate through node pairs that compose edges
            for eachNode in eachEdge:
                # Append node to list
                coord.append(eachNode)
            # CallElements coordinate variables from co-ordinate list
            # then set each subsequent adjacency array value to 1 for each co-ordinate value pair
            adjacencyArray[coord[0]][coord[1]] = 1

        # Init the reachability matrix, using the adjacency array
        reachability_array = [value[:] for value in adjacencyArray]
        # Select all nodes from the array
        for allElements in range(len(reachability_array)):
            # Select all nodes as the start of the path
            for start in range(len(reachability_array)):
                # Select all nodes as the end of the path
                for end in range(len(reachability_array)):
                    # If we are on the shortest path available from start node to end node,
                    # then update the reachability array (with 1)
                    reachability_array[start][end] = reachability_array[start][end] or (
                                reachability_array[start][allElements] and reachability_array[allElements][end])

        # Matrix is defined as the Reflexive transitive closure of the reachability matrix
        # Therefore a node can reach itself so set diagonal elements to 1
        for i in range(len(reachability_array)):
            reachability_array[i][i] = 1

        x_axis = 0
        # Restrictiveness Estimator
        # Convert reachability_array into 1D array/single list
        reachability_list = []
        for eachRow in reachability_array:
            x_axis += 1
            for eachValue in eachRow:
                reachability_list.append(eachValue)

        # Calculate definition of restrictiveness estimator
        restrictiveness_estimator = (
                    ((2 * (sum(reachability_list))) - 6 * (node_num - 1)) / ((node_num - 2) * (node_num - 3)))
        # Round to 3 decimal place
        restrictiveness_estimator = round(restrictiveness_estimator, 3)
        return restrictiveness_estimator

        # # Simple output so that we can see the adjacency array in CMD
        # # Retained in comment form for future diagnostic use, visualisation of data, etc
        # print("--------------------ADJACENCY MATRIX " + str(self) + " --------------------")
        # x_axis = 0
        # sys.stdout.write("\t")
        # sys.stdout.flush()
        # for eachcolumn in range(node_num):
        #     sys.stdout.write(str(eachcolumn) + "\t")
        #     sys.stdout.flush()
        # print()
        # for eachRow in adjacencyArray:
        #     sys.stdout.write(str(x_axis) + "\t")
        #     x_axis += 1
        #     for eachValue in eachRow:
        #         sys.stdout.write(str(eachValue) + "\t")
        #         sys.stdout.flush()
        #     print()

        # # Simple output so that we can see the reachability array in CMD
        # # Retained in comment form for future diagnostic use, visualisation of data, etc
        # print("--------------------REACHABILITY MATRIX " + str(self) + " --------------------")
        # sys.stdout.write("\t")
        # sys.stdout.flush()
        # for eachcolumn in range(node_num):
        #     sys.stdout.write(str(eachcolumn) + "\t")
        #     sys.stdout.flush()
        # print()
        # for eachRow in reachability_array:
        #     sys.stdout.write(str(x_axis) + "\t")
        #     x_axis += 1
        #     for eachValue in eachRow:
        #         sys.stdout.write(str(eachValue) + "\t")
        #         sys.stdout.flush()
        #     print()

    # Calculate and return number of trees
    def number_of_trees(self):
        # Copy adjacency array
        diag_array = copy.deepcopy(adjacencyArray)

        # Diagonal elements = Sum of row
        for i in range(len(diag_array)):
            diag_array[i][i] = sum(diag_array[i])

        # Set negative values
        d_array = copy.deepcopy(adjacencyArray)
        for i in range(len(d_array)):
            for j in range(len(d_array[i])):
                d_array[i][j] = -(d_array[i][j])

        # Merge values into single matrix
        for i in range(len(d_array)):
            d_array[i][i] = copy.deepcopy(diag_array[i][i])

        # NetworkX has no function to calculate sink node (terminating node in graph)
        # However the sink node will have an adjacency of 0
        # We can use this to determine the sink node
        for i in range(len(adjacencyArray)):
            if (sum(diag_array[i])) == 0:
                sink_node = i

        # Convert array to numpy to carry out minor and determinant
        numpy_array = np.array(d_array)
        for i in range(len(diag_array)):
            diag_array[i][i] = sum(diag_array[i])

        # Calculate minor of sink node (delete row and column), creates minor matrix
        numpy_array = np.delete(numpy_array, sink_node, axis=0)
        numpy_array = np.delete(numpy_array, sink_node, axis=1)
        # Number of trees = determinant of minor matrix
        tree_number = int(round((np.linalg.det(numpy_array)), 0))
        return tree_number

        # # Simple output so that we can see the diagonal array in CMD
        # # Retained in comment form for future diagnostic use, visualisation of data, etc
        # print("--------------------D MATRIX" + str(self) + " --------------------")
        # x_axis = 0
        # sys.stdout.write("\t")
        # sys.stdout.flush()
        # for eachcolumn in range(node_num):
        #     sys.stdout.write(str(eachcolumn) + "\t")
        #     sys.stdout.flush()
        # print()
        # for eachRow in numpy_array:
        #     sys.stdout.write(str(x_axis) + "\t")
        #     x_axis += 1
        #     for eachValue in eachRow:
        #         sys.stdout.write(str(eachValue) + "\t")
        #         sys.stdout.flush()
        #     print()

    # Call library function to generate yaml file of NetworkX graph
    def yaml_generator(graph):
        nx.write_yaml(graph, "YAML-graphs/"+str(graph)+".YAML")

    # Call library function to read and return yaml file of NetworkX graph
    def yaml_reader(file_name):
        yaml_graph = nx.read_yaml(file_name)
        return yaml_graph

    def open_graph(self):
        file_name = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("YAML files", "yaml"),))
        # If user closes window, '' is returned, if statement to catch this and stop the software closing
        if file_name == '':
            return
        root.destroy()
        DiGraphUI.ui_graph(DiGraphUI.yaml_reader(file_name))


# Class for tooltip
class ToolTipGen(object):
    def __init__(self, widget, text=None):
        self.text = text
        self.widget = widget
        # Bind widgets to self
        self.widget.bind("<Enter>", self.arrive)
        self.widget.bind("<Leave>", self.depart)
        self.identity = None
        self.top_window = None

    # Respond to mouse entering widget space
    def arrive(self, blank=None):
        self.plan()

    # Respond to mouse leaving widget space
    def depart(self, blank=None):
        self.remove_plan()
        self.hide_tooltip()

    # Schedule events
    def plan(self):
        self.remove_plan()
        self.identity = self.widget.after(0, self.display_tooltip)

    # Remove schedule events
    def remove_plan(self):
        identity = self.identity
        self.identity = None
        if identity:
            self.widget.after_cancel(identity)

    # Display tooltip
    def display_tooltip(self, blank=None):
        # Set/declare variables
        x, y, x1, y2 = self.widget.bbox("insert")
        y += self.widget.winfo_rooty() + 20
        x += self.widget.winfo_rootx() + 25
        # Insert a top window
        self.top_window = Toplevel(self.widget)
        # Remove window, while leaving label
        self.top_window.wm_overrideredirect(1)
        self.top_window.wm_geometry("+%d+%d" % (x, y))
        # Generate label
        label = Label(self.top_window, background="#ffffff", borderwidth=1, justify="left",
                         wraplength=150, relief='solid', text=self.text)
        label.pack()

    # Remove tooltip
    def hide_tooltip(self):
        top_window = self.top_window
        self.top_window = None
        if top_window:
            top_window.destroy()


def main():
    Tk().withdraw()
    global file_name
    file_name = askopenfilename()
    DiGraphUI.ui_graph(DiGraphUI.yaml_reader(file_name))


if __name__ == "__main__":
    main()
