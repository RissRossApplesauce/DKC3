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
def order(a, b):
    return -1 if a < b else a > b

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