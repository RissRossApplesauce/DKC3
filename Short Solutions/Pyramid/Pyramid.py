import traceback, functools, itertools, cmath, math, collections, re, operator

# 2016 question 7
n = 'Pyramid/Pyramid'
fail = ''

def split(x):
    return x.split('\n\n')

def parse(x):
    # very nasty looking one liner, but it just converts the input into a 2d array of ints
    return list(map(lambda a: list(map(lambda b: int(b), a.split(' '))), x.split('\n')))

best = list()

# lists the values you get from x (the pyramid) when taking a path
def values(x, path):
    row = 0
    result = list()
    for idx in path:
        result.append(x[row][idx])
        row += 1
    return result

# gets the sum of values in a path
# x is the pyramid
def mysum(x, path):
    return sum(values(x, path))

# we had a lot of problems with this function because we were passing path in by reference (the default way lists are passed) and forgetting the .copy() part
# x is the pyramid
def help(x, path):
    global best
    # path is an array of indices that it follows through the pyramid
    # if path goes all the way through, check if its the best path so far and save it
    if len(path) == len(x):
        if mysum(x, best) < mysum(x, path):
            best = path.copy()
    else:
        # can either go to the same idx in the next row, or idx + 1
        # recursively call with both options
        prev_idx = path[-1]
        path.append(prev_idx)
        help(x, path.copy())
        path.pop(-1)
        path.append(prev_idx + 1)
        help(x, path.copy())

def solve(x):
    # x is the pyramid
    global best
    # help is a recursive function that determines the best path by exploring every possible path, similar to the knights tour problem
    help(x, [0])
    result = best
    best = list()
    return x, result, mysum(x, result)


def format(x):
    # triangle is the pyramid, l is the path, s is the sum of values
    triangle, l, s = x
    # convert the path taken into a list of values, join them with spaces, and add the sum of the path at the end
    return ' '.join(list(map(lambda a: str(a), values(triangle, l)))) + ' ' + str(s)

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