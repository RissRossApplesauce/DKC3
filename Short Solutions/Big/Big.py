import traceback, functools, itertools, cmath, math, collections, re, operator

# 2016 problem 3
n = 'Big/Big'
fail = ''

def split(x):
    return x.split('\n')

def parse(x):
    x = x.split(', ')
    # convert each value to an int
    x = list(map(lambda a: int(a), x))
    return x

def solve(x):
    # i couldnt remember python's way of doing the ternary operation, so this is a cheaty way of doing it
    # the smarter way to do this is: greater = x[0] if x[0] > x[1] else x[1]
    greater = (x[0], x[1])[x[0] < x[1]]
    # cheaty way to determine how many digits the number has by converting to a string first
    digits = len(str(greater))
    best = 0
    for i in range(1, digits):
        # the division and mod by 10^i are equivalent to the card tearing mentioned in the question
        # f and f2 are the numbers taken from the front of the card, b and b2 are taken from the back
        f = x[0] // 10 ** i
        b = x[1] // (10 ** (digits - i))
        f2 = x[0] % 10 ** i
        b2 = x[1] % (10 ** (digits - i))
        # now we just need to test every combination to see if it's the best. there is probably a more elegant way of doing this, but we just copy-pasted if statements to be fast
        # note that f and b2 are never compared, and f2 and b are never compared. this is because they are on opposite sides of the same piece of card
        if f + b > best and f + b < x[2]:
            best = f + b
        if f2 + b2 > best and f2 + b2 < x[2]:
            best = f2 + b2
        if f + f2 > best and f + f2 < x[2]:
            best = f + f2
        if b2 + b > best and b2 + b < x[2]:
            best = b + b2
    return best

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