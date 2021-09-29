import traceback, functools, itertools, cmath, math, collections, re, operator

n = '.\WordSearch\WordSearch'
fail = ''

table = list()
trows = 18 # the question said the table would be 25x25, but the example they gave was only 18x25
tcols = 25

dirlist = [
    (-1,1), 
    (0,1), 
    (1,1), 
    (-1,0), 
    (1,0), 
    (-1,-1), 
    (0,-1), 
    (1,-1), 
]
names = [
    'Diagonal Up Forward',
    'Forward',
    'Diagonal Down Forward',
    'Up',
    'Down',
    'Diagonal Up Backward',
    'Backward',
    'Diagonal Down Backward',
]
namedict = dict(zip(dirlist, names))

def split(x):
    input = x.splitlines()
    global table 
    table = input[:trows]
    words = input[trows:]
    return words

def parse(x):
    return x

def dirs(row,col):
    tuples = dirlist
    if row == 0:
        tuples = filter(lambda t: t[0]!=-1, tuples)
    if col == 0:
        tuples = filter(lambda t: t[1]!=-1, tuples)
    if row == trows - 1:
        tuples = filter(lambda t: t[0]!=1, tuples)
    if col == tcols - 1:
        tuples = filter(lambda t: t[1]!=1, tuples)
    return list(tuples)

def getword(row, col, dir):
    drow, dcol = dir
    result = list()
    while dir in dirs(row, col):
        result.append(table[row][col])
        row += drow
        col += dcol
    result.append(table[row][col])
    return ''.join(result)

def solve(x):
    for row in range(0, trows):
        for col in range (0, tcols):
            for dir in dirs(row, col):
                word = getword(row, col, dir)
                if re.match(x + '.*', word):
                    return row, col, dir
                    
def format(x):
    r, c, dir = x
    return f'({r},{c}) {namedict[dir]}'
    
    

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