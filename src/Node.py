class Node:
    def __init__(self, node_id: int, pos: tuple):
        self.id = node_id
        self.pos = pos
        self.inEdges = {}  # key is the src node id. value is the weight.
        self.outEdges = {}  # key is the dest node id. value is the weight.

    def setPos(self, pos: tuple):
        self.pos = pos

    def __repr__(self):
        return f'\nnode id: {self.id} and location: {self.pos}\nedges outside: {self.inEdges}\nedges inside: {self.outEdges}\n'

