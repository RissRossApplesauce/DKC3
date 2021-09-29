import traceback
import functools
import itertools
import cmath
import math
import collections
import re
import operator

path = 'D:/'
name = 'HopToit'
failed_solution = ''

def separate(input):
    return input.split('\n')
    
def parse(case):
    return int(case)

def ispow(n):
    while True:
        if n == 1: return True
        if n < 1: return False
        n /= 2

def solve(case):
    if case % 2 == 0:
        first = case // 2
        second = first + 1
        if ispow(first): return True, first
        elif ispow(second): return True, second
        else: return False, second
    else:
        if ispow(case // 2 + 1): return True, case // 2 + 1
        else: return False, case // 2 + 1

def format(case):
    b, v = case
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
