import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback, copy

n = 'NAME'
fail = ''

def split(x):
    return x.strip('\n').split('\n')

def solve(x):
    pass

def join(x):
    return '\n'.join(str(x))

sols = list()
for case in split(open(n + 'In.txt').read()):
    try:
        sol = solve(case)
        if not isinstance(sol, str): sol = fail
    except:
        print(str(case[:100]))
        print(traceback.format_exc())
        sol = fail
    print(sol)
    sols.append(sol)
    open(n + 'Out.txt', 'w').write(join(sols))