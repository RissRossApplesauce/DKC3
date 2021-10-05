import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback

# took about 45 minutes for 45 points
n = 'Vampire/Vampire'
fail = ''

def split(x):
    return x.strip('\n*').split('\n*')

def solve(x):
    x = x.strip().split('\n')
    goal = x[-1]
    goal = goal.split(' ')
    x = x[:-1]
    routes = list()
    for line in x:
        line = line.split(' ')
        line[2] = int(line[2])
        line[3] = int(line[3])
        if line[2] >= 19 or line[2] <= 7 and (line[3] + line[2]) % 24 <= 7:
            routes.append(line)

    bestpath = []

    def posmoves(path):
        last = path[-1][1]
        moves = list()
        for route in routes:
            if route[0] == last:
                moves.append(route)
        return moves

    def compare(a, b): return -1 if a < b else a > b

    def pathblood(path):
        count = 0
        lastmove = path[0]
        for i in range(1, len(path)):
            if lastmove[2] + lastmove[3] < (path[i][2] + 24 if path[i][2] <= 7 else path[i][2]):
                count -= 1
            count += 1
            lastmove = path[i]
        return count

    def minblood(a, b):
        return compare(pathblood(a), pathblood(b))

    def lesshours(a, b):
        hoursa = hoursb = 0
        for route in a:
            hoursa += route[3]
        for route in b:
            hoursb += route[3]
        return compare(hoursa, hoursb)

    def shortest(a, b): return compare(len(a), len(b))


    def isbest(path):
        if not bestpath: return True
        for comp in [minblood, lesshours, shortest]:
            r = comp(path, bestpath)
            if r == -1: return True
            if r == 1: return False
        return False
        

    def isdone(path):
        last = path[-1][1]
        return last == goal[1]


    def findpath(path):
        for move in posmoves(path):
            newpath = path.copy()
            newpath.append(move)
            if isdone(newpath):
                if isbest(newpath):
                    nonlocal bestpath
                    bestpath = newpath
            else:
                findpath(newpath)

    starts = [route for route in routes if route[0] == goal[0]]
    for start in starts:
        findpath([start])

    answer = ''
    for route in bestpath:
        answer += route[0] + ' '
    answer += bestpath[-1][1] + ' '

    hours = 0
    for route in bestpath:
        hours += route[3]

    answer += str(hours) + '\n'

    answer += str(pathblood(bestpath))
    return answer

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