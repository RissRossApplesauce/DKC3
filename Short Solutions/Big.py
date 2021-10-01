import traceback, functools, itertools, cmath, math, collections, re, operator

n = 'Big/Big'
fail = ''

def split(x):
    return x.split('\n')

def parse(x):
    x = x.split(', ')
    x = list(map(lambda a: int(a), x))
    return x

def solve(x):
    greater = (x[0], x[1])[x[0] < x[1]]
    digits = len(str(greater))
    best = 0
    for i in range(1, digits):
        a = 10 ** i
        f = x[0] // a
        b = x[1] // (10 ** (digits - i))
        f2 = x[0] % a
        b2 = x[1] % (10 ** (digits - i))
        if f + b > best and f + b < x[2]:
            best = f + b
        if f2 + b2 > best and f2 + b2 < x[2]:
            best = f2 + b2
        if f + f2 > best and f + f2 < x[2]:
            best = f + f2
        if b2 + b > best and b2 + b < x[2]:
            best = b + b2
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