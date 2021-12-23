from tkinter import *
from GraphAlgo import GraphAlgo
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface


class Window(Frame):
    def __init__(self, algo: GraphAlgoInterface, master=None):
        super().__init__(master)
        self.algo = algo
        Frame.__init__(self, master)
        self.master = master
        menu = Menu(self.master)
        self.master.config(menu=menu)
        self.entry = Entry
        self.newWindow = Toplevel
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
        canvas = Canvas(root, width=1500, height=1500, bg="white")
        canvas.pack(pady=20)

        minX = 0.1
        minY = 0.1
        maxX = 0.1
        maxY = 0.1

        once = False
        for node in self.algo.get_graph().get_all_v().values():
            if (once == False):
                minX = node.pos[0]
                minY = node.pos[1]
                maxX = node.pos[0]
                maxY = node.pos[1]
                once = True

            tempX = node.pos[0]
            elif node.pos[0] < minX:
                # bbbb = 0



        for node in self.algo.get_graph().get_all_v().values():
            print(node)
            x = node.pos[0]
            y = node.pos[1]
            r = 0.1
            canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")


    def graphInfo(self):
        n_size = self.algo.get_graph().v_size()
        e_size = self.algo.get_graph().e_size()
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("graph info")
        Label(self.newWindow, text=f"num of nodes: {n_size} and num of edges: {e_size}").pack()

    def load(self):
        pass

    def save(self):
        pass

    def addNode(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("add node")
        self.newWindow.geometry("400x400")
        Button(self.newWindow, text='create', command=self.addNodeButton).pack()
        self.entry = Entry(self.newWindow, width=50)
        self.entry.pack()
        self.entry.insert(0, "id,x,y,z")

    def addNodeButton(self):
        try:
            s = "" + self.entry.get()
            values = s.split(",")
            key = values[0]
            pos = (values[1], values[2], values[3])
            answer = self.algo.get_graph().add_node(key, pos)

            if not answer:
                Label(self.newWindow, text="insertion didn't work").pack()
            else:
                Label(self.newWindow, text="insertion worked").pack()
        except:
            Label(self.newWindow, text="input invalid").pack()

    def addEdge(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("add edge")
        self.newWindow.geometry("400x400")
        Button(self.newWindow, text='create', command=self.addEdgeButton).pack()
        self.entry = Entry(self.newWindow, width=50)
        self.entry.pack()
        self.entry.insert(0, "src,dest,weight")

    def addEdgeButton(self):
        try:
            s = "" + self.entry.get()
            values = s.split(",")
            src = values[0]
            dest = values[1]
            w = values[2]
            answer = self.algo.get_graph().add_Edge(src, dest, w)

            if not answer:
                Label(self.newWindow, text="insertion didn't work").pack()
            else:
                Label(self.newWindow, text="insertion worked").pack()
        except:
            Label(self.newWindow, text="input invalid").pack()

    def removeNode(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("remove node")
        self.newWindow.geometry("400x400")
        Button(self.newWindow, text='remove', command=self.removeNodeButton).pack()
        self.entry = Entry(self.newWindow, width=50)
        self.entry.pack()
        self.entry.insert(0, "id")

    def removeNodeButton(self):
        try:
            s = "" + self.entry.get()
            answer = self.algo.get_graph().remove_node(s)

            if not answer:
                Label(self.newWindow, text="removal didn't work").pack()
            else:
                Label(self.newWindow, text="removal worked").pack()
        except:
            Label(self.newWindow, text="input invalid").pack()

    def removeEdge(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("remove edge")
        self.newWindow.geometry("400x400")
        Button(self.newWindow, text='remove', command=self.removeEdgeButton).pack()
        self.entry = Entry(self.newWindow, width=50)
        self.entry.pack()
        self.entry.insert(0, "src,dest")

    def removeEdgeButton(self):
        try:
            s = "" + self.entry.get()
            values = s.split(",")
            src = values[0]
            dest = values[1]
            answer = self.algo.get_graph().remove_edge(src, dest)

            if not answer:
                Label(self.newWindow, text="removal didn't work").pack()
            else:
                Label(self.newWindow, text="removal worked").pack()
        except:
            Label(self.newWindow, text="input invalid").pack()

    def shortestPath(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("shortest path")
        self.newWindow.geometry("400x400")
        Button(self.newWindow, text='find', command=self.shortestPathButton).pack()
        self.entry = Entry(self.newWindow, width=50)
        self.entry.pack()
        self.entry.insert(0, "src,dest")

    def shortestPathButton(self):
        try:
            s = "" + self.entry.get()
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
        self.entry.insert(0, "enter the following: id1,id2,id3,...")

    def tspButton(self):
        try:
            s = "" + self.entry.get()
            values = s.split(",")
            (path, w) = self.algo.TSP(values)

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
        Label(self.newWindow, text=f"center node id: {key} and the min-maximum distance: {weight}").pack()


graph = GraphInterface()
algo = GraphAlgo(graph)
algo.load_from_json('../../data/A0.json')
print(algo.shortest_path(3,5))

root = Tk()
app = Window(algo, root)
root.wm_title("Tkinter window")
root.mainloop()
