import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Long Programming\SpareShoppingIn.txt'
fout = './Long Programming\SpareShoppingOut.txt'
open(fout, 'w').close()

def splitcases(x):
    x = x.strip('\n').split('\n')
    result = []
    while x:
        result.append(
            (x[0], x[1])
        )
        x = x[2:]
    return result

def breakup(s):
    result = {}
    while s:
        for i, l in enumerate(s):
            if l.isalpha():
                break
        num = int(s[:i])

        result[l] = num

        s = s[i + 1:]
    return result
        

class package:
    def __init__(self, name, contents, price):
        self.name = name
        self.contents = breakup(contents)
        self.price = float(price[1:])
        
    
def solve(x, n):
    packages, target = x
    packages = packages.split(', ')
    packages = [*map(lambda a: a.split(' '), packages)]
    packages = [package(*info) for info in packages]
    target = breakup(target)

    best = 0

    def accept(c):
        for key, value in target.items():
            for p in c:
                value -= p.contents.get(key, 0)
            if value > 0:
                return False
        return True
    
    def reject(c):
        if sum(map(lambda p: p.price, c)) > best:
            return True
        return False

    def options(c):
        for p in packages:
            yield c + [p]
    
    bestcombo = []
    def dfs(c):
        if reject(c):
            return
        if accept(c):
            nonlocal bestcombo, best
            best = sum(map(lambda p: p.price, c))
            bestcombo = c
        for o in options(c):
            dfs(o)
    
    dfs([])

    return 

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