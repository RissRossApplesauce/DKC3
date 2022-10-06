import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\BotchagaloopIn.txt'
fout = './Short Programming\BotchagaloopOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    x = int(x)
    for i in range(5):
        # convert to string in octal form and sort
        p = f'{x:o}'
        q = ''.join(sorted(p))

        if p == q and i != 0:
            break

        # convert back to ints (reading in the string as base 8). then do the math
        x = int(p, base=8) - int(q, base=8)

    return x

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