import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback, copy

n = 'One/One'
fail = ''

def split(x):
    return x.strip('\n').split('\n')

def build(n):
    m = 3 ** n
    vals = ['A', 'L', 'O']
    res = list()
    for i in range(m):
        r = list()
        foundl = False
        alast = False
        bad = False
        for _ in range(n):
            val = i % 3
            if alast and val == 0:
                bad = True
                break
            if val == 0: alast = True
            else: alast = False
            if foundl and val ==1:
                bad = True
                break
            if val == 1: foundl = True
            r.append(vals[val])
            i //= 3
        if not bad:
            r = ''.join(list(reversed(r)))
            res.append(r)
    return res

def solve(x):
    n = int(x)
    if n > 15: return f'{3**n}\n\n*\n'
    res = f'{3 ** n}\n'
    x = build(n)
    while x:
        res += ', '.join(x[:5]) + ',\n'
        x = x[5:]
    res = res[:-2]
    return res + '\n*'

    res += '*\n'
    
    l = list(a.keys())
    






    return x

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
    it.permutations(it.chain.from_iterable(['A', 'L', 'O'] * 4), 4)