import traceback
import functools
import itertools
import cmath
import math
import collections
import re
import operator

# 2020 question 7
path = 'ComboLogic/'
name = 'ComboLogic'
failed_solution = ''

def separate(input):
    return input.split('\n')
    
def parse(case):
    # convert case into a list of ints
    return list(map(lambda x: int(x), case.split(' ')))

def solve(case):
    # do math for both parts of the question. convert b to int because the question wants 0 or 1, not 'true' or 'false'
    b = int((not case[0] and case[1]) or (case[2] and case[3]) or (case[4] and not case[5]))
    f = (not case[0]) + case[2] + case[4] + (case[1] + case[3] + (not case[5])) / 10
    return b, f

def format(case):
    b, f = case
    # use formatted string to convert to a string and truncate to one decimal place
    return f'{b} - {f:.1f}'

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
