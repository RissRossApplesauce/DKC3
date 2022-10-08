import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string
from tkinter import Y

fin = './Short Programming\SudokuIn.txt'
fout = './Short Programming\SudokuOut.txt'
open(fout, 'w').close()

def splitcases(x):
    x= x.strip('\n').split('\n')
    cases = []
    while x:
        num = x[0]
        rest = x[1:10]
        x = x[10:]
        cases.append((num, rest))
    return cases
    
def solve(x, n):
    num, puzzle = x
    num = int(num)
    newpuzzle = []
    for row in puzzle:
        newpuzzle.append([*map(int, list(row))])

    def hasdupes(l):
        newl = [*filter(lambda x: x != 0, l)]
        return len(set(newl)) != len(newl)

    def reject(c):
        result = []
        for row in c:
            if hasdupes(row):
                result.append('1')
                break
        for i in range(9):
            col = (row[i] for row in c)
            if hasdupes(col):
                result.append('2')
                break
        flag = False
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                l = []
                for i in range(3):
                    l += c[x + i][y:y + 3]
                if hasdupes(l):
                    result.append('3')
                    flag = True
                    break
            if flag:
                break
        return ' '.join(result)
    result = reject(newpuzzle)
    if not result:
        yn = 'Yes'
    else:
        yn = 'No'

    return f'Case #{num}: {yn} {result}'
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