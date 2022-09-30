import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\ReversePolishIn.txt'
fout = './Short Programming\ReversePolishOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    x = x.split(' ')
    stack = []
    for item in x:
        if (item not in ['+', '-', '*', '/']):
            item = int(item)
            stack.append(item)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(eval(f'{b}{item}{a}'))
    return str(stack[0])

        

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