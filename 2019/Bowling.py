import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy, string

fin = './Long Programming\BowlingIn.txt'
fout = './Long Programming\BowlingOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')

def framesumnobonus(f, framenumber):
    if framenumber == 10:
        if len(f) == 4:
            if f[3] == 'X':
                return 40
            else:
                return 20 + int(f[3])
        else:
            newf = f.copy()
            for i, x in enumerate(f):
                if x == 'X':
                    newf[i] = 20
                elif x == '/':
                    newf[i] = 20 - int(f[i - 1])
            return sum(map(int, newf))
            
    if f[-1] == '/':
        return 20
    if len(f) == 1:
        return 20

    return sum(map(int, f))
    

def solve(x, n):
    x = x.split(' ')

    framecount = 1
    i = 0
    result = 0
    while i < len(x):
        roll = x[i]
        if roll == 'X':
            #strike
            f = [roll]
            nextrollidx = i + 1
        else:
            f = [x[i], x[i+1]]
            nextrollidx = i + 2
            
        if 10 <= framesumnobonus(f, 1) < 20:
            f.append(x[i + 2])
            nextrollidx = i + 3
        # all rolls added to frame
        s = framesumnobonus(f, 1)

        if framecount == 10:
            if f[-1] == 'X':
                f += [x[nextrollidx], x[nextrollidx + 1]]
            elif f[-1] == '/':
                f += [x[nextrollidx]]
            result += framesumnobonus(f, 10)
        else:
            # figure out bonuses for this frame
            nextroll = x[nextrollidx]
            if nextroll == 'X':
                nextroll = 20
            else:
                nextroll = int(nextroll)
            if f[-1] == '/':
                s += nextroll
            elif f[-1] == 'X':
                s += nextroll
                n2roll = x[nextrollidx + 1]
                if n2roll == 'X':
                    n2roll = 20
                elif n2roll == '/':
                    n2roll = 20 - nextroll
                else:
                    n2roll = int(n2roll)
                s += n2roll
            result += s
    

        framecount += 1
        i += len(f)

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