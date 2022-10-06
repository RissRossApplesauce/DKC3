import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\ReversePolishIn.txt'
fout = './Short Programming\ReversePolishOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    # reverse polish is based on a stack: when you get a number, push it to the stack.
    # when you get an operator, apply it to the last 2 items on the stack. the result is whatever remains on the stack
    x = x.split(' ')
    stack = []
    for item in x:
        if item not in ['+', '-', '*', '/']:
            # got a number
            item = int(item)
            stack.append(item)
        else:
            # got an operator
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