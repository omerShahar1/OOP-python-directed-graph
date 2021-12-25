import json
import heapq
import random
from abc import ABC
from typing import List
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface, ABC):
    def __init__(self, graph: GraphInterface = GraphAlgoInterface()):
        self.graph = graph  # the graph of the algorithm

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
                    if "pos" in node:
                        s = node["pos"]
                        st = str(s).split(",")
                        pos = (float(st[0]), float(st[1]), float(st[2]))
                        graph.add_node(node["id"], pos)
                    else:
                        graph.add_node(node["id"])
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
                    if node.pos is not None:
                        s = str(node.pos[0]) + "," + str(node.pos[1]) + "," + str(node.pos[2])
                        nodeDict = {"pos": s, "id": node.id}
                        nodes.append(nodeDict)
                    else:
                        nodeDict = {"id": node.id}
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
            return float('inf'), []  # if the id's are illegal then return.

        visited = {}  # save true or false for each node id.
        weights = {}  # save the shortest distance from src to every other node
        for key in self.graph.get_all_v().keys():  # zero the visited and weights values
            visited[key] = False
            weights[key] = float('inf')

        path = []  # final path to take from src to dest
        pathDict = {}  # key is id and value is the id of the node we travel from to the key node
        queue = []  # priority queue
        weights[id1] = 0  # distance from src to itself is always 0
        heapq.heappush(queue, (0, id1))
        while len(queue) > 0:
            (g, u) = heapq.heappop(queue)  # g is the distance from src to node u
            visited[u] = True
            for vertex in self.graph.all_out_edges_of_node(u).keys():  # check all nodes out from node u
                w = self.graph.all_out_edges_of_node(u)[vertex]
                if not visited[vertex]:
                    f = g + w
                    if f < weights[vertex]:
                        weights[vertex] = f
                        pathDict[vertex] = u
                        heapq.heappush(queue, (f, vertex))

        if weights[id2] == float('inf'):  # if distance is still float('inf') then we don't have a path
            return float('inf'), []
        index = id2
        while index != id1:  # calculate the path
            path.insert(0, index)
            index = pathDict[index]
        path.insert(0, id1)
        return weights[id2], path

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        visited = {}  # to check if we have already been to a specific node in a specific run
        path = {}  # final path to take
        weight = float('inf')  # final weight of the path
        for i in node_lst:  # check if one of the given id's is illegal.
            if i not in self.graph.get_all_v().keys():
                return [], float('inf')

        for key in node_lst:
            for i in node_lst:  # zero all the visited values.
                visited[i] = False
            src = key
            visited[src] = True
            newPath = [src]  # create new path and add the src key to the new path.
            newWeight = 0
            while False in visited.values():  # for every src find the best path from it to the other.
                (tempList, w, newSrc) = self.findNextNode(src, visited, node_lst)
                if newSrc == -1:  # in case we don't have a path stop the function.
                    return [], float('inf')

                newWeight += w
                tempList.remove(src)

                for i in tempList:  # insert the new path we found to the main path of the specific key
                    newPath.append(i)
                visited[newSrc] = True
                src = newSrc
            if newWeight < weight:
                weight = newWeight
                path = newPath

        return path, weight

    def centerPoint(self) -> (int, float):
        center = -1  # id of the center
        minDist = float('inf')  # the min distance selected

        for i in self.graph.get_all_v().keys():  # go over all nodes
            dist = self.shortest_path_for_center(i)  # dist is the max distance from node i to another node
            if dist == -1:  # if dist=-1 then the graph is not connected
                return -1, float('inf')

            if dist < minDist:
                minDist = dist
                center = i

        return center, minDist

    def shortest_path_for_center(self, id1: int) -> float:
        visited = {}  # save true or false for each node id.
        weights = {}  # save the shortest distance from src to every other node
        for key in self.graph.get_all_v().keys():  # zero the visited and weights values
            visited[key] = False
            weights[key] = float('inf')

        queue = []  # priority queue
        weights[id1] = 0  # distance from src to itself is always 0
        heapq.heappush(queue, (0, id1))
        while len(queue) > 0:
            g, u = heapq.heappop(queue)  # g is the distance from src to node u
            visited[u] = True
            for vertex in self.graph.all_out_edges_of_node(u).keys():  # check all nodes out from node u
                w = self.graph.all_out_edges_of_node(u)[vertex]
                if not visited[vertex]:
                    f = g + w
                    if f < weights[vertex]:
                        weights[vertex] = f
                        heapq.heappush(queue, (f, vertex))

        if float('inf') in weights:  # if the graph is not connected return -1
            return -1

        max = -1
        for i in weights.values():  # check max distance
            if max < i:
                max = i

        return max

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
            self.graph.get_all_v().get(n).pos = (minX + random.random() * 10, minY + random.random() * 10)

    def findNextNode(self, src: int, visited: dict, node_lst: list) -> (List[int], float, int):
        weight = float('inf')
        key = 0
        path = []

        for node in node_lst:  # go over all the nodes and check for the one with the shortest path from src.
            if visited[node]:
                continue
            (newWeight, newPath) = self.shortest_path(src, node)
            if newWeight == float('inf'):  # in case we don't have a path return null.
                return [], -1.0, -1,

            if newWeight < weight:
                weight = newWeight
                path = newPath
                key = node

        return path, weight, key
