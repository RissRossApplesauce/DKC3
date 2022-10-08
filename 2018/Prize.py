import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Long Programming\PrizeIn.txt'
fout = './Long Programming\PrizeOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    x = int(x)

    def good(s):
        last = ''
        lcount = 0
        for c in s:
            if c == last and c == 'A':
                return False
            last = c
            if c == 'L':
                lcount += 1
                if lcount > 1:
                    return False
        return True

    combinations = list(it.product('ALO', repeat=x))
    count = len(combinations)
    combinations = list(filter(good, combinations))

    l = []
    while combinations:
        if len(combinations )< 5:
            l.append(combinations)
            break
        else:
            l.append(combinations[:5])
            combinations = combinations[5:]
    
    l = ',\n'.join([
            ', '.join([
                ''.join(word) for word in line
            ])
            for line in l
        ])
    return f'{count}\n{l}\n*'

    pass

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