import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\\NamesIn.txt'
fout = './Short Programming\\NamesOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n\n').split('\n\n')
    
def solve(x, n):
    x = x.split('\n')
    target = x[0]
    x.sort()
    
    def score(name):
        sum = 0
        for c in name.lower():
            sum += ord(c) - ord('a') + 1
        return sum
    
    return f'{target} - {score(target) * (x.index(target) + 1)}'


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