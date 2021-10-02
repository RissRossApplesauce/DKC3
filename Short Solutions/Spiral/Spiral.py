import traceback, functools, itertools, cmath, math, collections, re, operator

# 2016 question 5
n = 'Spiral/Spiral'
fail = ''

def split(x):
    return x.split('\n')

def parse(x):
    return int(x)

# this question was mostly solved on paper by determining formulas, so the implementation probably isnt very helpful
def solve(x):
    size = x//2
    if x / 2 == size:
        pass # not solved for even input. the question didnt give much information about that case and we decided to skip it
    else:
        r = 1 # result
        l = 1 # last value of previous ring (starts at 1 because 1 is the first ring)
        for s in range(size):
            # s is how many rings away from the center we are
            # formulas found by drawing out the spiral and seeing how much each ring of the spiral adds
            i = 2 * (s + 1) # i means increment. i + the current value gives the next value
            r += 4 * l + 10 * i # formula that gets the total value of the ring
            l += 4 * i # determine the last value of this ring so we can use it in the next iteration
        return r

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