import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Long Programming\\BoggleIn.txt'
fout = './Long Programming\\BoggleOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n\n').split('\n\n')

def notoob(x, y):
    return not any([
        x < 0,
        x >= 4,
        y < 0,
        y >= 4,
    ])


def ingrid(word, grid):
    w = list(word)

    i = 0
    while i < len(w):
        if w[i] == 'q':
            w[i] = w[i] + w[i+1]
            w.pop(i+1)
        i += 1
    
    dirs = [
        (0, 1),
        (1, 0),
        (-1, 0),
        (0, -1),
        (-1, 1),
        (-1, -1),
        (1, -1),
        (1, 1),
    ]

    def wordfrom(remaining, x, y, taken):
        if len(remaining) == 0:
            return True

        for d in dirs:
            newx, newy = d
            newx += x
            newy += y
            if (notoob(newx, newy)
                and grid[newx][newy] == remaining[0]
                and (newx, newy) not in taken
                and wordfrom(remaining[1:], newx, newy, taken + [(newx, newy)])):
                return True
        
        return False

    # make sure that every letter in the word actually exists in the grid
    # this is to deal with adversary input that makes it take a very long time to search
    for letter in word:
        found = False
        for row in grid:
            if letter in row:
                found = True
                break
        if not found:
            return False

    for x in range(4):
        for y in range(4):
            if w[0] == grid[x][y]:
                # found first letter. try to start the word from here

                if wordfrom(w[1:], x, y, [(x, y)]):
                    return True

    return False

table = [
    0,
    0, 
    0,
    1,
    1,
    2,
    3,
    5,
]

def score(word):
    if len(word) >= 8:
        return 11
    return table[len(word)]

def solve(x, n):
    x = x.split('\n')
    grid = x[:4]
    words = x[4]
    for i in range(len(grid)):
        grid[i] = grid[i].split('\t')
        grid[i] = [dice.lower() for dice in grid[i]]
    words = words.split(' ')
    words = [word.lower() for word in words]

    s = 0
    for word in words:
        if ingrid(word, grid):
            s += score(word)
    
    return s

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