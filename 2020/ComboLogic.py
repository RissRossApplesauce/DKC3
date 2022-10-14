import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\ComboLogicIn.txt'
fout = './Short Programming\ComboLogicOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    x = x.split(' ')
    x = [int(b) for b in x]
    b = int((not x[0] and x[1]) or (x[2] and x[3]) or (x[4] and not x[5]))
    def noti(x):
        if x == 0: return 1
        return 0
    i = eval(f'{noti(x[0])}.{x[1]} + {x[2]}.{x[3]} + {x[4]}.{noti(x[5])}')
    return f'{b} - {i}'

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