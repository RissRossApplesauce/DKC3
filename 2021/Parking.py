import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Long Programming\\ParkingIn.txt'
fout = './Long Programming\\ParkingOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n*\n').split('\n*\n')
    
def solve(x, n):
    x = x.split('\n')
    cars = [int(a) for a in x[0].split(' ')]
    cars_unsorted = x[0].split(' ')
    leaving = [int(a) for a in x[1].split(' ')]

    cars.sort()
    cars = [(a, str(a)) for a in cars]

    parked = []

    for empty in leaving:
        i = len(cars) - 1
        while i >= 0:
            if cars[i][0] <= empty:
                break
            i -= 1
        else:
            i = len(cars) - 1
        
        spaces_moved = (empty + 30 - cars[i][0]) % 30

        parked.append((cars[i][1], empty))

        cars.pop(i)
        cars = [((car + spaces_moved) % 30, name) for car, name in cars]

    result = []

    for car, spot in parked:
        result.append(f'{car} parked in {spot}')

    strings = [c[1] for c in cars]
    for car in cars_unsorted:
        if car in strings:
            i = strings.index(car)
            result.append(f'{cars[i][1]} did not park')

    return '\n'.join(result)

for num, case in enumerate(splitcases(open(fin).read())):
    print(f'Case {num + 1}:')
    try:
        sol = str(solve(case, num))
        print(sol, '\n')
    except Exception:
        print(f'Input: "{case[:99]}"')
        print(traceback.format_exc())
        sol = ''
    open(fout, 'a').write(sol + '\n*\n')