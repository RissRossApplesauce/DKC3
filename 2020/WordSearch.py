import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Long Programming\WordSearchIn.txt'
fout = './Long Programming\WordSearchOut.txt'
open(fout, 'w').close()

grid = []
def splitcases(x):
    global grid
    x = x.strip('\n').split('\n')
    grid = x[:25]
    grid = [*map(list, grid)]
    cases = x[25:]
    return cases

dirs = [
    (0, 1, 'Forward'),
    (0, -1, 'Backward'),
    (1, 0, 'Down'),
    (-1, 0, 'Up'),
    (1, 1, 'Diagonal Down Forward'),
    (-1, 1, 'Diagonal Up Forward'),
    (1, -1, 'Diagonal Down Backward'),
    (-1, -1, 'Diagonal Up Backward'),
]

def ingrid(x, y):
    return not any([
        x < 0,
        x >= 25,
        y < 0,
        y >= 25,
    ])

def findremaining(letters, x, y, dir):
    if len(letters) == 0:
        return True
    dx, dy, name = dir
    newx = x + dx
    newy = y + dy
    if not ingrid(newx, newy):
        return False
    if grid[newx][newy] != letters[0]:
        return False
    return findremaining(letters[1:], newx, newy, dir)
    
def solve(x, n):
    word = x
    for i in range(25):
        for j in range(25):
            if grid[i][j] != word[0]:
                continue
            for dir in dirs:
                dx, dy, name = dir
                newx = i + dx
                newy = j + dy
                if not ingrid(newx, newy):
                    continue
                if findremaining(word[1:], i, j, dir):
                    return f'({i},{j}) {name}'

                

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