import traceback
import functools
import itertools
import cmath
import math
import collections
import re
import operator

path = 'D:/'
name = 'GeorgeGrammar'
failed_solution = ''

def separate(input):
    return input.splitlines()
    
def parse(case):
    return case

def solve(case):
    letters = [x for x in case if x.isalpha()]
    letters.sort()
    for i in range(len(case)):
        if not case[i].isalpha():
            letters.insert(i, case[i])
    return (case, ''.join(letters))


def format(case):
    first, last = case
    return first + '\n' + last
    
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
