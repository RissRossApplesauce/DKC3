import traceback, functools, itertools, cmath, math, collections, re, operator, sys

# 2020 question 11
n = '.\MissingTerms\MissingTerms'
fail = ''

def split(x):
    return x.split('\n')

def parse(x):
    return x.split(' ')


# this is not a perfect solution, but it can brute force most answers
def solve(x):
    # if the equation is in the form ... = ? then we can just use eval on the left half of the equals sign
    if x[4] == '?':
        # replace ^ with ** so python recognizes it and convert the list to a string
        return int(eval(' '.join(x)[:-4].replace('^', '**')))
    else:
        # replace ^ with ** and = with ==, then convert to a string
        string = ' '.join(x).replace('^', '**').replace('=', '==')
        # brute force an answer, checking the result of eval for every value of i until it is successful
        # the mess of comparisons in range makes it start at 1 when the operation is division/modulo to avoid division by 0 errors
        for i in range((x[1] == '/' or x[1] == '%') and x[2] == '?', 2**20):
            if eval(string.replace('?', str(i))):
                return int(i) # not sure why we converted i to an int here. it probably was already



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