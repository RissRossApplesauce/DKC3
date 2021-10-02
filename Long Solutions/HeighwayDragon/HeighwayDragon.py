import traceback, functools, itertools, cmath, math, collections, re, operator

# took 27:25 not counting time to read
n = 'HeighwayDragon/HeighwayDragon'
fail = ''

def split(x):
    return x.split('\n')

def parse(x):
    return list(map(lambda a: int(a), x.split(' ')))

d0 = list('Fa')
sub1 = list('aRbFR')
sub2 = list('LFaLb')

def replace(c):
    if c == ['a']:
        return sub1
    if c == ['b']:
        return sub2
    return c

def solve(x):
    n, snum = x
    s = list(map(lambda a: list(a), d0))
    e = list()
    for i in range(0, n):
        s = list(map(replace, s))
        s = list(map(lambda a: list(a), list(itertools.chain.from_iterable(s))))
    
    loc = [0, 0]
    dir = [0, 1]
    steps = 0
    r1 = list()
    s = ''.join(list(map(lambda a: str(a), s)))
    for c in s:
        if c == 'F':
            loc[0] += dir[0]
            loc[1] += dir[1]
            steps += 1
        if c == 'L':
            dircpy = dir.copy()
            dir[0] = -dircpy[1]
            dir[1] = dircpy[0]
        if c == 'R':
            dircpy = dir.copy()
            dir[0] = dircpy[1]
            dir[1] = -dircpy[0]
        if steps == snum:
            r1 = loc.copy()
            
    return n, snum, r1, loc, steps

def format(x):
    n, s, r1, loc, steps = x
    return f'D{n}: Position after {s} steps is ({r1[0]},{r1[1]}) and ends at ({loc[0]},{loc[1]}) with {steps} steps.'

def join(x):
    return '\n'.join(x)
    
sols = list()
for case in split(open(n + 'In.txt').read()):
    try:
        temp = solve(parse(case))
        sol = format(temp) if temp else fail
    except:
        print('Err on ' + str(case))
        print(traceback.format_exc())
        sol = fail
    else:
        print(sol)
    sols.append(sol)
    open(n + 'Out.txt', 'w').write(join(sols))