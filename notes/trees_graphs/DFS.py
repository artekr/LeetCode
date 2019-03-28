from collections import defaultdict 
  
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
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(3,5)
g.addEdge(4,6)
g.addEdge(5,6)
g.addEdge(6,7)

# Build the same graph using adjacency_matrix
adjacency_matrix_graph = {  1: [2, 3],
                            2: [4, 5],
                            3: [5],
                            4: [6],
                            5: [6],
                            6: [7],
                            7: []}
###############
# DFS recursive
###############
def DFS_recursive(graph, start):
    visited = set()
    dfs_helper(graph, start, visited)

def dfs_helper(graph, current, visited):
    visited.add(current)
    print(current)
    for vertex in graph[current]:
        if vertex not in visited:
            dfs_helper(graph, vertex, visited)

DFS_recursive(g.graph, 1)
# expected: 1, 2, 4, 6, 7, 5, 3

###############
# DFS iterative
###############
def DFS_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        current = stack.pop()
        visited.add(current)
        print(current)
        for vertex in graph[current]:
            if vertex not in visited:
                stack.append(vertex)

DFS_iterative(g.graph, 1)
# expected: 1, 3, 5, 6, 7, 2, 4

###############
# DFS find the paths between two nodes
###############

def DFS_paths_recursive(graph, start, goal):
    path = [start]
    DFS_paths_recursive_helper(graph, start, goal, path)

def DFS_paths_recursive_helper(graph, current, goal, path):
    if current == goal:
        print(path)
        return path
    for vertex in graph[current]:
        DFS_paths_recursive_helper(graph, vertex, goal, path+[vertex])

DFS_paths_recursive(g.graph, 1, 7)
# expected:
# [1, 2, 4, 6, 7]
# [1, 2, 5, 6, 7]
# [1, 3, 5, 6, 7]

def DFS_paths_iterative(graph, start, goal):
    stack = [(start, [start])]

    while stack:
        current, path = stack.pop()
        for vertex in graph[current]:
            if vertex in path:
                continue
            
            if vertex == goal:
                path.append(vertex)
                print(path)
            else:
                stack.append((vertex, path+[vertex]))

DFS_paths_iterative(g.graph, 1, 7)
# expected:
# [1, 3, 5, 6, 7]
# [1, 2, 5, 6, 7]
# [1, 2, 4, 6, 7]