import sys
import numpy as np
from solution import Solution

sys.path.append("..")

import utils

from selection import Selection

class Crossover:
    def __init__(self, type = "one_point"):
        self.type = type
    
    def __call__(self, s1, s2):
        veca = s1.value
        vecb = s2.value

        # suponiendo que las soluciones son vectores
        point = np.random.randint(1, len(veca)-1)

        if self.type == "one_point":
            h1 = veca[:point] + vecb[point:]
            h2 = vecb[:point] + veca[point:]

            res1 = Solution(h1, utils.check_solution(h1))
            res2 = Solution(h2, utils.check_solution(h2))
            return (res1,res2)
        
if __name__ == "__main__":
    testpop = []
    # Generar 4 objetos de la clase Solution usando las funciones de utils
    for i in range(8):
        s = utils.generate_random_solution(6)
        testpop.append(Solution(s, utils.check_solution(s)))

    
    # Obtener dos miembros de la poblacion usando torneos
    selection = Selection("tournament", 4)
    r1 = selection(testpop)
    r2 = selection(testpop)
    print(r1, "-", r2)

    print("----------")
    crossover = Crossover()
    h1, h2 = crossover(r1, r2)
    print(h1, "-", h2)

