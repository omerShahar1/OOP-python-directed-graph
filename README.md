# oop_ex3


# websites used for more info:
* https://stackabuse.com/dijkstras-algorithm-in-python/



# algorithm class:
* the shortest_Path function uses Dijkstra’s algorithm. The idea is to traverse all vertices of the graph by using BFS algo consept and use a Min Heap to store the vertices not yet included. Min Heap is used as a priority queue to get the minimum distance vertex from set of not yet included vertices. Time complexity of BFS is o(E+V) and complexity of operations like extract-min and decrease-key value is O(LogV) for Min Heap. therefore, overall time complexity is O(E+V)*O(LogV) which is O((E+V)*LogV) = O(ELogV).
* center function will use the same algorithm as we used before but now we will return for every node the max distance found (max distance from the list of min distances given to us by the Dijkstra's algorithm). after that we will find the node that returned the lowest distance and return it (the node) with the selected distance.
* tsp function will work as followed: for every node in the given list we will treat as the src node and find for each the best path to reach all other nodes in the list. after that we will simply choose the best path from the pathes we created and return it.
in order to find the path from a selected src node we will find the node from the list with the shortest distance from our current src.
after that we will assume the new node is the next in the path so we will add it to the temp list we created for the selected src node. after that we will find the node from the original list with the shortest distance from the node we just add to the path. we will do that again and again until we reached all the nodes from the original list.
* the save functuon will create new file and insert there all the graph data in json format.
* the load function use the graph pre made constructer that works with a given json file name.
* the findNextNode function is udes in the tsp function. we will call it every time we want to know the next node to go to from our current stand (also return the weight and the path we need to go throw to get there).
