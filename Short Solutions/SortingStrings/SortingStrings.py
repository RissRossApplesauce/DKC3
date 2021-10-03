import traceback, functools, itertools, cmath, math, collections, re, operator

# 2020 question 9
n = '.\SortingStrings\SortingStrings'
fail = ''

def split(x):
    return x.split('*\n')

def parse(x):
    return x.strip('\n*')
    
# better solution in notes.py
# very nasty comparison function to determine which char (a or b) goes first
def mycmp(a, b):
    aa = a.isalpha()
    ba = a.isalpha()
    if aa > ba: return -1
    if aa < ba: return 1
    else:
        al = a.lower()
        bl = b.lower()
        if al < bl: return -1
        elif al > bl: return 1
        else:
            au = a.isupper()
            bu = b.isupper()
            if au > bu: return -1
            if au < bu: return 1
            else: return 0

def solve(x):
    # sort the list with mycmp as the key
    return sorted(list(x), key = functools.cmp_to_key(mycmp))

def format(x):
    return ''.join(x)

def join(x):
    return '\n*\n'.join(x)
    
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