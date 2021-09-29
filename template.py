import traceback, functools, itertools, cmath, math, collections, re, operator

n = 'NAME'
fail = ''

def split(x):
    return x.split('\n')

def parse(x):
    return x

def solve(x):
    return x

def format(x):
    return x

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