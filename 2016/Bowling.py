import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\BowlingIn.txt'
fout = './Short Programming\BowlingOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    x = [int(b) for b in x.split(',')]
    framecount = x[0]
    pins = x[1]
    rolls = x[2:]
    
    # the first step is to convert the list of rolls into a list of frames
    frames = []
    i = 0
    while i < len(rolls):
        if len(frames) == framecount:
            # final frame. the code only gets here if they got a strike/spare, giving them extra rolls for the last frame
            # now add the last 1 or 2 rolls to the frame
            first, second = frames[-1]
            if (first == pins):
                # got a strike in first roll. they get 2 more rolls
                frames[-1] = (first, rolls[i], rolls[i + 1])
            else:
                # got a spare. add 1 more roll
                frames[-1] = (first, second, rolls[i])

            # done
            break
        else:
            if rolls[i] == pins:
                # strike. only put 1 roll in this frame
                frames.append((pins, 0))
            else:
                # not a strike. put the next 2 rolls into this frame
                frames.append((rolls[i], rolls[i + 1]))
                i += 1
            i += 1

    # now sum up the scores
    scores = []
    for i, frame in enumerate(frames):
        if i == framecount - 1:
            # last frame. there is no special scoring for strikes/spares, just add up the values
            scores.append(sum(frame))
            break
        if frame[0] == pins:
            # they got a strike. add up the next 2 rolls to the score
            nextroll = frames[i + 1][0]
            if nextroll == pins:
                # next roll is also a strike
                if (i + 1 == framecount - 1):
                    # next frame is final frame. just get the second roll from that frame
                    next2 = frames[i + 1][1]
                else:
                    # next frame is normal, so go 1 frame further
                    next2 = frames[i + 2][0]
            else:
                # next roll isnt a strike. get the second roll from the frame
                next2 = frames[i + 1][1]
            scores.append(frame[0] + nextroll + next2)
        elif sum(frame) == pins:
            # spare. add the score of the next roll
            nextroll = frames[i + 1][0]
            scores.append(sum(frame) + nextroll)
        else:
            # no special points
            scores.append(sum(frame))

    return sum(scores)

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