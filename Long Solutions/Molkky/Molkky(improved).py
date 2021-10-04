import traceback, functools, itertools, cmath, math, collections, re, operator

# changed the data type of players list from a list of numbers to a custom class
# replaced sorting with better version
# cleaned up split and parse to make more sense
n = './Molkky\Molkky'
fail = ''


def split(x):
    # when the case delimiter is more than just \n, strip it off
    x = x.strip('\n*')
    splitidx = x.index('\n')
    # take the cases, ignoring the first line (number of games isnt necessary)
    x = x[splitidx + 1:]
    # separate cases by the delimiter
    return x.split('\n**')

def parse(x):
    # split lines before trying to 
    x = x.splitlines()
    playercount = int(x[0])
    moves = x[1:]
    for i in range(len(x)):
        # remove comments
        moves[i] = moves[i].split('**')[0].strip()
        # convert info to list of ints
        moves[i] = list(map(int, moves[i].split(' ')))
        # organize the data (player number, then list of pins hit)
        moves[i] = [moves[i][0], moves[i][1:]]

    return playercount, moves

def solve(x):
    playercount, moves = x
    class cplayer: pass
    players = list()
    for i in range(playercount):
        player = cplayer()
        player.num = i + 1
        player.score = 0
        player.misses = 0
        player.lost = 0
        players.append(player)
    winner = -1

    for move in moves:
        playeridx = move[0] - 1
        if not players[playeridx].lost:
            pins = len(move[1])
            if players[playeridx].lost:
                continue
            
            if len(move[1]) == 0:
                players[playeridx].misses += 1
            elif pins == 1:
                players[playeridx].score += move[1][0]
                players[playeridx].misses = 0
            else:
                players[playeridx].score += pins
                players[playeridx].misses = 0
            
            if players[playeridx].score > 50:
                players[playeridx].score = 25
            
            if players[playeridx].score == 50:
                winner = players[playeridx].num

            if players[playeridx].misses == 3:
                players[playeridx].lost = 1
            
    return winner, players

# uses the better sorting solution in notes.py
# losers last, then sort by score
def order(a, b): return -1 if a < b else a > b

def loserslast(a, b):
    return order(a.lost, b.lost)

def scorefirst(a, b):
    return -order(a.score, b.score)

def mycmp(a, b):
    for comp in [loserslast, scorefirst]:
        r = comp(a, b)
        if r: return r
    return 0

gamenum = 0

def format(x):
    winner, players = x
    global gamenum
    gamenum += 1
    
    players.sort(key = functools.cmp_to_key(mycmp))
    
    result = f'{gamenum}'
    for player in players:
        result += f' ({player.num},{"-" if player.lost else ""}{player.score})'
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