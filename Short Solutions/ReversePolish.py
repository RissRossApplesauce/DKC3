import traceback, functools, itertools, cmath, math, collections, re, operator

n = 'ReversePolish/ReversePolish'
fail = ''

def split(x):
    return x.split('\n')

def parse(x):
    return x.split(' ')

ops = dict({
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
    ('/', operator.floordiv)
})

def solve(x):
    stack = list()
    for el in x:
        try:
            val = int(el)
            stack.append(val)
        except:
            stack[-2] = ops[el](stack[-2], stack[-1])
            stack.pop(-1)
    
    return stack[0]
            


def format(x):
    return str(x)

def join(x):
    return '\n'.join(x)
    
sols = list()
for case in split(open(n + 'In.txt').read()):
    try:
        temp = solve(parse(case))
        sol = (format(temp), fail)[temp == None]
    except:
        print('Err on ' + str(case))
        print(traceback.format_exc())
        sol = fail
    else:
        print(sol)
    sols.append(sol)
open(n + 'Out.txt', 'w').write(join(sols))