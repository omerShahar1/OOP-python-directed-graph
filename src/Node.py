class Node:
    def __init__(self, node_id: int, pos: tuple):
        self.id = node_id
        self.pos = pos
        self.inEdges = {}  # key is the src node id. key is the weight.
        self.outEdges = {}  # key is the dest node id. key is the weight.

    def __repr__(self):
        return f'pos: {self.pos}\tin edges from: {self.inEdges}\tout nodes from: {self.outEdges}\n'
