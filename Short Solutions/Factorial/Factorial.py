import traceback, functools, itertools, cmath, math, collections, re, operator

# 2016 question 1
n = 'Factorial/Factorial'
fail = 'none'

def split(x):
    return x.split('\n')

# convert case to int
def parse(x):
    return int(x)

def solve(x):
    # determine if x is a factorial by dividing by each number, starting at 2 and going up until we cant divide any more out
    # start by dividing by 2 because dividing by 1 doesnt help us
    for i in range(2, x):
        # test if x / i is an integer by comparing the result of integer division to floating point division
        if not x / i == x // i:
            break # if x / i is not an integer, break from the for loop, causing solve to return None. the fail case is then used as the answer (it hasnt really failed though)
        else:
            # if x // i == 1, then x == i, and i is the base of the factorial
            # in retrospect we couldve just checked if x == i
            if x // i == 1:
                return i
        # divide x by i to do the next iteration
        x /= i

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