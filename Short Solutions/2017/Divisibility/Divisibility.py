import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback, copy

n = '2017/Divisibility/Divisibility'
fail = ''

def split(x):
    return x.strip('\n').split('\n')

def solve(x):
    x = int(x)
    s = 0
    for i in it.count(0):
        if (x + i) / (i + 1) == (x + i) // (i + 1):
            pass
        else:
            s = i
            break
    return f'streak({x})={s}'

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