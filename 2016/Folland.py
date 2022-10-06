import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\FollandIn.txt'
fout = './Short Programming\FollandOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    x = x.split(' ')
    command = x[0]
    numbers = [int(a) for a in x[1:]]

    # loop through and add/subtract in the correct order depending on command
    if command[0] == 'D':
        #decompress
        for i in range(len(numbers) - 1):
            numbers[i + 1] = numbers[i] + numbers[i + 1]
    else:
        #compress
        for i in range(len(numbers) - 2, 0, -1):
            numbers[i + 1] = numbers[i + 1] - numbers[i]
    
    return ' '.join([str(n) for n in numbers])

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