import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback, copy

n = '2017/Repeat/Repeat'
fail = ''

def split(x):
    return x.strip('\n').split('\n')

def next(x):
    s = sorted(x)
    r = ''.join(list(reversed(s)))
    s = ''.join(s)
    return str(int(str(r)) - int(str(s)))

def solve(x):
    res = [x]
    while next(x) != res[-1]:
        res.append(next(x))
        x = next(x)

    return ' '.join(res)

def join(x):
    return '\n'.join(x)

sols = list()
for case in split(open(n + 'In.txt').read()):
    try: sol = solve(case)
    except:
        print(str(case[:100]))
        print(traceback.format_exc())
        sol = fail
    print(sol)
    sols.append(sol)
    open(n + 'Out.txt', 'w').write(join(sols))