import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\BigIn.txt'
fout = './Short Programming\BigOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    x = x.split(', ')
    target = int(x[2])
    l1 = len(x[0])
    l2 = len(x[1])

    l = max(l1, l2)

    x[0] = x[0].zfill(l)
    x[1] = x[1].zfill(l)

    stop = 2 ** (l - 1)
    best = 0
    for i in range(stop - 1, 0, -1):
        s = f'{i:b}'.zfill(l - 1)
        cuts = [bool(int(x)) for x in list(s)]
        cuts.append(True)
        pairs = []
        lastcut = 0
        bad = False
        for n, cut in enumerate(cuts):
            n += 1
            if cut:
                pairs.append((int(x[0][lastcut:n]), int(x[1][l - n:l - lastcut])))
                lastcut = n
                if int(pairs[-1][0]) > target and int(pairs[-1][1]) > target:
                    bad = True
                    break
        if bad: continue
        for b in range(0, 2 ** (len(pairs))):
            bstring = f'{b:b}'.zfill(len(pairs))
            blist = [bool(int(x)) for x in list(bstring)]
            sum = 0
            for b, pair in zip(blist, pairs):
                sum += pair[b]
            if sum < target:
                if sum > best:
                    best = sum
            elif sum == target:
                return target

    return best


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