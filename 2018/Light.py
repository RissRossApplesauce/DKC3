import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\LightIn.txt'
fout = './Short Programming\LightOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n-\n').split('\n-\n')
    
def solve(x, n):
    x = x.split('\n')
    x = [[*map(int, l.split(' '))] for l in x]

    # def combine(i1, i2):
    #     start = (i1[0], i2[0])
    #     end = (i1[1], i2[1])
    #     if i2[0] < i1[1] or i1[0] < i2[1]:
    #         return [min(start), max(end)]

    

    x.sort(key=lambda p: p[1])
    end = x[-1][1]
    x.sort(key=lambda p: p[0])
    start = x[0][0]
    l = list(it.repeat(0, end - start))
    for s, e in x: #nice
        for i in range(s - start, e - start):
            l[i] = 1
            
    return sum(l)

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