import traceback
import functools
import itertools
import cmath
import math
import collections
import re
import operator

# 2020 question 4
path = 'GeorgeGrammar/'
name = 'GeorgeGrammar'
failed_solution = ''

def separate(input):
    return input.splitlines()
    
def parse(case):
    # dont need to change the string to anything else
    return case

def solve(case):
    # strip non-alphabetical characters from case and put result in letters
    letters = [x for x in case if x.isalpha()]
    letters.sort() # sort the letters
    # loop through case. every time a non-alphabetical character is found, insert it where it belongs in letters
    for i in range(len(case)): 
        if not case[i].isalpha():
            letters.insert(i, case[i])
    # return both the input and the output. at this point letters is a list of chars, so it must be converted to a string with join
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
