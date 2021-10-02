import traceback, functools, itertools, cmath, math, collections, re, operator

# 2016 question 2
n = 'ReversePolish/ReversePolish'
fail = ''

def split(x):
    return x.split('\n')

def parse(x):
    return x.split(' ')

# lookup table so we can quickly get an operator function when given a string
ops = dict({
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
    ('/', operator.floordiv)
})

# the solution to reverse polish is to read left->right and push values to a stack
# when an operation is found, pop the last 2 values, apply the operator, and push the result to the stack
def solve(x):
    stack = list()
    # read left->right
    for el in x:
        # attempt to convert to int (basically checking if it is a value or an operator)
        try:
            val = int(el)
            stack.append(val)
        except:
            # if it is an operator, take the last 2 values, apply operation, and put the result on the stack
            stack[-2] = ops[el](stack[-2], stack[-1])
            # pop the last value because it isnt needed
            stack.pop(-1)
    
    # when the process is done, the result is sitting at the base of the stack
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