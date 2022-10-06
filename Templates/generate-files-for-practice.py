# does everything to get a new year's directory ready for practice
# this will overwrite files that already exist with the same name

# 4 things before running:
# create a directory with the year that you are practicing from and put this file in it
# make sure you are running this file from the correct year's directory or you will just make a mess
# make sure the string with the template file copied into it is up to date
# also make sure you update short_names and long_names to match the year's problem files
#   - for example, the 2016 problem "Lack of Funding" expects files named FundingIn.txt and FundingOut.txt,
#   - so you would put 'Funding' (no need for the In/Out.txt part) in long_names to have them generated
#   - just put all of the files 

short_problem_names = [
    'Budget',
    'Color',
    'Counting',
    'Divisibility',
    'ECIAComplaint',
    'Fibonacci',
    'Fold',
    'Multiples',
    'OrderOp',
    'Pal',
    'Parlez',
    'Repeat',
    'Sudoku',
    'Wax',
    'Ziggity',
]

long_problem_names = [
    'Bunny',
    'Mars',
    'Molkky',
    'QRCode',
]

template = """
import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = 'NAMEIn.txt'
fout = 'NAMEOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\\n').split('\\n')
    
def solve(x, n):
    return x

for num, case in enumerate(splitcases(open(fin).read())):
    print(f'Case {num + 1}:')
    try:
        sol = str(solve(case, num))
        print(sol, '\\n')
    except Exception:
        print(f'Input: "{case[:99]}"')
        print(traceback.format_exc())
        sol = ''
    open(fout, 'a').write(sol + '\\n')
"""

import os
try:
    os.mkdir(os.path.join(os.getcwd(), 'Short Programming'))
    os.mkdir(os.path.join(os.getcwd(), 'Long Programming'))
except FileExistsError:
    pass

for name in short_problem_names:
    open('Short Programming/' + name + 'In.txt', 'w')
    open(name + '.py', 'w').write(template.replace('NAME', './Short Programming/' + name))

for name in long_problem_names:
    open('Long Programming/' + name + 'In.txt', 'w')
    open(name + '.py', 'w').write(template.replace('NAME', './Long Programming/' + name))