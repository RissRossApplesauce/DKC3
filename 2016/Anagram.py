import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy
import string

fin = './Short Programming\AnagramIn.txt'
fout = './Short Programming\AnagramOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n\n').split('\n\n')
    
def solve(x, n):
    # this is the original solution we came up with, but there is an easier one called bettersolve(x, n) below
    x = x.strip('\n').split('\n')
    unique = 0
    
    counters = []
    # use collections.Counter to count up all of the letters, after filtering out all of the non-letter characters
    for sentence in x:
        sentence = str([letter for letter in sentence if letter.isalpha()]).lower()
        c = co.Counter(sentence)
        counters.append(c)
    
    # this loop looks through the counters and counts up the duplicated sentences. it adds to unique every time it finds an anagram
    while len(counters) > 1:
        number = 0
        j = 1
        while j < len(counters):
            if counters[0] == counters[j]:
                number += 1
                counters.pop(j)
                j -=1
            j += 1
        if number > 0:
            unique += 1
        counters.pop(0)
    
    return unique

def bettersolve(x, n):
    # in the original solution, we used a counter to see how many of each letter a sentence had. that way, we were able to see if sentence were equivalent
    # in this solution, we just sort the sentences alphabetically. if they were anagrams before, theyre the exact same now
    x = x.strip('\n').split('\n')
    
    # for every sentence:
    # convert to lowercase and filter away non-alphabetical characters.
    # then sort and convert back to a string
    cleaned = []
    for sentence in x:
        alpha = filter(lambda x: x.isalpha(), sentence.lower())
        cleaned.append(str(sorted(alpha)))
        
    # count unique sentences
    counter = co.Counter(cleaned)
    
    # count up the number of sentences that had 2 or more duplicates
    return len(list(
        filter(
            lambda x: x[1] >= 2,
            counter.most_common()
        )
    ))

for num, case in enumerate(splitcases(open(fin).read())):
    print(f'Case {num + 1}:')
    try:
        sol = str(bettersolve(case, num))
        print(sol, '\n')
    except Exception:
        print(f'Input: "{case[:99]}"')
        print(traceback.format_exc())
        sol = ''
    open(fout, 'a').write(sol + '\n')