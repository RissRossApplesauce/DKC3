"""
General brute-force algorithms.
You can optionally define a reject() method that allows for the backtracking optimization.
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
    
    # rather than returning a list, some situations can work with a generator
    # use a generator to prevent creating more values than needed
    # it is also possible to use a generator to avoid making copies (see 2017 sudoku)
    # be careful using this option with breadth-first searches. understand the difference between copy and deep copy
    def genoptions(c):
        o = c
        yield o
    
    # test if the combination should be rejected
    # optional. not all problems work out so you can reject combinations early
    def reject(c):
        pass
    
    # depth first search
    def dfs(c):
        # optional for backtracking
        # if reject(c):
        #     return
        if accept(c):
            # found a valid combination
            nonlocal results
            results.append(c)
            return
        for o in options(c):
            dfs(o)
            
        # if you want to stop as soon as a result is found:
        # 
        # if accept(c):
        #     nonlocal results
        #     results.append(c)
        #     return True
        # for o in options(c):
        #     if dfs(o):
        #         return True
    
    # breadth first search
    def bfs(c):
        # track explored combinations in a list
        e = []
        e.append(c)
        
        # queue to hold new combinations to test
        import collections as co
        q = co.deque()
        q.append(c)
        
        # main loop. runs until everything has been explored, or a result is accepted
        while q:
            cur_c = q.pop(0)
            if accept(cur_c):
                nonlocal results
                results.append(cur_c)
                # you can simply return here if you only want one solution.
                # you don't need to do extra work like in dfs
            for new_c in options(cur_c):
                if new_c not in e:
                    e.append(new_c)
                    q.append(new_c)
    
    # the initial input should be an empty list
    dfs([])
    bfs([])

    return results