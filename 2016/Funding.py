import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Long Programming\FundingIn.txt'
fout = './Long Programming\FundingOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    return f'{int(x) ** .5:.3f}'

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