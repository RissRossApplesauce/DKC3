import traceback, functools, itertools, cmath, math, collections, re, operator

# 2016 question 6
n = 'Bridge/Bridge'
fail = ''

def split(x):
    return x.split('\n')

def parse(x):
    return int(x)

def solve(x):
    count = 0
    best = 0
    # loop until no more bits in x are set to 1
    while x != 0:
        # use & bitwise operator to check what the rightmost bit is. if it's a 1, increase the count
        if x & 1:
            count += 1
        # if it's a 0, reset the count to 0
        else:
            count = 0
        # if the count is better than any previously found count, store it
        if count > best:
            best = count
        # bit shift right one
        x >>= 1
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