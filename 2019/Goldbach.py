import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback, copy

n = 'Goldbach/Goldbach'
fail = ''

def split(x):
    return x.strip('\n').split('\n')

def isprime(n):
    if n < 2: return False
    if n < 4: return True
    if not n % 2: return False
    if not n % 3: return False

    i = 5
    w = 2
    while i * i <= n:
        if not n % i: return False
        i += w
        w = 6 - w
    return True

def solve(x):
    n = int(x)
    for i in range(n // 2 + 1):
        if isprime(i) and isprime(n - i):
            return f'{i} {n - i}'


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