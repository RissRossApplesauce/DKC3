import functools as ft, itertools as it, operator as op, cmath, math, collections, re, traceback, copy

n = 'Password/Password'
fail = ''

def split(x):
    return x.strip('\n').split('\n')

# need to use search, not match
def isacceptable(x):
    return (not re.search(r'[^A-Za-z\d~!@#\$%\^\&\*()\-_\+=\?/]', x)) and len(x) >= 8 and len(x) <= 32 and re.search(r'[A-Z]', x) and re.search(r'[a-z]', x) and re.search(r'\d', x) and re.search(r'[~!@#\$%\^&\*()\-_\+=\?/]', x)


def solve(x):
    res = list()
    na = 0
    for p in x.split(' '):
        if isacceptable(p):
            res.append(p)
        else:
            na += 1
    
    if res:
        return ' '.join(res)
    else:
        return f'No acceptable passwords found! {na}'

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