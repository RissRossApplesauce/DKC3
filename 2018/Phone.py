import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\PhoneIn.txt'
fout = './Short Programming\PhoneOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
rules = [
    '',
    'double',
    'triple',
    'quadruple',
    'quintuple',
    'sextuple',#nice
    'septuple',
    'octuple',
    'nonuple',
    'decuple',
    ''
]

nums = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]

def solve(x, n):

    number, format = x.split(' ')
    format = format.split('-')
    cuts = []
    for size in format:
        size = int(size)
        cuts.append(number[:size])
        number = number[size:]

    words = []
    for cut in cuts:
        count = 0
        curnum = ''
        for c in cut:
            if not curnum:
                curnum = c

            if c == curnum:
                count += 1
            else:
                words.append(rules[count - 1])
                words.append(nums[int(curnum)])
                curnum = c
                count = 1
        words.append(rules[count - 1])
        words.append(nums[int(curnum)])
    
    words = [w for w in words if w]

    return f'Case #{n + 1}: ' + ' '.join(words)

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