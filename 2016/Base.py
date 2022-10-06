import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\BaseIn.txt'
fout = './Short Programming\BaseOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    x = x.split('\t')
    num = x[0]
    b1 = int(x[1])
    b2 = int(x[2])
    # easy to load from any base. i tested this and it works through base 36, so we should be good to use it
    num = int(num, base=b1)
    # cant use f-strings because they only work on base 2, 8, 10, and 16
    # break up the digits using integer division and modulo
    digits = []
    while num // b2:
        digits.append(num % b2)
        num //= b2
    digits.append(num)
    digits = digits[::-1]
    # now we have our digits, but the digits themselves arent in the correct base (just decimal numbers stored in a list). now convert them to the correct base

    def convert(digit):
        if digit < 10: # if theyre 0-9, they can stay the same
            return str(digit)
        else: # convert 11-35 to correct ascii values, then use chr() to convert from ascii to string
            return chr(65 + digit - 10)

    digits = [convert(digit) for digit in digits]
    
    return ''.join(digits)

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