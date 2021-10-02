import traceback
import functools
import itertools
import cmath
import math
import collections
import re
import operator

# 2020 question 6
path = 'HopToIt/'
name = 'HopToit'
failed_solution = ''

def separate(input):
    return input.split('\n')
    
def parse(case):
    # convert case to integer
    return int(case)

def ispow(n):
    # determine if n is a power of 2
    while True:
        if n == 1: return True
        if n < 1: return False
        n /= 2

def solve(case):
    # if a pillar is a power of 2 and is in reach of the center, dr jones survives
    # when there are an even number of pillars, there are 2 pillars in reach of the center
    if case % 2 == 0:
        first = case // 2
        second = first + 1
        # determine if either of the pillars wont crumble. if one of them is safe, return it
        if ispow(first): return True, first
        elif ispow(second): return True, second
        # if neither pillar is safe, then dr jones dies testing the second pillar
        else: return False, second
    # with an odd number of pillars, there is only one pillar in reach of the center
    else:
        if ispow(case // 2 + 1): return True, case // 2 + 1
        else: return False, case // 2 + 1

def format(case):
    b, v = case
    # booleans print as 'True' and 'False', but the question wants lowercase answers so we have to convert them
    if b: B = 'true'
    else: B = 'false'
    return f'{B} - {v}'

def join(cases):
    return "\n".join(cases)

with open(path + name + 'In.txt') as input:
    solutions = list()
    for case in separate(input.read()):
        try:
            # parse, solve, and format the case
            tempsol = solve(parse(case))
            if tempsol:
                solution = format(tempsol)
            else:
                solution = failed_solution
        except Exception:
            # handle exception and print information
            solution = failed_solution
            print('Exception on case ' + str(case))
            if solution: print('Solution produced was ' + str(solution))
            print(traceback.format_exc())
        else:
            # print the solution if it was successful
            print(solution)
        solutions.append(solution) # store the solution
    with open(path + name + 'Out.txt', 'w') as output:
        # join the solutions and write them to the output file
        output.write(join(solutions)) 
