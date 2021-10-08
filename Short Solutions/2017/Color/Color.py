import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback, copy

n = '2017/Color/Color'
fail = ''

def split(x):
    return x.strip('\n\n').split('\n\n')

def solve(x):
    grid = list()
    for line in x.splitlines():
        grid.append(line.split(' '))

    bestpath = []



    def posmoves(path):
        result = list()
        for row in len(path[-1]):
            for col in len(path[-1]):
                if path[-1][row][col] != 

    def isbest(path):
        pass

    def isdone(path):
        pass


    def findpath(path):
        nonlocal bestpath
        stack = [(path, posmoves(path))]
        while stack:
            newpath = stack[-1][0].copy()
            moves = stack[-1][1]
            if isdone(newpath):
                if isbest(newpath):
                    bestpath = newpath.copy()
                    stack.pop()
                    continue
            if not moves:
                stack.pop()
            else:
                newpath.append(moves.pop())
                stack.append((newpath, posmoves(newpath)))

def join(x):
    return '\n'.join(x)

sols = list()
for case in split(open(n + 'In.txt').read()):
    try: sol = solve(case)
    except:
        print(str(case[:100]))
        print(traceback.format_exc())
        sol = fail
    print(sol)
    sols.append(sol)
    open(n + 'Out.txt', 'w').write(join(sols))