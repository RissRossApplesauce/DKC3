import traceback, functools, itertools, cmath, math, collections, re, operator

# 2020 question 10
n = '.\Concrete\Concrete'
fail = ''

def split(x):
    return x.split('\n')

def parse(x):
    # convert to list of ints
    x = x.split(', ')
    x = list(map(lambda a: int(a), x))
    return x

def solve(x):
    # pretty much just applying the formulas as they said to
    # we initially forgot the ceil (round up to nearest int) and floor (round down to nearest int)
    weight, width = x
    w = math.ceil(weight / width * 1.75)
    d = math.floor(weight/w + width/2)
    a = math.ceil(w * w * d / (12 ** 3) / .45)
    return w, d, a


def format(x):
    return ', '.join(map(lambda s: str(s), x))

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