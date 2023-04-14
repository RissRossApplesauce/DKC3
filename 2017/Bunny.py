import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback

# 2017 question 2
# took about an hour with distractions
n = 'Bunny/Bunny'
fail = ''

def split(x):
    x = x.strip().splitlines()
    res = list()
    for i in range(len(x) // 3):
        res.append(x[:3])
        x = x[3:]
    
    return res


# slightly more up-to-date solution for best path finding is in notes.py
bestpath = list()
found = 0

def posmoves(path, lhill):
    i = path[-1]
    res = list()
    for idx in range(len(lhill)):
        if idx == i: continue
        h1 = lhill[i]
        h2 = lhill[idx]
        if abs(h2[0] - h1[0]) == abs(h2[1] - h1[1]):
            res.append(idx)
    return res

def betterpath(a):
    return len(a) < len(bestpath)

def iscomplete(path, lhill):
    return len(path) > 0 and path[-1] == len(lhill) - 1    

def isbad(path):
    return len(path) > len(bestpath)

def findpath(path, lhill):
    global bestpath
    global found
    for move in posmoves(path, lhill):
        newpath = path.copy()
        newpath.append(move)
        if isbad(newpath): return
        elif iscomplete(newpath, lhill):
            if betterpath(newpath):
                bestpath = newpath
                found = 1
        else:
            findpath(newpath, lhill)
            
fieldnum = 0

def solve(x):
    ltemps = list(map(int, x[1].split(' ')))
    lhumid = list(map(int, x[2].split(' ')))
    lhill = list(zip(ltemps, lhumid))
    
    global bestpath
    global found
    found = 0
    bestpath = [0] * int(x[0]) ** 2

    findpath([0], lhill)
    
    global fieldnum
    fieldnum += 1
    
    
    return f'Field #{fieldnum}: {len(bestpath) - 1 if found else -1}'
        

def join(x):
    return '\n'.join(x)

sols = list()
for case in split(open(n + 'In.txt').read()):
    try: sol = solve(case)
    except:
        print(str(case))
        print(traceback.format_exc())
        sol = fail
    print(sol)
    sols.append(sol)
    open(n + 'Out.txt', 'w').write(join(sols))