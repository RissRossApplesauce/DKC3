import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\WordIn.txt'
fout = './Short Programming\WordOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    x = x.split(' ')
    best = 0
    bestword = ''
    # loop through words, score them, and return the best
    for word in x:
        # ord gets the ascii value of a character. sum up for the whole word
        score = sum([ord(c) for c in word])
        if score > best:
            best = score
            bestword = word
    return bestword

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