from tkinter import *
from GraphAlgoInterface import GraphAlgoInterface


class Gui(Frame):
    def __init__(self, algo: GraphAlgoInterface, master=None):
        super().__init__(master)
        self.algo = algo
        Frame.__init__(self, master)
        self.master = master
        menu = Menu(self.master)
        self.master.config(menu=menu)
        self.entry = Entry
        self.newWindow = Toplevel
        self.canvas = Canvas(master, width=1500, height=600, bg="white")
        self.canvas.pack(pady=20)
        self.paintGraph()

        fileMenu = Menu(menu)
        fileMenu.add_command(label="graph info", command=self.graphInfo)
        fileMenu.add_command(label="load", command=self.load)
        fileMenu.add_command(label="save", command=self.save)
        fileMenu.add_command(label="add node", command=self.addNode)
        fileMenu.add_command(label="add edge", command=self.addEdge)
        fileMenu.add_command(label="remove node", command=self.removeNode)
        fileMenu.add_command(label="remove edge", command=self.removeEdge)
        menu.add_cascade(label="graph", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="shortest path", command=self.shortestPath)
        editMenu.add_command(label="tsp", command=self.tsp)
        editMenu.add_command(label="center", command=self.center)
        menu.add_cascade(label="algo", menu=editMenu)

    def paintGraph(self):
        if self.algo.get_graph().v_size() == 0:
            return
        self.canvas.delete('all')
        minX = float('inf')  # find min X value
        minY = float('inf')  # find min Y value
        maxX = float('-inf')  # find max X value
        maxY = float('-inf')  # find max X value
        for node in self.algo.get_graph().get_all_v().values():
            if node.pos is None:  # if graph is empty then stop
                self.algo.plot_graph()

            if node.pos[0] < minX:
                minX = node.pos[0]
            if maxX < node.pos[0]:
                maxX = node.pos[0]
            if node.pos[1] < minY:
                minY = node.pos[1]
            if maxY < node.pos[1]:
                maxY = node.pos[1]

        if self.algo.get_graph().v_size() == 1:  # in case we only have 1 node in the graph
            absX = abs(maxX)
            absY = abs(maxY)
        else:
            absX = abs(maxX - minX)
            absY = abs(maxY - minY)

        scaleX = 1500 / absX * 0.6
        scaleY = 600 / absY * 0.6
        nodes = []
        for node in self.algo.get_graph().get_all_v().values():
            x = (node.pos[0] - minX) * scaleX + 20
            y = (node.pos[1] - minY) * scaleY + 20
            r = 10
            if node.id not in nodes:
                self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="red")
                nodes.append(node.id)
            for n in self.algo.get_graph().all_out_edges_of_node(node.id).keys():  # draw all out edges and the dest nodes.
                dest = self.algo.get_graph().get_all_v()[n]
                destX = (dest.pos[0] - minX) * scaleX + 20
                destY = (dest.pos[1] - minY) * scaleY + 20
                if n not in nodes:
                    self.canvas.create_oval(destX - r, destY - r, destX + r, destY + r, fill="red")
                    nodes.append(n)
                if n in self.algo.get_graph().all_in_edges_of_node(node.id):
                    self.canvas.create_line(x, y, destX, destY, arrow=BOTH)
                else:
                    self.canvas.create_line(x, y, destX, destY, arrow=LAST)

    def graphInfo(self):
        n_size = self.algo.get_graph().v_size()
        e_size = self.algo.get_graph().e_size()
        mc = self.algo.get_graph().get_mc()
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("graph info")
        Label(self.newWindow, text=f"num of nodes: {n_size}, num of edges: {e_size} and MC value: {mc}").pack()

    def load(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("load")
        self.newWindow.geometry("400x400")
        Button(self.newWindow, text='load', command=self.loadButton).pack()
        self.entry = Entry(self.newWindow, width=50)
        self.entry.pack()
        Label(self.newWindow, text="enter file name").pack()

    def loadButton(self):
        name = str(self.entry.get())
        answer = self.algo.load_from_json(name)
        if not answer:
            Label(self.newWindow, text="load didn't work. file doesn't exist in given path").pack()
        else:
            Label(self.newWindow, text="load worked").pack()
            self.paintGraph()

    def save(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("save")
        self.newWindow.geometry("400x400")
        Button(self.newWindow, text='save', command=self.saveButton).pack()
        self.entry = Entry(self.newWindow, width=50)
        self.entry.pack()
        Label(self.newWindow, text="enter file name").pack()

    def saveButton(self):
        name = str(self.entry.get())
        answer = self.algo.save_to_json(name)
        if not answer:
            Label(self.newWindow, text="save didn't work. try again").pack()
        else:
            Label(self.newWindow, text="save worked").pack()

    def addNode(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("add node")
        self.newWindow.geometry("400x400")
        Button(self.newWindow, text='create', command=self.addNodeButton).pack()
        self.entry = Entry(self.newWindow, width=50)
        self.entry.pack()
        Label(self.newWindow, text="enter id,x,y,z").pack()

    def addNodeButton(self):
        try:
            s = str(self.entry.get())
            values = s.split(",")
            if len(values) > 1:
                key = int(values[0])
                pos = (float(values[1]), float(values[2]), float(values[3]))
                answer = self.algo.get_graph().add_node(key, pos)
            else:
                key = int(values[0])
                answer = self.algo.get_graph().add_node(key)

            if not answer:
                Label(self.newWindow, text="insertion didn't work").pack()
            else:
                Label(self.newWindow, text="insertion worked").pack()
                self.paintGraph()
        except:
            Label(self.newWindow, text="input invalid").pack()

    def addEdge(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("add edge")
        self.newWindow.geometry("400x400")
        Button(self.newWindow, text='create', command=self.addEdgeButton).pack()
        self.entry = Entry(self.newWindow, width=50)
        self.entry.pack()
        Label(self.newWindow, text="enter src,dest,weight").pack()

    def addEdgeButton(self):
        try:
            s = str(self.entry.get())
            values = s.split(",")
            src = int(values[0])
            dest = int(values[1])
            w = float(values[2])
            answer = self.algo.get_graph().add_edge(src, dest, w)

            if not answer:
                Label(self.newWindow, text="insertion didn't work").pack()
            else:
                Label(self.newWindow, text="insertion worked").pack()
                self.paintGraph()
        except:
            Label(self.newWindow, text="input invalid").pack()

    def removeNode(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("remove node")
        self.newWindow.geometry("400x400")
        Button(self.newWindow, text='remove', command=self.removeNodeButton).pack()
        self.entry = Entry(self.newWindow, width=50)
        self.entry.pack()
        Label(self.newWindow, text="enter id number").pack()

    def removeNodeButton(self):
        try:
            s = int(self.entry.get())
            answer = self.algo.get_graph().remove_node(s)

            if not answer:
                Label(self.newWindow, text="removal didn't work").pack()
            else:
                Label(self.newWindow, text="removal worked").pack()
                self.paintGraph()
        except:
            Label(self.newWindow, text="input invalid").pack()

    def removeEdge(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("remove edge")
        self.newWindow.geometry("400x400")
        Button(self.newWindow, text='remove', command=self.removeEdgeButton).pack()
        self.entry = Entry(self.newWindow, width=50)
        self.entry.pack()
        Label(self.newWindow, text="enter src,dest").pack()

    def removeEdgeButton(self):
        try:
            s = str(self.entry.get())
            values = s.split(",")
            src = int(values[0])
            dest = int(values[1])
            answer = self.algo.get_graph().remove_edge(src, dest)

            if not answer:
                Label(self.newWindow, text="removal didn't work").pack()
            else:
                Label(self.newWindow, text="removal worked").pack()
                self.paintGraph()
        except:
            Label(self.newWindow, text="input invalid").pack()

    def shortestPath(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("shortest path")
        self.newWindow.geometry("400x400")
        Button(self.newWindow, text='find', command=self.shortestPathButton).pack()
        self.entry = Entry(self.newWindow, width=50)
        self.entry.pack()
        Label(self.newWindow, text="enter src,dest").pack()

    def shortestPathButton(self):
        try:
            s = str(self.entry.get())
            values = s.split(",")
            src = int(values[0])
            dest = int(values[1])
            w, path = self.algo.shortest_path(src, dest)
            print(self.algo.shortest_path(src, dest))

            if w == float('inf'):
                Label(self.newWindow, text="no path").pack()
            else:
                Label(self.newWindow, text=f"weight: {w} and the path: {path}").pack()
        except():
            Label(self.newWindow, text="input invalid").pack()

    def tsp(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("tsp")
        self.newWindow.geometry("400x400")
        Button(self.newWindow, text='find', command=self.tspButton).pack()
        self.entry = Entry(self.newWindow, width=50)
        self.entry.pack()
        Label(self.newWindow, text="enter id1,id2,id3,...").pack()

    def tspButton(self):
        try:
            s = str(self.entry.get())
            values1 = s.split(",")
            values2 = []
            for i in values1:
                values2.append(int(i))

            (path, w) = self.algo.TSP(values2)

            if w == float('inf'):
                Label(self.newWindow, text="no path").pack()
            else:
                Label(self.newWindow, text=f"weight: {w} and the path: {path}").pack()
        except:
            Label(self.newWindow, text="input invalid").pack()

    def center(self):
        (key, weight) = self.algo.centerPoint()
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("center")
        if key != -1:
            Label(self.newWindow, text=f"center node id: {key} and the min-maximum distance: {weight}").pack()
        else:
            Label(self.newWindow, text="no center. graph is not connected").pack()