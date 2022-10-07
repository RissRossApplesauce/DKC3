import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\ColorIn.txt'
fout = './Short Programming\ColorOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n\n').split('\n\n')
    
def solve(x, n):
    grid = x.split('\n')
    grid = [*map(lambda s: s.split(' '), grid)]
    pass

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