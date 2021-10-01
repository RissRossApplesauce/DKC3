import traceback, functools, itertools, cmath, math, collections, re, operator

n = 'Factorial/Factorial'
fail = 'none'

def split(x):
    return x.split('\n')

def parse(x):
    return int(x)

def solve(x):
    for i in range(2, x):
        if not x / i == x // i:
            break
        else:
            if x // i == 1:
                return i
        x /= i

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