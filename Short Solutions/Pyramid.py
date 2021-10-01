import traceback, functools, itertools, cmath, math, collections, re, operator

n = 'Pyramid/Pyramid'
fail = ''

def split(x):
    return x.split('\n\n')

def parse(x):
    return list(map(lambda a: list(map(lambda b: int(b), a.split(' '))), x.split('\n')))

best = list()

def values(x, path):
    row = 0
    result = list()
    for idx in path:
        result.append(x[row][idx])
        row += 1
    return result

def mysum(x, path):
    return sum(values(x, path))

def help(x, path):
    global best
    if len(path) == len(x):
        if mysum(x, best) < mysum(x, path):
            best = path.copy()
    else:
        prev_idx = path[-1]
        path.append(prev_idx)
        help(x, path.copy())
        path.pop(-1)
        path.append(prev_idx + 1)
        help(x, path.copy())

def solve(x):
    global best
    help(x, [0])
    result = best
    best = list()
    return x, result, mysum(x, result)


def format(x):
    triangle, l, s = x
    return ' '.join(list(map(lambda a: str(a), values(triangle, l)))) + ' ' + str(s)

def join(x):
    return '\n'.join(x)
    
sols = list()
for case in split(open(n + 'In.txt').read()):
    try:
        temp = solve(parse(case))
        sol = (format(temp), fail)[temp == None]
    except:
        print('Err on ' + str(case))
        print(traceback.format_exc())
        sol = fail
    else:
        print(sol)
    sols.append(sol)
open(n + 'Out.txt', 'w').write(join(sols))