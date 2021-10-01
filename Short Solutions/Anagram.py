import traceback, functools, itertools, cmath, math, collections, re, operator

n = 'Anagram/Anagram'
fail = ''

def split(x):
    return x.split('\n\n')

def parse(x):
    r = x.split('\n')
    return list(map(lambda l: [char.lower() for char in list(l) if char.isalpha()], r))

def solve(x):
    x = list(map(lambda l: sorted(l), x))
    count = 0
    i = j = 0
    while i < len(x):
        j = i + 1
        while j < len(x):
            if x[i] == x[j]:
                count += 1
                x = [l for l in x if l != x[i]]
                i = j = 0
    return count

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