import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback

n = 'Word/Word'
fail = ''

def split(x):
    return x.strip('\n').split('\n')

def solve(x):
    words = x.split(' ')
    bestscore = 0
    bestword = ''
    for word in words:
        wordcopy = word
        wordcopy = list(map(ord, wordcopy))
        score = sum(wordcopy)
        # score = sum(map(ord, word))
        if score > bestscore:
            bestword = word
            bestscore = score
    return bestword

def join(x):
    return '\n'.join(x)

sols = list()
for case in split(open(n + 'In.txt').read()):
    try: sol = solve(case)
    except:
        print(str(case)[:100])
        print(traceback.format_exc())
        sol = fail
    print(sol)
    sols.append(sol)
    open(n + 'Out.txt', 'w').write(join(sols))