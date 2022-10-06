import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\ConnectFourIn.txt'
fout = './Short Programming\ConnectFourOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n\n').split('\n\n')
    
def solve(x, n):
    grid = [[int(b) for b in l.split(' ')] for l in x.split('\n')]
    
    # loop over every square in the grid.
    # if it is in a spot where it could be the start of the 4 numbers (meaning we arent too close to the edge to get 4 numbers),
    # then check the product and save it if its the best
    bestproduct = 0
    bestnums = [0, 0, 0, 0]
    bestdir = ''
    for i in range(20):
        for j in range(20):
            # can be horizontal if it is not one of the last 3 in the row
            # can be vertical if it is not one of the last 3 in the column
            # can be diagonal (down to the right) if it can be both horizontal and vertical
            # can be diagonal (down to the left) if it can be vertical, and it isn't within the first 3 of the row

            if j < 17: # can be horizontal
                nums = grid[i][j:j+4]
                if math.prod(nums) > bestproduct:
                    bestnums = nums
                    bestproduct = math.prod(nums)
                    bestdir = 'Horizontal'
            if i < 17: # can be vertical
                nums = [grid[i+a][j] for a in range(4)]
                if math.prod(nums) > bestproduct:
                    bestnums = nums
                    bestproduct = math.prod(nums)
                    bestdir = 'Vertical'
            if j < 17 and i < 17: # can be down-right diagonal
                nums = [grid[i+a][j+a] for a in range(4)]
                if math.prod(nums) > bestproduct:
                    bestnums = nums
                    bestproduct = math.prod(nums)
                    bestdir = 'Diagonal'
            if j >= 3 and i < 17: # can be down-left diagonal
                # im reversing nums here to make it output the same result as the example (they must go in a different order in their code), but i dont think the order of the numbers necessarily matters
                nums = [grid[i+a][j-a] for a in range(4)][::-1] 
                if math.prod(nums) > bestproduct:
                    bestnums = nums
                    bestproduct = math.prod(nums)
                    bestdir = 'Diagonal'
    
    return f'{bestdir}: {" * ".join([str(a) for a in bestnums])} = {bestproduct}'


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