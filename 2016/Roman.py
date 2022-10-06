import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\RomanIn.txt'
fout = './Short Programming\RomanOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    key = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    # first convert from roman numerals (with the potentially incorrect writing methods) to regular numbers
    # s will accumulate characters until we find out if we are doing subtraction/addition, then the operation will be done and s will reset
    s = ''
    value = 0
    bad = False # keep track of whether it is written wrong
    
    # c just means 'character', not 100
    for c in x:
        if not s:
            # s is empty, so just put the first character in
            s = c
        else:
            if key[c] > key[s[-1]]:
                # subtract value of s from value of c, assume s has all the same character
                # written incorrectly if s is more than 1 character long when subtracting
                if len(s) > 1:
                    bad = True
                else:
                    # there are restrictions on which values can be subtracted from others in valid roman numerals
                    canfollow = {
                        'I': ['V', 'X'],
                        'V': [],
                        'X': ['L', 'C'],
                        'L': [],
                        'C': ['M'],
                        'M': [],
                    }
                    if c not in canfollow[s]:
                        bad = True

                sval = key[s[0]] * len(s)
                value += key[c] - sval
                s = ''
            elif key[c] < key[s[-1]]:
                # c is smaller than previous character
                # add what's in s, then make s = c
                value += key[s[0]] * len(s)
                s = c
            else:
                # same character as what s has. just add it
                s += c
        
        # written incorrectly if s is ever 4 long, with the exception of using M's since there is nothing larger than M's
        if len(s) == 4 and s[0] != 'M':
            bad = True
    
    if len(s):
        value += len(s) * key[s[0]]
    
    # at this point, we know the value of the number, and whether it's written incorrectly

    if not bad:
        return value
    
    # we only reach this point if the roman numeral was written incorrectly
    # now write it correctly

    # terrible disgusting way to make roman numerals
    result = ''
    # get thousands
    result += 'M' * (value // 1000)
    value %= 1000
    # deal with values from 900-999
    if value >= 900:
        result += 'CM'
        value -= 900
    # 500-899
    if value >= 500:
        result += 'D'
        value -= 500
    # 400-499
    if value >= 400:
        result += 'CD'
        value -= 400
    # 100-399
    result += 'C' * (value // 100)
    value %= 100
    # 90-99
    if value >= 90:
        result += 'XC'
        value -= 90
    # 50-89
    if value >= 50:
        result += 'L'
        value -= 50
    # 40-49
    if value >= 40:
        result += 'XL'
        value -= 40
    # 10-39
    result += 'X' * (value // 10)
    value %= 10
    # 9
    if value == 9:
        result += 'IX'
        value -= 9
    # 5-8
    if value >= 5:
        result += 'V'
        value -= 5
    # 4
    if value == 4:
        result += 'IV'
        value -= 4
    # 1-3
    result += 'I' * value

    return result


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