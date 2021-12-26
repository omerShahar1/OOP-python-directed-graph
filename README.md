# oop_ex3


# websites used for more info:
* https://stackabuse.com/dijkstras-algorithm-in-python/
* https://www.geeksforgeeks.org/how-to-check-the-execution-time-of-python-script/



# algorithm class:
* the shortest_Path function uses Dijkstra’s algorithm. The idea is to traverse all vertices of the graph by using BFS algo consept and use a Min Heap to store the vertices not yet included. Min Heap is used as a priority queue to get the minimum distance vertex from set of not yet included vertices. Time complexity of BFS is o(E+V) and complexity of operations like extract-min and decrease-key value is O(LogV) for Min Heap. therefore, overall time complexity is O(E+V)*O(LogV) which is O((E+V)*LogV) = O(ELogV).
* center function will use the same algorithm as we used before but now we will return for every node the max distance found (max distance from the list of min distances given to us by the Dijkstra's algorithm). after that we will find the node that returned the lowest distance and return it (the node) with the selected distance.
* tsp function will work as followed: for every node in the given list we will treat as the src node and find for each the best path to reach all other nodes in the list. after that we will simply choose the best path from the pathes we created and return it.
in order to find the path from a selected src node we will find the node from the list with the shortest distance from our current src.
after that we will assume the new node is the next in the path so we will add it to the temp list we created for the selected src node. after that we will find the node from the original list with the shortest distance from the node we just add to the path. we will do that again and again until we reached all the nodes from the original list.
* the save functuon will create new file and insert there all the graph data in json format.
* the load function use the graph pre made constructer that works with a given json file name.
* the findNextNode function is udes in the tsp function. we will call it every time we want to know the next node to go to from our current stand (also return the weight and the path we need to go throw to get there).


# node class:
* to create new node we need id number (int) and tuple of the node location (x,y,z)
* every node has dict to represent the nodes we can reach from the current node with 1 edge, and all the nodes who can reach us with 1 edge. the key is always the other node id and the value is the weight of the edge.


# graph class:
* we can contruct an empty graph.
* every graph has dict represent its nodes (key is id and value is the node object), integer mc to count changes to the graph and integer to count anount of edges.
* v_size function return the size of the graph nodes dict.
* e_size funcyion return the graph edges counter.
* get_all_v function return the graph nodes dict.
* all_in_edges_of_node function return the specific node dict represent the nodes who can reach the current node with 1 edge.
* all_out_edges_of_node function return the specific node dict represent the nodes we can reach from the current node with 1 edge.
* get_mc function return the graph changes counter.
* add_edge function will insert the new edge data to the 2 nodes dicts and update the graph counters.
* add_node function will insert new key and value (which we will create) to the graph nodes dict. then update its changes counter (mc).
* remove_node function will remove the node data from all required nodes dicts and then remove the node from the graph nodes dict (and update all the counters in the procces).
* remove_edge function will update the 2 nodes dicts and uodate the graph counters.

<img src="https://github.com/omerShahar1/oop_ex3/blob/main/Screenshot%202021-12-26%20142523.png">
