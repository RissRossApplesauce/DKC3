import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\GolfIn.txt'
fout = './Short Programming\GolfOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    x = [int(a) for a in x.split(' ')]
    target = x[0]
    clubs = x[1:]
    clubs.sort(reverse=True)
    besthits = math.inf
    def minhits(dist, numhits):
        nonlocal clubs, besthits
        results = []
        if numhits > besthits:
            return math.inf
        for club in clubs:
            if club > dist:
                continue
            if club == dist:
                besthits = numhits + 1
                return 1
            else:
                results.append(1 + minhits(dist - club, numhits + 1))
        if len(results) == 0:
            return math.inf
        return min(results)
    
    def betterminhits(dist):
        nonlocal clubs, besthits
        available_clubs = [club for club in clubs if club <= dist]
        if len(available_clubs) == 0:
            return math.inf
        for club in available_clubs:
            if club == dist:
                return 0
        besthit = 1 + min([betterminhits(dist - club) for club in available_clubs])
        return besthit

    
    r = betterminhits(target) + 1
    if math.isinf(r):
        return 'Can\'t be done.'
    else: return r
    return minhits(target)

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