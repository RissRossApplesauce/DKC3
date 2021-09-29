import traceback, functools, itertools, cmath, math, collections, re, operator, sys

n = '.\MissingTerms\MissingTerms'
fail = ''

def split(x):
    return x.split('\n')

def parse(x):
    return x.split(' ')


def solve(x):
    if x[4] == '?':
        return int(eval(' '.join(x)[:-4].replace('^', '**')))
    else:
        string = ' '.join(x).replace('^', '**').replace('=', '==')
        for i in range((x[1] == '/' or x[1] == '%') and x[2] == '?', 2**20):
            if eval(string.replace('?', str(i))):
                return int(i)



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