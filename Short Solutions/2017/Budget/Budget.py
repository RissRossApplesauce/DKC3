import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback, copy

n = '2017/Budget/Budget'
fail = ''

def split(x):
    x = x.strip('\n')
    x = x.split('\n')

    res = list()
    while x:
        row1 = x[0].split(' ') 
        count = int(row1[0])
        diseases = x[1:count + 1]
        res.append((row1, diseases))
        x = x[count + 1:]


    return res

def solve(x):
    x = list(x)
    x[0] = list(map(int, x[0]))
    x[1] = list(map(lambda a: a.split(' '), x[1]))
    x[1] = list(map(lambda a: list(map(int, a)), x[1]))
    totalmoney = x[0][1]
    costs = list()
    lives = list()
    for disease in x[1]:
        costs.append(disease[::2])
        lives.append(disease[1::2])

    for i in range(x[0][0]):
        

    return

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