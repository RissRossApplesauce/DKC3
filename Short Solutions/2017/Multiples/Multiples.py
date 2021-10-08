import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback, copy

n = '2017/Multiples/Multiples'
fail = ''

def split(x):
    return x.strip('\n').split('\n')

def solve(i):
    i = i.split(' ')
    x = int(i[0])
    p = int(i[1])
    set = 0
    ans = 0
    for i in it.count(0):
        if sorted(list(str(i))) == sorted(list(str(i * x))):
            if set == p:
                ans = i
                break
            set += 1

    return f'[{ans}, {ans * x}]'
    

def join(x):
    return '\n'.join(x)

sols = list()
for case in split(open(n + 'In.txt').read()):
    try: sol = solve(case)
    except:
        print(str(case[:100]))
        print(traceback.format_exc())
        sol = fail
    print(sol)
    sols.append(sol)
    open(n + 'Out.txt', 'w').write(join(sols))