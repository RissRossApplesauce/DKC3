import traceback, functools, itertools, cmath, math, collections, re, operator

# took 1:10:00
n = './2017\Molkky'
fail = ''

games = 0
mynum = 0

# had issues stripping newlines and spaces from outside
def split(x):
    x = x.strip('\n**')
    splitidx = x.index('\n')
    global games
    games = int(x[:splitidx])
    x = x[splitidx + 1:]
    return x.split('\n**')

# had issues stripping newlines and spaces from outside
def parse(x):
    x = x.strip('\n')
    splitidx = x.index('\n')
    # didnt use correct indices originally
    players = int(x[:splitidx])
    x = x[splitidx + 1:]
    x = x.split('\n')
    for i in range(len(x)):
        x[i] = x[i].split('**')[0].strip(' \n')
        x[i] = list(map(lambda a: int(a), x[i].split(' ')))
        if len(x[i]):
            x[i] = [x[i][0], x[i][1:]]
        else:
            x[i] = [x[i][0], []]

    return players, x

def solve(x):
    pnum, moves = x
    # had problems with creating 2d array again
    players = list()
    for i in range(pnum):
        players.append([i + 1, 0, 0, 0])
    winner = -1

    # 0number, 1score, 2misses, 3lost
    for move in moves:
        thispnum = move[0] - 1
        if not players[thispnum][3]:
            length = len(move[1])
            if players[thispnum][3]:
                continue
            if len(move[1]) == 0:
                players[thispnum][2] += 1
            elif length == 1:
                players[thispnum][1] += move[1][0]
                players[thispnum][2] = 0
            else:
                players[thispnum][1] += length
                players[thispnum][2] = 0
            
            if players[thispnum][1] > 50:
                players[thispnum][1] = 25
            
            if players[thispnum][1] == 50:
                winner = players[thispnum][0]

            if players[thispnum][2] == 3:
                players[thispnum][3] = 1
            
    return winner, players

# research a better way to make sort comparisons
def mycmp(a, b):
    if a[3] and b[3]:
        if a[1] == b[1]: return 0
        else:
            if a[1] > b[1]: return -1
            else: return 1
    if a[3]: return 1
    if b[3]: return -1
    
    if a[1] == b[1]: return 0
    else:
        if a[1] > b[1]: return -1
        else: return 1

def format(x):
    global mynum
    global games
    mynum += 1
    winner, players = x
    players.sort(key = functools.cmp_to_key(mycmp))
    result = f'{mynum}'
    for player in players:
        minus = '-'
        empty = ''
        result += f' ({player[0]},{minus if player[3] else empty}{player[1]})'
    if winner == -1:
        result += ' X'
    else:
        result += f' {winner}'
    
    return result

def join(x):
    return '\n'.join(x)
    
sols = list()
for case in split(open(n + 'In.txt').read()):
    try:
        temp = solve(parse(case))
        sol = format(temp) if temp else fail
    except:
        print('Err on ' + str(case))
        print(traceback.format_exc())
        sol = fail
    else:
        print(sol)
    sols.append(sol)
    open(n + 'Out.txt', 'w').write(join(sols))