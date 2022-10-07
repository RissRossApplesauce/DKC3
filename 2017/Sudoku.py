import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\SudokuIn.txt'
fout = './Short Programming\SudokuOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n*\n').split('\n*\n')
    
def solve(x, n):
    puzzles = x.split('\n\n')
    for i, puzzle in enumerate(puzzles):
        newpuzzle = []
        for row in puzzle.split('\n'):
            newpuzzle.append([*map(int, list(row))])
        puzzles[i] = newpuzzle
    

    def accept(c):
        for row in c:
            for col in row:
                if col == 0:
                    return False
        return True
    
    def hasdupes(l):
        newl = [*filter(lambda x: x != 0, l)]
        return len(set(newl)) != len(newl)

    def reject(c):
        for row in c:
            if hasdupes(row):
                return True
        for i in range(9):
            col = (row[i] for row in c)
            if hasdupes(col):
                return True
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                l = []
                for i in range(3):
                    l += c[x + i][y:y + 3]
                if hasdupes(l):
                    return True
        return False

    def options(c):
        # generator version
        flag = False
        for col in range(9):
            for row in range(9):
                if c[row][col] == 0:
                    flag = True
                    break
            if flag:
                break
        
        # row, col has a 0
        for i in range(1, 10):
            c[row][col] = i
            yield c
        
        c[row][col] = 0

    # Non-generator version.
    # This waste a lot of time making copies of c, while the generator just modifies c
    # def options(c):
    #     o = []
    #     flag = False
    #     for col in range(9):
    #         for row in range(9):
    #             if c[row][col] == 0:
    #                 flag = True
    #                 break
    #         if flag:
    #             break
        
    #     # row, col has a 0
    #     for i in range(1, 10):
    #         newsudoku = copy.deepcopy(c)
    #         newsudoku[row][col] = i
    #         o.append(newsudoku)

    #     return o

    results = []

    def backtrack(c):
        if reject(c):
            return
        if accept(c):
            nonlocal results
            results.append(c)
            return True
        for o in options(c):
            if backtrack(o):
                return True

    for puzzle in puzzles:
        backtrack(puzzle)
    
    sum = 0
    for result in results:
        sum += int(''.join(map(str, result[0][:3])))


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