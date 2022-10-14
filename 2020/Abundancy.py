import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\AbundancyIn.txt'
fout = './Short Programming\AbundancyOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    x = int(x)
    s = x + 1
    for i in range(2, x):
        if math.lcm(i, x) == x:
            s += i
    return f'{s / x:.3f}'

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