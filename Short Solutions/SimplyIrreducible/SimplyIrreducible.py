import traceback
import functools
import itertools
import cmath
import math
import collections
import re
import operator

path = 'D:/'
name = 'SimplyIrreducible'
failed_solution = ''

def separate(input):
    return input.split('*\n')
    
def parse(case):
    return int(case)

def solve(case):
    fracs = list()
    for x in range(1, 100):
        for y in range(1, 100):
            if (x / y) < case and fracs.count(x / y) == 0:
                fracs.append(x / y)
    return sum(fracs)

def format(case):
    return f'{case:.3f}' + '\n*'

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
