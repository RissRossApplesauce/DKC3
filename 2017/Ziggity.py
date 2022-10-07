import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\ZiggityIn.txt'
fout = './Short Programming\ZiggityOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    x = int(x)

    diagonal = [*range(x - 1)]
    diagonal += diagonal[-2::-1] + [0]
    
    sum = 0
    i = 0
    for diag in diagonal:
        sum += (2 * i) + 1
        i += diag + 2
    
    return sum
        


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