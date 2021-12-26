import time
from GraphAlgo import GraphAlgo

a = GraphAlgo()

start = time.time()
a.load_from_json("../data/10000.json")
end = time.time()
print("python load time in seconds: ", end - start)
print()

start = time.time()
a.save_to_json("../test.json")
end = time.time()
print("python save time in seconds: ", end - start)
print()

start = time.time()
a.shortest_path(6, 700)
end = time.time()
print("python shortestPath time in seconds: ", end - start)
print()

start = time.time()
a.centerPoint()
end = time.time()
print("python center time in seconds: ", end - start)
print()

start = time.time()
a.TSP([1, 8, 20, 100, 500])
end = time.time()
print("python tsp time in seconds: ", end - start)
