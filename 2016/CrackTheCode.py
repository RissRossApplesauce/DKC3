import traceback, functools, itertools, cmath, math, collections, re, operator

# took 43:54
n = 'CrackTheCode/CrackTheCode'
fail = ''

def split(x):
    return x.split('\n')

def helper(x):
    return [int(x[0]), int(x[1])]

def parse(x):
    # did not split correct at first
    # split by '(', but really only wanted to split by the FIRST '('
    idx = list(x).index('(')
    r = list()
    r.append(x[0:idx])
    r.append(x[idx:])
    x = r
    x[0] = x[0].strip(',').split(',')
    x[1] = x[1].strip(')(,').split('),(')
    x[1] = list(map(lambda a: helper(a.split(',')), x[1]))
    w = int(x[0][0])
    l = int(x[0][1])
    x[0].pop(0)
    x[0].pop(0)
    return w, l, x[0].copy(), x[1]

def cipher(c):
    if c.isalpha():
        return 25 - (ord(c) - 97) # + 97  --- we were converting to the ascii number when it shouldve been the number in the alphabet
    elif c == ' ':
        return ' '
    else:
        return chr(25 - ((97 + int(c)) - 97) + 97)
    
# we made this while we had a grid, but grids didnt end up working
def apply(g):
    newgrid = list()
    for col in g:
        newcol = list()
        for c in col:
            newcol.append(cipher(c))
        newgrid.append(newcol)
    return newgrid

def solve(x):
    w, l, c, p = x
    # we made a grid with values from c when c was sufficient (c is the list input characters)
    # we had problems indexing the grid
    c = list(c)
    for i in range(len(c)):
        c[i] = cipher(c[i])
        
    result = list()
    for ca in p:
        # had some trouble indexing a 1d array that acts as a 2d array
        # had trouble indexing the 2d grid before it was removed
        result.append(c[ca[0] + ca[1] * w])
    return list(map(lambda a: str(a), result))

def format(x):
    return ''.join(x)

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