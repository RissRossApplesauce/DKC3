import traceback, functools, itertools, cmath, math, collections, re, operator

# 2016 problem 4
n = 'Anagram/Anagram'
fail = ''

def split(x):
    return x.split('\n\n')

def parse(x):
    # separate case into individual lines. r is a meaningless name
    r = x.split('\n')
    # for each line l in r, apply the list comprehension in square brackets
    # the list comprehension keeps only alphabetical characters and then converts those to lowercase
    return list(map(lambda l: [char.lower() for char in list(l) if char.isalpha()], r))

def solve(x):
    # x is a list of lines
    # sort each line in x. if two lines are an anagram, they should now be the exact same (same letters and same order)
    x = list(map(lambda l: sorted(l), x))
    # the loops here are mainly so we dont count the same anagram twice
    # we originally had for loops, but the range() iterator is only calculated once and we needed i < len(x) to be re-calculated every time x is changed or we get index out of bound errors
    count = 0
    i = j = 0
    while i < len(x):
        j = i + 1
        while j < len(x):
            # if x[i] and x[j] are anagrams
            if x[i] == x[j]:
                # add 1 to the count
                count += 1
                # list comprehension that gets rid of all lines from x that are anagrams of x[i]
                x = [l for l in x if l != x[i]]
                # reset i and j to 0 because we have removed some values from x and need to start at the beginning
                i = j = 0
    return count

def format(x):
    return str(x)

def join(x):
    return '\n'.join(x)
    
sols = list()
for case in split(open(n + 'In.txt').read()):
    try:
        temp = solve(parse(case))
        sol = (format(temp), fail)[temp == None]
    except:
        print('Err on ' + str(case))
        print(traceback.format_exc())
        sol = fail
    else:
        print(sol)
    sols.append(sol)
open(n + 'Out.txt', 'w').write(join(sols))