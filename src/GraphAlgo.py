import copy
import json
import math
import heapq as hq
import random
from abc import ABC
from typing import List
from DiGraph import DiGraph
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
                    s = node["pos"]
                    st = str(s).split(",")
                    pos = (float(st[0]), float(st[1]), float(st[2]))
                    graph.add_node(node["id"], pos)
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
                    s = str(node.pos[0]) + "," + str(node.pos[1]) + "," + str(node.pos[2])
                    nodeDict = {"pos": s, "id": node.id}
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
        if (id1 not in self.graph.get_all_v()) or (id2 not in self.graph.get_all_v()):
            return float('inf'), []

        n = self.graph.v_size()
        visited = [False] * n
        weights = [math.inf] * n
        path = []
        pathDict = {}
        queue = []
        weights[id1] = 0
        hq.heappush(queue, (0, id1))
        while len(queue) > 0:
            g, u = hq.heappop(queue)
            visited[u] = True
            for vertex in self.graph.all_out_edges_of_node(u).keys():
                w = self.graph.all_out_edges_of_node(u)[vertex]
                if not visited[vertex]:
                    f = g + w
                    if f < weights[vertex]:
                        weights[vertex] = f
                        pathDict[vertex] = u
                        hq.heappush(queue, (f, vertex))

        if weights[id2] == math.inf:
            return float('inf'), []
        index = id2
        while index != id1:
            path.insert(0, index)
            index = pathDict[index]
        path.insert(0, id1)
        return weights[id2], path

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
            ansList.add(closestNode)

        return ansList, ansDist

    def centerPoint(self) -> (int, float):

        center = -1
        biggestDist = float('inf')
        ans = 0

        for i in self.graph.get_all_v().keys():
            tempDist = 0

            for j in self.graph.get_all_v().keys():

                if i == j:
                    continue
                dist, list = self.shortest_path(i, j)

                if dist > tempDist:
                    tempDist = dist

            if tempDist < biggestDist:
                biggestDist = tempDist
                ans = tempDist
                center = i

        return center, ans

    def plot_graph(self) -> None:
        fillNodes = []
        minX = 0
        minY = 0
        for node in self.graph.get_all_v().values():
            if node.pos is None:
                fillNodes.append(node.id)
            else:
                minX = node.pos[0]
                minY = node.pos[1]

        for n in fillNodes:
            node = self.graph.get_all_v().get(n)
            node.pos[0] = minX + random.random() * 10
            node.pos[1] = minY + random.random() * 10
