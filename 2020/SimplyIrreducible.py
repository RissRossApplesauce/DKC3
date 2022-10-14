import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\SimplyIrreducibleIn.txt'
fout = './Short Programming\SimplyIrreducibleOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n*\n').split('\n*\n')
    
def solve(x, n):
    x = int(x)

    def irreducible(num, den):
        return math.gcd(num, den) == 1
    
    s = 0
    for den in range(1, 100):
        for num in range(1, 100):
            if not num / den < x:
                continue
            if not irreducible(num, den):
                continue
            s += num / den
    return f'{s:.3f}'

for num, case in enumerate(splitcases(open(fin).read())):
    print(f'Case {num + 1}:')
    try:
        sol = str(solve(case, num))
        print(sol, '\n')
    except Exception:
        print(f'Input: "{case[:99]}"')
        print(traceback.format_exc())
        sol = ''
    open(fout, 'a').write(sol + '\n*\n')