"""
General brute-force algorithm.
"""

def solve(x):
    results = []
    
    # test if the combination is a valid solution
    def accept(c):
        pass

    # get a list of every variable that we can append to c
    def options(c):
        o = []
        return o
    
    # test if the combination should be rejected
    # optional. not all problems work out so you can reject combinations early
    def reject(c):
        pass

    def backtrack(c):
        if reject(c):
            return
        if accept(c):
            # found a valid combination
            nonlocal results
            results.append(c)
            return
        for o in options(c):
            backtrack(o)
    
    # the initial input should be an empty list
    backtrack([])

    return results