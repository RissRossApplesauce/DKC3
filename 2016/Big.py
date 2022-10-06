import functools as ft, itertools as it, operator as op, collections as co, cmath, math, re, traceback, copy

fin = './Short Programming\BigIn.txt'
fout = './Short Programming\BigOut.txt'
open(fout, 'w').close()

def splitcases(x):
    return x.strip('\n').split('\n')
    
def solve(x, n):
    # 
    x = x.split(', ')
    target = int(x[2])
    
    # pad the numbers with leading zeros. note that they are still stored as strings
    l1 = len(x[0])
    l2 = len(x[1])
    l = max(l1, l2) # number of digits on the largest card
    x[0] = x[0].zfill(l)
    x[1] = x[1].zfill(l)

    # counting in binary covers every possible combinations of 1's and 0's, so we used this to represent every possible combination of cut/no cut
    # for example, the number 110 would cut a card like this: X|X|XX - where the X's are the digits on the card
    # to do this, we count all the way up to the number that would represent doing every single cut: 2^(l - 1) - 1
    stop = 2 ** (l - 1)
    best = 0
    
    # the range starts at the highest value and goes backwards.
    # this is because we are more likely to find a solution with higher numbers (higher => more cuts => smaller sum => closer to desired output)
    for i in range(stop - 1, 0, -1):
        # convert i to a string, written in binary. pad with leading zeros so it is consistent length
        s = f'{i:b}'.zfill(l - 1)
        # convert to array of booleans
        cuts = [bool(int(x)) for x in list(s)]
        # add one last cut to the end. this is just a hacky way to make the loop below output the last number (it only outputs numbers when it does a cut)
        cuts.append(True)
        pairs = []
        lastcut = 0
        bad = False
        # create a list of pairs. each pair respresent a piece that was cut off. the first value is the front of the piece, the second value is the back of the piece
        for n, cut in enumerate(cuts, 1): # you can set the initial value for enumerate
            if cut:
                pairs.append((int(x[0][lastcut:n]), int(x[1][l - n:l - lastcut])))
                lastcut = n
                # here is an optimization:
                # if the numbers on both sides of this piece are larger than the desired result, it's impossible for this cutting pattern to give us a sum <= the desired result
                # so we just go to the next cutting pattern
                if int(pairs[-1][0]) > target and int(pairs[-1][1]) > target:
                    # use a flag because we have to break out of 2x nested loops
                    bad = True
                    break
        if bad: continue
        
        # at this point, pairs is a list of all the pieces the card was cut into
        # using the same binary counting trick as we used with the cuts, we go through every possible combination of pieces to add together
        for b in range(0, 2 ** (len(pairs))):
            # binary number for the binary counting trick
            bstring = f'{b:b}'.zfill(len(pairs))
            blist = [bool(int(x)) for x in list(bstring)]
            sum = 0
            
            # add up the pieces by looping over the pairs and choosing which side to use based on the binary numbers in blist
            # since the values are in pair[0] and pair[1], we can use the bits of the binary number as list indices
            # this is a faster way of typing:
            # if b: sum += pair[1]
            # else: sum += pair[0]
            for b, pair in zip(blist, pairs):
                sum += pair[b]
                
            # if a sum is found that is better than the best one we've found so far, save it
            if sum < target:
                if sum > best:
                    best = sum
            
            # if we get the target as a sum, were done. return the sum
            elif sum == target:
                return target

    return best


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