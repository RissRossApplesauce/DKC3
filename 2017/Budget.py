import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\BudgetIn.txt'
fout = './Short Programming\BudgetOut.txt'
open(fout, 'w').close()

def splitcases(x):
    x=x.strip('\n').split('\n')
    results=[]
    while x:
        l1 = x[0]
        l1 = l1.split(" ")
        diseases = l1[0]
        budget = l1[1]
        disbudge = []
        for i in range (1,int(diseases)+1):
            disbudge.append(x[i])
        x=x[int(diseases)+1:]
        results.append((diseases,budget,disbudge))
    return results
    
def solve(x, n):

    diseases, budget, cutoffs = x
    diseases = int(diseases)
    budget = int(budget)
    newcutoffs = []
    for cutoff in cutoffs:
        newcutoff = [*map(int, cutoff.split(' '))]
        keys = newcutoff[::2] + [0]
        values = newcutoff[1::2] + [0]
        d = dict(zip(keys, values))
        newcutoffs.append(d)

    pos = it.product(*map(lambda d: d.keys(), newcutoffs))
    pos = [*filter(
        lambda x:
        sum(x) <= budget
        ,
        pos
    )]

    def l(prices):
        lives = 0
        for i, price in enumerate(prices):
            lives += newcutoffs[i][price]
        return lives

    lives = max(map(l, pos))

    return f'Budget #{n + 1}: Maximum of {lives} lives saved.'

for num, case in enumerate(splitcases(open(fin).read())):
    print(f'Case {num + 1}:')
    try:
        sol = str(solve(case, num))
        print(sol, '\n')
    except Exception:
        print(f'Input: "{case[:99]}"')
        print(traceback.format_exc())
        sol = ''
    open(fout, 'a').write(sol + '\n')