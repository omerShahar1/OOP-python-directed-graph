import copy
import json
from abc import ABC
from typing import List
from DiGraph import DiGraph
from queue import PriorityQueue
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface, ABC):
    def __init__(self, graph: GraphInterface):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as file:
                graph = DiGraph()
                reader = json.load(file)
                edges_list: list = reader["Edges"]
                nodes_list: list = reader["Nodes"]
                for node in nodes_list:
                    graph.add_node(node["id"], node["pos"])
                for edge in edges_list:
                    graph.add_edge(edge["src"], edge["dest"], edge["w"])
                graph.MC = 0
                self.graph = graph
                return True
        except():
            print("file not found")
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as file:
                nodes = []
                edges = []
                for node in self.graph.get_all_v().values():
                    nodeDict = {"pos": node.pos, "id": node.id}
                    nodes.append(nodeDict)
                    for dest in self.graph.all_out_edges_of_node(node.id):
                        edgeDict = {"src": node.id, "w": node.outEdges[dest], "dest": dest}
                        edges.append(edgeDict)
                finalDict = {"Edges": edges, "Nodes": nodes}
                jsonWriter = json.dumps(finalDict)
                file.write(jsonWriter)
                return True
        except():
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        dist = {}  # shortest distance (value) from src to all other nodes (each node is id a key).
        pathDict = {}
        path = []
        visited = {}
        for i in self.graph.get_all_v():
            dist[i] = float('inf')
            visited[i] = False

        dist[id1] = 0.0
        pq = PriorityQueue()
        pq.put((0, id1))

        while not pq.empty():
            (key, current) = pq.get()
            dist[current] = key

            visited[current] = True
            for neighbor in self.graph.all_out_edges_of_node(current):  # all the nodes we can get to from current
                distance = self.graph.all_out_edges_of_node(current)[neighbor]
                if neighbor not in visited:
                    newD = dist[current] + distance
                    if newD < dist[neighbor]:
                        pathDict[neighbor] = current
                        pq.put((newD, neighbor))
                        dist[neighbor] = newD
        index = id2
        while index != id1:
            path.insert(0, index)
            id2 = pathDict[index]

        return dist[id2], path

    def TSP(self, node_lst: List[int]) -> (List[int], float):

        newList = copy.deepcopy(node_lst)

        ansList = []
        ansDist = 0

        ansList.__add__(newList[0])
        newList.remove(newList[0])

        while (newList.__sizeof__() > 0):
            closestNode
            closestDistance = 0

            for i in newList:
                dist, list = self.shortest_path(ansList[-1], i)

                if (dist < closestDistance):
                    closestDistance = dist
                    closestNode = list[-1]

            ansDist += closestDistance
            ansList.__add__(closestNode)

        return ansList, ansDist

    def centerPoint(self) -> (int, float):

        center = -1
        biggestDist = float('inf')
        ans = 0

        for i in self.graph.get_all_v().keys():
            tempDist = 0

            for j in self.graph.get_all_v().keys():

                if (i == j):
                    continue
                dist, list = self.shortest_path(i, j)

                if (dist > tempDist):
                    tempDist = dist

            if (tempDist < biggestDist):
                biggestDist = tempDist
                ans = tempDist
                center = i

        return center, ans


    def plot_graph(self) -> None:
        fillNodes = []
        minX = 0
        minY = 0
        for node in self.graph.get_all_v():
            if node.pos is None:
                fillNodes.append(node.id)






