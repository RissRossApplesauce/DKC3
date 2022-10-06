import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\BridgeIn.txt'
fout = './Short Programming\BridgeOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    x = int(x)
    # no 1's means no bridges
    if x == 0: return 0
    
    # convert to a string in binary format
    s = f'{x:b}'
    
    # separate by 0's and get rid of any empty strings ''
    s = s.strip('0').split('0')
    s = [j for j in s if len(j) > 0]
    
    # get the length of the largest bridge
    return len(sorted(s)[-1])

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