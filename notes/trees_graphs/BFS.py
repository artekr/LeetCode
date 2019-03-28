from collections import defaultdict 
from collections import deque

# This class represents a DIRECTED graph using  adjacency list representation 
class Graph: 
    # Constructor
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].append(v)


g = Graph()
g.addEdge(1,2)
g.addEdge(1,4)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(3,5)
g.addEdge(5,4)

# Build the same graph using adjacency_matrix
adjacency_matrix_graph = {  1: [2, 4, 3],
                            2: [4, 5],
                            3: [5],
                            4: [],
                            5: [4]}

###############
# BFS visit
###############
def BFS(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        print(current)
        for vertex in graph[current]:
            if vertex not in visited:
                queue.append(vertex)

# BFS(g.graph, 1)
# expected: 1, 2, 4, 3, 5

###############
# BFS find the paths between two nodes
###############
def BFS_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (current, path) = queue.pop(0)
        for vertex in graph[current]:
            if vertex in path:
                continue
            if vertex == goal:
                path.append(vertex)
                print(path)
            else:
                queue.append((vertex, path+[vertex]))

BFS_paths(g.graph, 1, 5)
# expected:
# [1, 2, 5]
# [1, 3, 5]
