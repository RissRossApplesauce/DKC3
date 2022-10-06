"""
There are multiple ways to represent a graph, and the competition tends to use a variety for inputs.
These are helper functions that convert from one representation to another.
"""

def edges2matrix(edges):
    # find all of the vertices that the edges connect to
    # store them in a dictionary and assign each one an index. the indices will be used to create the matrix
    names = {}
    i = 0
    for edge in edges:
        if edge[0] not in names:
            names[edge[0]] = i
            i += 1
        if edge[1] not in names:
            names[edge[1]] = i
            i += 1
            
    # create matrix full of zeros
    V = len(names)
    matrix = [[0 for _ in range(V)] for _ in range(V)]
    
    for edge in edges:
        i0 = names[edge[0]]
        i1 = names[edge[1]]
        weight = edge[2]
        matrix[i0][i1] = weight
        # only do the following line if the graph is UNDIRECTED, meaning there are no one-way edges
        matrix[i1][i0] = weight
    
    return matrix, names

def matrix2edges(matrix, names = {}):
    edges = set()
    
    V = len(matrix)
    
    if names:
        name_lookup = [''] * V
        for key, value in names.items():
            name_lookup[value] = key
            
    for start in range(V):
        for end in range(V):
            if matrix[start][end] != 0:
                if names:
                    edges.add((name_lookup[start], name_lookup[end], matrix[start][end]))
                else:
                    edges.add(start, end, matrix[start][end])
            if matrix[end][start] != 0:
                if names:
                    edges.add((name_lookup[end], name_lookup[start], matrix[end][start]))
                else:
                    edges.add(end, start, matrix[end][start])
    
    return list(edges)

def points2edges(points, names = {}):
    
    def dist(a, b):
        x = a[0] - b[0]
        y = a[1] - b[1]
        return (x ** 2 + y ** 2) ** 0.5 # 'as the bird flies' distance (you can go in a straight path from a to b)
        return abs(x) + abs(y) # 'city block' distance (you can only travel north/east/south/west, no diagonal)
    
    V = len(points)
    
    if names:
        name_lookup = [''] * V
        for key, value in names.items():
            name_lookup[value] = key
    
    # assumes you can travel from any point to any other point
    edges = set()
    for i1, p1 in enumerate(points):
        for i2, p2 in enumerate(points):
            if i1 == i2: continue
            if names:
                edges.add((name_lookup[i1], name_lookup[i2], dist(p1, p2)))
            else:
                edges.add((str(i1), str(i2), dist(p1, p2)))
            
    return edges

def points2matrix(points, names = {}):
    return edges2matrix(points2edges(points, names))

# example of edge representation
# each entry represents the edge connecting between vertexes, along with the 'weight' or distance of the edge
edges = [
    ('A', 'B', 3),
    ('A', 'C', 5),
    ('B', 'C', 2),
    ('B', 'D', 1),
    ('C', 'D', 5),
    ('D', 'X', 1),
    ('X', 'Y', 12),
]

# example of point representation
# each point represents a vertex, and the weights of the edges are just the distances to travel between points
points = [
    (5, 9),
    (20, 20),
    (1, 1),
    (1, 8),
    (2, 8),
]
# the 'names' dictionary maps the name of a vertex to it's index in the list. if you dont need to track the names of vertices, then it's optional
pnames = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

# example of matrix representation
# to retrieve the distance between two nodes, use their corresponding indices: matrix[start_node][end_node]
matrix = [
    [0, 2, 1, 0, 3, 0],
    [2, 0, 5, 0, 5, 0],
    [1, 5, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 12],
    [3, 5, 0, 0, 0, 0],
    [0, 0, 0, 12, 0, 0],
]
# the 'names' dictionary maps the name of a vertex to it's index in the matrix. if you dont need to track the names of vertices, then it's optional
mnames = {'B': 0, 'C': 1, 'A': 2, 'D': 3, 'X': 4, 'Y': 5}