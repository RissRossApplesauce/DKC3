# create multi-dimensional array. use nested list comprehension for more dimensions
# note that the cols and rows are used in reverse order when creating the array. this makes it so indexing is in forward order, aka a[col][row]


cols = 5
rows = 3
a = [[0] * rows for _ in range(cols)]

for col in range(cols):
    for row in range(rows):
        a[col][row]

# for 3 dimensions
xlen = 3
ylen = 10
zlen = 2
b = [[[0] * zlen for _ in range(ylen)] for _ in range(xlen)]

for x in range(xlen):
    for y in range(ylen):
        for z in range(zlen):
            b[x][y][z]





# comparison function with multiple conditions
# make helpers for each rule

# generic helper that just applies greater than/less than
def order(a, b): return -1 if a < b else a > b

# default char comparison puts numbers first, so this might be useful
# if we have a function that checks for a condition, put a - sign to make that condition come FIRST. no - sign will make it go LAST
# if order is defined, we might be able to get away with a lambda function since this is a one-liner anyway
def numslast(a, b):
    return order(a.isnumeric(), b.isnumeric())

def symbolslast(a, b):
    return order(not a.isalnum(), not b.isalnum())

# put z at the beginning, just for fun
def zfirst(a, b):
    # - sign because we want it first
    return -order(a == 'z', b == 'z')

# put comparisons in order of importance (if one rule should override another, its more important)
# here, we make sure numbers are last, symbols are 2nd last, letter z is first, then sort the rest with standard gt/lt
def compare(a, b):
    for comp in [numslast, symbolslast, zfirst, order]:
        r = comp(a, b)
        if r: return r
    return 0






# quick local classes to organize things easily. replaces arrays of data in cases where they are used frequently
class person: pass
# you dont need to define anything inside the class, just give it a name
ross = person()
ross.name = 'Ross'
ross.age = 21
keegan = person()
keegan.name = 'Keegan'

# instance variables can still be compared
if ross.name == keegan.name: print("same name")

# this will crash because keegan.age is undefined
# this problem should be easy to avoid, just fully define everyones variables from the start
# if ross.age > keegan.age: print("older")






# finding the best path
# depth first search with some rules
def solve(x):
    bestpath = []
    
    # generate possible next moves given the path so far
    def posmoves(path):
        pass

    # determine if path is better than bestpath. assumes isdone(path) == True
    # this example says a shorter path is better, however, if bestpath is empty, anything is better
    def isbest(path):
        return len(path) < len(bestpath) if bestpath else True

    # path has reached its goal (such as getting to the target city)
    def isdone(path):
        pass

    # path has failed (can't possibly replace bestpath)
    # dont need to check for dead ends
    def isfailed(path):
        pass

    def findpath(path):
        for move in posmoves(path):
            newpath = path.copy()
            newpath.append(move)
            if isfailed(newpath): return
            elif isdone(newpath): # what if the best path comes farther along this path?
                # to correct this, this code path must recurse and isfailed becomes necessary
                if isbest(newpath):
                    nonlocal bestpath
                    bestpath = newpath
            else:
                findpath(newpath)

    # non-recursive findpath
    def newfindpath(path):
        nonlocal bestpath
        stack = [(path, posmoves(path))]
        while stack:
            newpath = stack[-1][0]
            moves = stack[-1][1]
            if isfailed(newpath):
                stack.pop(-1)
                continue
            # the isfailed check may not always be necessary if isdone has pop and continue uncommented
            if isdone(newpath):
                if isbest(newpath): bestpath = newpath 
                # stack.pop(-1)
                # continue
                # only uncomment above 2 lines if a better path cant be an extension of the current bestpath
            if not moves:
                stack.pop(-1)
            else:
                nextpath = newpath.copy()
                nextpath.append(moves.pop(0))
                stack.append((nextpath, posmoves(nextpath)))

    findpath('[path start location]')




# prime number generator stolen off the internet. note this returns an infinite generator if no n is given. loop over it (with a break condition) or call next() to get values out of it
def primes(n = -1):
    D = {}
    q = 2
    while True:
        if n == 0: return
        p = D.pop(q, None)
        if p:
            x = p + q
            while x in D: x += p
            D[x] = p
        else:
            D[q*q] = q
            yield q
            n -= 1
        q += 1
            


# test for a prime number, also stolen
def isprime(n):
    if n < 2: return False
    if n < 4: return True
    if not n % 2: return False
    if not n % 3: return False
    i = 5
    w = 2
    while i * i <= n:
        if not n % i:
            return False
        i += w
        w = 6 - w
    return True