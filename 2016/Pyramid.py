import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\PyramidIn.txt'
fout = './Short Programming\PyramidOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n\n').split('\n\n')
    
def solve(x, n):
    layers = x.split('\n')
    layers = [[int(b) for b in l.split()] for l in layers]
    
    # a shallow copy (layers.copy()) would be enough, but overkill is better than not doing enought
    l2 = copy.deepcopy(layers)
    path = [layers[0][0]] # path starts at 3

    # start at the 2nd to last layer of the pyramid.
    # for each value in the layer, look at the 2 numbers that you can go to from it. add the larger one to the value above it
    """
    3
    7 4
    2 4 6
    8 5 9 3
    VVV
    3
    7 4
    10 13 15    (10 = 2 + 8, 13 = 4 + 9, 15 = 6 + 9)
    8 5 9 3
    VVV
    3
    20 19
    10 13 15
    8 5 9 3
    VVV
    23
    20 19
    10 13 15
    8 5 9 3
    """
    for row in range(len(layers) - 2, -1, -1):
        for i in range(len(layers[row])):
            m = max(layers[row + 1][i], layers[row + 1][i + 1])
            layers[row][i] +=  m
    
    # now, we can go down the pyramid, always choosing the larger number
    # l2 holds a copy of the original pyramid, so we just look at l2 to get the original values as we go down the new pyramid
    # i tells how far from left-right we are in each layer. it is used to determine which places we can step to as we go down the pyramid
    i = 0
    for row in range(len(layers) - 1):
        # option 1 and option 2
        o1 = layers[row + 1][i]
        o2 = layers[row + 1][i + 1]
        if max(o1, o2) == o1:
            path.append(l2[row + 1][i])
        else:
            path.append(l2[row + 1][i + 1])
            i += 1

    path.append(layers[0][0])
    return ' '.join([str(x) for x in path])


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