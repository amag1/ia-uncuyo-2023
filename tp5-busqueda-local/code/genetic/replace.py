import sys
import numpy as np
from solution import Solution

sys.path.append("..")

import utils

class Replace:
    def __init__(self, type = "elitism"):
        self.type = type
    
    def __call__(self, population, children):
        if self.type == "elitism":
            return self.elitism(population, children)
        elif self.type == "random":
            return self.random(population, children, rate = 0.5)
        
    def elitism(self, population, children):
        # Combinar la poblacion con los hijos
        combined = population + children
        # Ordenarlos por fitness
        combined = sorted(combined)
        # Seleccionar los mejores
        return combined[:len(population)]
    
    def random(self, population, children, rate = 0.5):
        # Cambiar un porcentaje de la poblacion
        for i in range(len(population)):
            if np.random.random() < rate:
                # Seleccionar un hijo random y asignarlo a population
                population[i] = np.random.choice(children)
        return population
    

if __name__ == "__main__":
    old = []
    for i in range(8):
        s = utils.generate_random_solution(8)
        old.append(Solution(s, utils.check_solution(s)))
    
    for i in old:
        print(i)

    print("--------------")
    
    new = []
    for i in range(8):
        s = utils.generate_random_solution(8)
        new.append(Solution(s, utils.check_solution(s)))
    
    for i in new:
        print(i)

    
    replace = Replace()
    r = replace(old, new)
    print("--------------")
    # for i in r:
    #     print(i)

    print("--------------")
    replace = Replace("random")
    r = replace(old, new)
    for i in r:
        print(i)
    
