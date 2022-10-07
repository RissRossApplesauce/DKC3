import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\RepeatIn.txt'
fout = './Short Programming\RepeatOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    results=[]
    
    while True:
        results.append(x)
        numlist = list(x)
        numlist = [*map(int,numlist)]
        small = sorted(numlist)
        big = small[::-1]
        small = [*map(str,small)]
        big = [*map(str,big)]
        small = int("".join(small))
        big = int("".join(big))
        newx= big-small
        if (newx==int(x)):
            break
        else:
            x=str(newx)
    return " ".join(results)
    


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