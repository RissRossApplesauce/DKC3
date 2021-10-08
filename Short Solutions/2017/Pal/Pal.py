import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback, copy

n = '2017/Pal/Pal'
fail = ''

def split(x):
    x = x.strip('\n').split('\n')
    res = list()
    while x:
        nsounds = int(x[0])
        lsounds = x[1:1 + nsounds]
        nstrings = int(x[1 + nsounds])
        lstrings = x[1 + nsounds + 1: 2 + nsounds + nstrings]
        res.append([lsounds, lstrings])
        x = x[2 + nsounds + nstrings:]
    return res

def issame(a, b, rules : dict):
    if a == b: return True
    if a not in list(rules.keys()):
        return False
    return rules[a] == b

casenum = 0

def solve(x):
    x[0] = list(map(lambda a: a.split(' '), x[0]))
    copyx0 = x[0].copy()
    copyx0 = list(map(lambda a: list(reversed(a)), copyx0))
    x[0] = list(it.chain.from_iterable([x[0], copyx0]))
    x[0] = dict(map(lambda a: tuple(a), x[0]))
    sames = list()
    for string in x[1]:
        stop = False
        for i in range(len(string) // 2):
            if not issame(string[i], string[-1 - i], x[0]):
                sames.append('NO')
                stop = True
        if not stop:
            sames.append('YES')

    global casenum
    casenum += 1

    res = f'Test case #{casenum}:\n'
    for i in range(len(x[1])):
        res += f'{x[1][i]} {sames[i]}\n'


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