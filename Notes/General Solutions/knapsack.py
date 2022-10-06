import math, itertools as it

def knapsack(items, capacity, bad, best, infinite):
    # initialize dynamic programming matrix
    m = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]
    for i in range(1, capacity + 1):
        m[0][i] = bad
        
    for i, item in enumerate(items, 1):
        for c in range(1, capacity + 1):
            # i is an index corresponding to each item type, c is the capcity of the subproblem that the entry m[i][c] corresponds to
            old_value = m[i - 1][c]
            potential_value = bad
            
            if c >= item.weight: # is it possible to fit the item in the knapsack, for this specific sub-problem
                potential_value = m[i - 1 + bool(infinite)][c - item.weight] + item.value
            
            m[i][c] = best(potential_value, old_value)
    
    return m[-1][-1]

# To choose the parameters 'bad', 'best', and 'infinite':
#   is it allowed to partially fill the knapsack?
#       yes: 0
#       no: +/- math.inf (if you choose max in the next step, do -math.inf. if you choose min, do +math.inf)
#   are you maximizing the value?
#       yes: max
#       no: min
#   do your items run out?
#       yes: False
#       no: True
#
# explanation:
# bad - a value to represent the worst case (-math.inf, 0, or math.inf), such as not being able to fit anything in the knapsack
    # if bad is +/- math.inf, it forces the solution to entirely fill the knapsack. if there is no solution that entirely fills the knapsack, +/- math.inf is returned
# best - a function (min or max) that decides which value is 'better' than the other
# infinite - a bool (True or False) that tells whether the items being taken are limited or unlimited

# EXAMPLES:
from dataclasses import dataclass
@dataclass
class item():
    weight: int
    value: int

### Integer Knapsack Problem, Unlimited Items:
# the bag doesn't need to be filled entirely (bad == 0)
# maximize profit (best is max)
# items are infinite (infinite == True)
items = [
    item(weight, profit)
    for weight, profit in
    [(2, 3), (3, 4), (4, 1)]
]
print(items)
print(knapsack(items, 9, 0, max, True))

### Integer Knapsack Problem, Limited Items
# same as above, but infinite == False
# to tell the knapsack solver there are <n> of some type of item, put <n> copies of the item in the input
# the way items2 is constructed below makes it easy to programmatically create n copies of an item
items2 = [*it.chain.from_iterable(
    [
        [item(weight, profit)] * count
        for weight, profit, count in
        [(2, 3, 2), (3, 4, 3), (4, 1, 2)]
    ]
)]
print(items2)
print(knapsack(items, 9, 0, max, False))


# change-making problem: finding the minimum number of coins to make change for a value
# this uses some unusual tricks to make it work. the "value" of each coin is 1. that means if we have a pile of coins, the "value" of the pile is just how many coins there are
# the "weight" of the coins is how many cents they are worth
# we want to minimize the number of coins, so we minimize the value
# we also will only accept exact change. if we cant make change with the coins available, an error value should be returned (the error value is math.inf)
# in this example, we have infinite of each type of coin, but that isn't necessary
# as a result, the inputs are bad = math.inf, best = min, and infinite=True
@dataclass
class coin():
    weight: int
    value: int = 1

coins = [
    coin(cents)
    for cents in
    [1, 5, 10, 25]
]
print(coins)
print(knapsack(coins, 31, math.inf, min, True))