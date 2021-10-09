import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback, copy

n = 'One copy/One'
fail = ''

def split(x):
    return x.strip('\n').split('\n')

def getcoeffs(s):
    vars = [0] * 6
    regexes = [r'(-?\d+)?x\^2', r'(-?\d+)?xy', r'(-?\d+)?y\^2', r'(-?\d+)?x(?![xy^])', r'(-?\d+)?y(?![xy^])', r'(?<!\^)(-?\d+)(?:=)']

    for i, regex in enumerate(regexes):
        match = re.search(regex, s)
        if not match:
            vars[i] = 0
        elif match.group(1):
            vars[i] = int(match.group(1))
        else:
            gs = match.groups()
            vars[i] = 1



    return vars

def diffsigns(x, y):
    if x < 0 and y > 0: return True
    elif x > 0 and y < 0: return True
    else: return False



def solve(x):
    cs = getcoeffs(x)
    if cs[0] == cs[2] and cs[1] == 0:
        #circle
        pass
    elif not diffsigns(cs[0], cs[2]) and cs[1] == 0:
        #ellipse
        pass
    elif (cs[0] == 0 or cs[2] == 0) and cs[1] == 0:
        # parabola
        pass
    else:
        # hyperbola
        pass








    return x

def join(x):
    return '\n'.join(x)

sols = list()
for case in split(open(n + 'In.txt').read()):
    try: sol = solve(case)
    except:
        print(str(case[:100]))
        print(traceback.format_exc())
        sol = fail
    print(sol)
    sols.append(sol)
    open(n + 'Out.txt', 'w').write(join(sols))
    it.permutations(it.chain.from_iterable(['A', 'L', 'O'] * 4), 4)