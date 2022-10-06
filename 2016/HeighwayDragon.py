import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Long Programming\HeighwayDragonIn.txt'
fout = './Long Programming\HeighwayDragonOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    x = x.split(' ')
    steps = int(x[1])
    n = int(x[0])
    dn = ['F', 'a']

    def expand(s):
        a = list('aRbFR')
        b = list('LFaLb')
        if s == 'a': return a
        elif s == 'b': return b
        else: return s

    for i in range(n):
        dn = list(it.chain(*[expand(q) for q in dn]))

    dirs = [
        (0, 1), # up
        (1, 0), # right
        (0, -1), # down
        (-1, 0), # left
    ]

    curdir = 0
    loc = (0, 0)
    stepcount = 0

    pos1 = (0, 0)

    for ins in dn:
        if ins in ['a', 'b']:
            continue
        elif ins == 'F':
            l1, l2 = loc
            d1, d2 = dirs[curdir]
            loc = (l1 + d1, l2 + d2)
            stepcount += 1
            if stepcount == steps:
                pos1 = loc
        elif ins == 'L':
            curdir -= 1
            if curdir < 0:
                curdir %= 4
        elif ins == 'R':
            curdir += 1
            if curdir > 3:
                curdir %= 4

    return f'D{n}: Position after {steps} steps is ({pos1[0]},{pos1[1]}) and ends at ({loc[0]},{loc[1]}) with {stepcount} steps.'

for num, case in enumerate(splitcases(open(fin).read())):
    print(f'Case {num + 1}:')
    try:
        sol = str(solve(case, num))
        print(sol, '\n')
    except Exception:
        print(f'Input: "{case[:99]}"')
        print(traceback.format_exc())
        sol = ''
    open(fout, 'a').write(sol + '\n')