import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\ClockIn.txt'
fout = './Short Programming\ClockOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    h, m = x.split(':')
    mratio = int(m) / 60
    hratio = (int(h) + (mratio)) / 12
    ratio = abs(mratio - hratio)
    if ratio == 1:
        ratio = 0
    return f'{ratio * 360:.3f}'

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