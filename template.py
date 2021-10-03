import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback

n = 'NAME'
fail = ''

def split(x):
    return x.strip('\n').split('\n')

def solve(x):
    return x

def join(x):
    return '\n'.join(x)

sols = list()
for case in split(open(n + 'In.txt').read()):
    try: temp = solve(case)
    except:
        print(str(case))
        print(traceback.format_exc())
        sol = fail
    print(sol)
    sols.append(sol)
    open(n + 'Out.txt', 'w').write(join(sols))