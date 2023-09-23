import time
from solution import *
from utils import *
# Solving n-queens by backtracking

def backtrack_queens(queens):
    current_sol = []
    t1 = time.time()

    
    s = backtrack_queens_rec(queens, current_sol)
    t2 = time.time()
    if s == None:
        return Solution(None,None, t2-t1)

    return Solution(s[0],s[1], t2-t1)

def backtrack_queens_rec(queens, current_sol, steps = None):
    if steps == None:
        steps = [0]

    if len(current_sol) == queens:
        return current_sol, steps[0]

    for i in range(queens):
        steps[0] += 1
        if not is_attacked(current_sol, i):
            current_sol.append(i)
            s = backtrack_queens_rec(queens, current_sol, steps)
            if s != None:
                return s
            current_sol.pop()
    return None

