import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\MathematicalMarvelIn.txt'
fout = './Short Programming\MathematicalMarvelOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    d = int(x)
    for a in it.count(1):
        temp = d - a
        for b in range(a + 1, int(temp ** 0.5) + 1):
            c = temp // b
            fc = temp / b
            if c == fc:
                return f'{a} {b} {c}'

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