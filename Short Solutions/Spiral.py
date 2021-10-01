import traceback, functools, itertools, cmath, math, collections, re, operator

n = 'Spiral/Spiral'
fail = ''

def split(x):
    return x.split('\n')

def parse(x):
    return int(x)

def solve(x):
    size = x//2
    if x / 2 == size:
        pass # not solved for even input
    else:
        r = 1
        l = 1
        for s in range(size):
            i = 2 * (s + 1)
            r += 4 * l + 10 * i
            l += 4 * i
        return r

def format(x):
    return str(x)

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