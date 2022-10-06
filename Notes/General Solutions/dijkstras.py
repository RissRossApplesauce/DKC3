import math

# Assumes graph is a matrix representation of the graph. Start is an index
def dijkstra(graph, start):
    # trust that the graph is correctly input as a square matrix
    V = len(graph)
    
    dists = [math.inf] * V
    dists[start] = 0
    parent = [None] * V
    parent[start] = start
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
            if graph[x][y] > 0 and visited[y] == False and dists[y] > dists[x] + graph[x][y]:
                parent[y] = x
                dists[y] = dists[x] + graph[x][y]
    
    # build a list of paths to each vertex
    # only do this if you need the path itself. the shortest distance has already been found
    paths = [[]] * V
    for u in range(V):
        x = u
        # build path backwards, starting at the destination
        paths[u] = [x]
        while x != start:
            if parent[x] is None:
                paths[x] = []
                break
            x = parent[x]
            paths[u].append(x)
        
        paths[u] = paths[u][::-1]
    
    return paths, dists


graph = [
#    0  1   2  3   4   5   6  7   8
    [0, 4,  0, 0,  0,  0,  0, 8,  0], #0
    [4, 0,  8, 0,  0,  0,  0, 11, 0], #1
    [0, 8,  0, 7,  0,  4,  0, 0,  2], #2
    [0, 0,  7, 0,  9,  14, 0, 0,  0], #3
    [0, 0,  0, 9,  0,  10, 0, 0,  0], #4
    [0, 0,  4, 14, 10, 0,  2, 0,  0], #5
    [0, 0,  0, 0,  0,  2,  0, 1,  6], #6
    [8, 11, 0, 0,  0,  0,  1, 0,  7], #7
    [0, 0,  2, 0,  0,  0,  6, 7,  0]  #8
]

start = 0
end = 4

paths, dists = dijkstra(graph, start)

for path, dist in zip(paths, dists):
    print('->'.join(map(str, path)), 'dist:', dist)