import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Short Programming\PalIn.txt'
fout = './Short Programming\PalOut.txt'
open(fout, 'w').close()

def splitcases(x):
    x=x.strip('\n').split('\n')
    results = []
    while x:
        numsounds = int(x[0])
        sounds = x[1:numsounds+1:]
        x=x[numsounds+1:]
        numcases = int(x[0])
        cases = x[1:numcases+1:]
        x=x[numcases+1:]
        results.append((sounds,cases))
    return results


def solve(x, n):
    sounds,cases = x
    simil = {}
    for sound in sounds:
        if(sound[0] in simil):
            simil.append(sound[-1])
        else:
            simil[sound[0]]=[sound[-1]] 
        if(sound[-1] in simil):
            simil.append(sound[0])
        else:
            simil[sound[-1]]=[sound[0]]
    boolres = []
    for case in cases:
        pairs = [*zip(case,case[::-1])]
        pairs = pairs[:int(len(pairs)/2)]
        good = True
        for first,second in pairs:
            if first != second:
                if second not in simil.get(first, []):
                    good = False
                    break

        if(not good):
            boolres.append("NO")
        else:
            boolres.append("YES")
    results =f"Test case #{n+1}:"
    for i,case in enumerate(cases):
        results+=f"\n{case} {boolres[i]}"
    return results+"\n"
    

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