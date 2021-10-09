import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback, copy

n = 'One copy 2/One'
fail = ''

def split(x):
    return x.strip('\n*').split('\n*\n')

lut = [
    '3211',
    '2221',
    '2122',
    '1411',
    '1132',
    '1231',
    '1114',
    '1312',
    '1213',
    '3112'
]

def solve(x):
    x = x.splitlines()[0]
    x = x[3:-3]

    res = ''
    parts = list()
    for i in range(6):
        parts.append(x[:7])
        x = x[7:]
    x = x[5:]
    for i in range(6):
        parts.append(x[:7])
        x = x[7:]

    res = [''] * 12
    for i in range(12):
        lastlen = 0
        newlen = 0
        lastlen = len(parts[i])
        for _ in range(4):
            parts[i] = parts[i].lstrip(parts[i][0])
            newlen = len(parts[i])
            res[i] += str(lastlen - newlen)
            lastlen = newlen


    res = list(map(lambda a: str(lut.index(a)), res))
    res = ''.join(res)
    return res

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