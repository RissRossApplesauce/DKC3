import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\FranksFlapjacksIn.txt'
fout = './Short Programming\FranksFlapjacksOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')

# create a dataclass (like a struct in c/c++) to keep track of info about pancakes
from dataclasses import dataclass
@dataclass
class pancake:
    butter: bool
    almond: bool
    choc: bool
    blue: bool
    bacon: bool

# checks if a pancake is consistent with the rules about mixing ingredients
def consistent(p: pancake):
    return (
        all([
            # requirements
            sum([p.almond, p.butter]) == 1,
            sum([p.choc, p.blue, p.bacon]) >= 1,
        ])
        and not any([
            # failure conditions
            p.almond and p.bacon,
            p.blue and p.bacon,
        ])
    )
    

# generate a list of all possible pancake mixes, then filter out the ones that break the rules
# this is global because it's the same for each case
pancakes = [*filter(consistent,
    [pancake(*args) for args in it.product((0, 1), repeat=5)]
)]

def solve(x, n):
    flour, butter, almond, choc, blue, bacon = map(int, x.split(' '))
    results = []
    
    # given a list of pancakes that were already made, return a list of pancakes that can still be made
    def options(c):
        nonlocal flour, butter, almond, choc, blue, bacon
        
        # get remaining amounts of each ingredient
        # if theres no flour, no pancakes can be made
        rflour = flour - len(c)
        if rflour == 0:
            return []
        
        rbutter = butter - sum([p.butter for p in c])
        ralmond = almond - sum([p.almond for p in c])
        rchoc = choc - sum([p.choc for p in c])
        rblue = blue - sum([p.blue for p in c])
        rbacon = bacon - sum([p.bacon for p in c])
        
        # filter out any pancakes that can't be made with the remaining ingredients
        options = [*filter(
            lambda p:
                rbutter >= p.butter
                and ralmond >= p.almond
                and rchoc >= p.choc
                and rblue >= p.blue
                and rbacon >= p.bacon,
            pancakes
        )]
        
        return options
        
    def brute(c):
        # see what pancakes can be made
        ops = options(c)
        # we are done with the ingredients when we can't make any more pancakes
        if len(ops) == 0:
            nonlocal results
            results.append(c) 
        for op in ops:
            brute(c + [op])
    
    # run the brute force method, initialized with an empty list
    brute([])
    
    def price(p):
        return (
            p.butter * 2
            + p.almond * 3
            + p.choc
            + p.blue * 2
            + p.bacon * 3
        )
    
    # for each result of the brute force method, add up the price of all the pancakes. take the max price of any result and return it
    return max([
        sum(map(price, result))
        for result in results
    ])

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