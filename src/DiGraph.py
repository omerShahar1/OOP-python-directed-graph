from abc import ABC
from GraphInterface import GraphInterface
from Node import Node


class DiGraph(GraphInterface, ABC):
    def __init__(self):
        self.nodes = {}
        self.MC = 0
        self.edgesSize = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.edgesSize

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].inEdges

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].outEdges

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if (id1 in self.nodes) and (id2 in self.nodes) and (id2 not in self.nodes[id1].outEdges):
            self.nodes[id1].outEdges[id2] = weight
            self.nodes[id2].inEdges[id1] = weight
            self.MC = self.MC + 1
            self.edgesSize = self.edgesSize + 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id, pos)
            self.MC = self.MC + 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            return False
        for src in self.nodes[node_id].inEdges:
            self.nodes[src].outEdges.pop(node_id)
            self.edgesSize = self.edgesSize - 1
            self.MC = self.MC + 1
        for dest in self.nodes[node_id].outEdges:
            self.nodes[dest].inEdges.pop(node_id)
            self.edgesSize = self.edgesSize - 1
            self.MC = self.MC + 1
        self.nodes.pop(node_id)
        self.MC = self.MC + 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.nodes[node_id2].inEdges:
            self.nodes[node_id2].inEdges.pop(node_id1)
            self.nodes[node_id1].outEdges.pop(node_id2)
            self.edgesSize = self.edgesSize - 1
            self.MC = self.MC + 1
            return True
        return False

    def __repr__(self):
        return f'{self.nodes}'

