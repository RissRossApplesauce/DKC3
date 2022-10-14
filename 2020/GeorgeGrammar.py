import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\GeorgeGrammarIn.txt'
fout = './Short Programming\GeorgeGrammarOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    copyx = x
    x = list(x)
    letters = sorted([l for l in x if l.isalpha()])
    i = 0
    li = 0
    while i < len(x):
        if x[i].isalpha():
            x[i] = letters[li]
            li +=1
        i += 1
    return copyx + '\n' + ''.join(x)


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