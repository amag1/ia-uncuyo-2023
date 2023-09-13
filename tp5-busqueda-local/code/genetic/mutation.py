import sys
import numpy as np
from solution import Solution

sys.path.append("..")

import utils

class Mutation:
    def __init__(self, type = "random"):
        self.type = type
    
    def __call__(self, solution):
        if self.type == "swap":
            return self.swap(solution)
        elif self.type == "random":
            return self.random(solution)
    
    def swap(self, solution):
        vec = solution.value.copy()
        
        i = np.random.randint(0, len(vec))
        j = np.random.randint(0, len(vec))
        
        vec[i], vec[j] = vec[j], vec[i]
        return Solution(vec, utils.check_solution(vec))

    def random(self, solution):
        vec = solution.value.copy()
        i = np.random.randint(0, len(vec))
        vec[i] = np.random.randint(0, len(vec))
        return Solution(vec, utils.check_solution(vec))
    

if __name__ == "__main__":
    s = utils.generate_random_solution(4)
    sol = Solution(s, utils.check_solution(s))
    
    print(sol)
    print("------------------")

    mutation = Mutation("random")
    r1 = mutation(sol)
    print(r1)    

    mutation = Mutation()
    r2 = mutation(sol)
    print(r2)

    print(sol)
