"""
A graph is just a collection of vertices connected by edges, where each edge has a weight
The minimum spanning tree (MST) of a graph is the 'lightest' set of edges that allows you to reach every vertex in the graph
There are 2 goals here: connect every vertex in the graph & have the sum of the edges be the minimum possible amount
There is only 1 case where there is more than 1 MST: when all the edges have the same weight
"""

import math

# Prim's algorithm to find MST is almost identical to Dijkstra's path finding algorithm
# Assumes graph is a matrix representation of the graph
def primMST(graph):
    # trust that the graph is correctly input as a square matrix
    V = len(graph)
    
    dists = [math.inf] * V
    dists[0] = 0
    parent = [None] * V
    parent[0] = -1 # pick the first node as the root of the tree
    visited = [False] * V
    
    for _ in range(V):
        # find the closest vertex not already traversed
        min = math.inf
        for u in range(V):
            if dists[u] < min and visited[u] == False:
                min = dists[u]
                x = u
        
        visited[x] = True
        
        # save distances to vertices that can be reached through vertex x
        for y in range(V):
            if graph[x][y] > 0 and visited[y] == False and dists[y] > graph[x][y]:
                parent[y] = x
                dists[y] = graph[x][y]
    
    edges = []
    
    for i, p in enumerate(parent[1:], 1):
        edges.append((p, i, graph[p][i]))
    
    return edges

graph = [
#    0   1   2   3   4   5   6
    [0,  16, 12, 21, 0,  0,  0],   #0
    [16, 0,  0,  17, 20, 0,  0,],  #1
    [12, 0,  0,  28, 0,  31, 0,],  #2
    [21, 17, 28, 0,  18, 19, 23,], #3
    [0,  20, 0,  18, 0,  0,  11,], #4
    [0,  0,  31, 19, 0,  0,  27,], #5
    [0,  0,  0,  23, 11, 27, 0,],  #6
]

mst = primMST(graph)

print(mst)

