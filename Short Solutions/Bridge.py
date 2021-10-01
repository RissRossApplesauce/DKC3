import traceback, functools, itertools, cmath, math, collections, re, operator

n = 'Bridge/Bridge'
fail = ''

def split(x):
    return x.split('\n')

def parse(x):
    return int(x)

def solve(x):
    count = 0
    best = 0
    while x != 0:
        if x & 1:
            count += 1
        else:
            count = 0
        if count > best:
            best = count
        x >>= 1

    return best

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