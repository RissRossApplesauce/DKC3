import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy
from os import curdir

fin = './Short Programming\SpiralIn.txt'
fout = './Short Programming\SpiralOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    x = int(x)
    # we dont know what to do if the input is even, so just dump out 1
    if x % 2 == 0: return 1
    
    # for a 5x5, there are 2 rings, for a 7x7, there are 3 rings, etc.
    rings = x // 2
    
    # the pattern is that each of the 4 corners of a ring increase by the same offset.
    # when you go to the next ring, the offset increases by 2
    # loop through rings, then loop through each value in the ring, adding to the sum as it goes
    sum = 1
    curnum = 1
    offset = 2
    for _ in range(rings):
        for _ in range(4):
            curnum += offset
            sum += curnum
        offset += 2

    return sum

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