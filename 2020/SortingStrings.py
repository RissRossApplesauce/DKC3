import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\SortingStringsIn.txt'
fout = './Short Programming\SortingStringsOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n*\n').split('\n*\n')
    
def solve(x, n):
    def order(a, b): return -1 if a < b else a > b
    def numslast(a, b):
        return order(a.isnumeric(), b.isnumeric())
    def upperfirst(a, b):
        return order(not a.isupper(), not b.isupper())
    def alphabetical(a, b):
        return order(a.lower(), b.lower())
    def compare(a, b):
        for comp in [numslast, alphabetical, upperfirst]:
            r = comp(a, b)
            if r: return r
        return 0
    return ''.join(sorted(x, key = ft.cmp_to_key(compare)))

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