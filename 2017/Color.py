import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\ColorIn.txt'
fout = './Short Programming\ColorOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n\n').split('\n\n')
    
def solve(x, n):
    grid = x.split('\n')
    grid = [*map(lambda s: s.split(' '), grid)]

    def accept(grid):
        color = None
        for row in grid:
            for entry in row:
                if color is None:
                    color = entry
                elif entry != color:
                    return False
        return True

    def options(grid):
        results = []
        direction = [
            (0, 1),
            (1, 0),
        ]

        colors = ['Red', 'White', 'Blue']
        for i in range(len(grid)):
            for j in range(len(grid)):
                color = grid[i][j]
                for d in direction:
                    di, dj = d
                    newi = i + di
                    newj = j + dj
                    if 0 <= newi < len(grid) and 0 <= newj < len(grid):
                        color2 = grid[newi][newj]
                        if color == color2:
                            continue
                        newgrid = copy.deepcopy(grid)
                        for othercolor in colors:
                            if othercolor != color and othercolor != color2:
                                break
                        newgrid[i][j] = othercolor
                        newgrid[newi][newj] = othercolor
                        results.append(newgrid)
        return results
    
    def bfs(grid):
        explored = list()
        q = co.deque()
        explored.append(grid)
        q.append((grid, 0))
        while q:
            current_grid, moves = q.popleft()
            if accept(current_grid):
                return moves
            for new_grid in options(current_grid):
                if new_grid not in explored:
                    explored.append(new_grid)
                    q.append((new_grid, moves + 1))

    def mbf(grid):
        if len(grid) == 1:
            return 0
        c = co.Counter()
        for row in grid:
            for entry in row:
                c[entry] += 1
        allyall = c.most_common()
        return allyall[-1][1]

    if len(grid) > 5:
        # best guess that will hopefully get some points
        return mbf(grid)
    else:
        # brute force that only works on very small inputs
        return bfs(grid)

for num, case in enumerate(splitcases(open(fin).read())):
    print(f'Case {num + 1}:')
    try:
        sol = str(solve(case, num))
        print(sol, '\n')
    except Exception:
        print(f'Input: "{case[:99]}"')
        print(traceback.format_exc())
        sol = ''
    open(fout, 'a').write(sol + '\n')