import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\FridayIn.txt'
fout = './Short Programming\FridayOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    """
    this doesnt match the answers given in the examples at all, but i checked by counting off a list of friday 13th's and this is correct, not the examples
    the example for 2010-2012 is missing the 3 friday 13ths from the year 2012, so the total should be 5
    there are similar issues for the other examples
    """

    x = x.split(' ')
    start = int(x[0])
    stop = int(x[1])

    # the problem with this question is that it hardly gives you enough information to work with
    # it assumes you already know how to determine the day of the week given a month/date/year
    # this is an algorithm off of the internet, but in the competition we just wouldnt touch this problem unless we had the algorithm available
    # https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
    def friday13count(year):
        count = 0
        for m in range(1, 13):
            # for some odd reason, m = 1 corresponds to march in this algorithm
            # january and february are 11 and 12, and must be treated like they are from the year prior
            y = year - 1 if m > 10 else year
            Y = y % 100 # year
            C = y // 100 # century
            k = 13 # day of the month. always 13
            W = (k + math.floor(2.6*m - 0.2) - (2 * C) + Y + (Y // 4) + (C // 4)) % 7
            if (W == 5): # 0 = sunday, 1 = monday, ... 5 = friday, 6 = saturday
                count += 1
        return count
    
    result = 0
    for year in range(start, stop + 1):
        result += friday13count(year)

    return result

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