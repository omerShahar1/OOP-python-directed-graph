from tkinter import *
from GraphAlgo import GraphAlgo
from Gui import Gui

if __name__ == '__main__':
    algo = GraphAlgo()
    root = Tk()
    app = Gui(algo, root)
    root.wm_title("GUI")
    root.mainloop()