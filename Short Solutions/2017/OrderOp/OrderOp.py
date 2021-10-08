import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback, copy

n = '2017/OrderOp/OrderOp'
fail = ''

def split(x):
    return x.strip('\n').split('\n')

def solve(x):
    for char in list(x):
        if char.isalpha():
            variable = char
            break
    x = x.replace('=', '==')
    for i in range(-100000, 10000):
        try:
            if eval(x.replace(variable, chr(i))):
                return f'{variable} = {i}'
        except:
            continue
    return fail

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