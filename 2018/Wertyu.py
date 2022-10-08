import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\WertyuIn.txt'
fout = './Short Programming\WertyuOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
rows = [
    '1234567890-=',
    'qwertyuiop[]\\'.upper(),
    'asdfghjkl;\''.upper(),
    'zxcvbnm,./'.upper(),
]
def solve(x, n):
    result = ''
    for c in x:
        if c == ' ':
            result += c
        else:
            for row in rows:
                if c in row:
                    result += row[row.index(c) - 1]
                    break
    return result

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