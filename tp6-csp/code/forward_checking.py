from solution import *
import time, copy


class Variable:
    value = None
    domain = None
    index = None

    def __init__(self, value, domain, index):
        self.value = value
        self.domain = domain
        self.index = index

    def __str__(self):
        return str(self.value)

# Solution using fordward checking and MVR
def fc_mvr_queens(queens):
    t1 = time.time()
    steps = [0]
    
    initial_state = [Variable(None, list(range(queens)), i) for i in range(queens)]
    
    s = fc_mvr_queens_rec(queens, initial_state, steps)

    t2 = time.time()
    if s == None:
        return Solution(None,None, t2-t1)

    return Solution([var.value for var in s],steps[0], t2-t1)

def extract_mvr(current_sol):
    # filter empty variables
    empty_vars = [var for var in current_sol if var.value is None]
    # extract the variable with the smallest domain
    shortest = empty_vars[0]
    for var in empty_vars:
        if len(var.domain) < len(shortest.domain):
            shortest = var
    
    return shortest
            
def fc_mvr_queens_rec(queens, current_sol, steps = None):
    if steps == None:
        steps = [0]

    # if there is no more variables to assign, return the solution
    if all(variable.value is not None for variable in current_sol):
        return current_sol
    
    # if there is no available value for a variable, return None
    if any(not variable.domain for variable in current_sol):
        return None
    
    # extract next variable to assign
    shortest = extract_mvr(current_sol)
    
    # iterate through all possible variables
    for val in shortest.domain:
        steps[0] += 1

        # copy the current solution
        copied_list = copy.deepcopy(current_sol)

        # set the value to the variable
        copied_list[shortest.index].value = val

        # remove the value from the domain
        copied_list[shortest.index].domain = [val]

        # update domains for other variables
        # remove possible queens in the same row or diagonal
        for variable in copied_list:
            if variable.value is None and variable.index != shortest.index:
                if val in variable.domain:
                    variable.domain.remove(val)
                if val + (variable.index - shortest.index) in variable.domain:
                    variable.domain.remove(val + (variable.index - shortest.index))
                    
                if val - (variable.index - shortest.index) in variable.domain:
                    variable.domain.remove(val - (variable.index - shortest.index))

        # call the function recursively
        s = fc_mvr_queens_rec(queens, copied_list, steps)

        if s != None:
            return s
        
        # if there is not solution, restore previous state
        