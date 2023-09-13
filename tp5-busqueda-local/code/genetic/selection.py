import sys
import numpy as np
from solution import Solution

sys.path.append("..")

import utils

class Selection:
    def __init__(self, type = "proportional", k = 8):
        self.type = type
        self.k = k
    
    def __call__(self, population):
        if self.type == "tournament":
            return self.tournament(population)
        elif self.type == "proportional":
            return self.proportional(population)
    
    def tournament(self, population):
        # Seleccionar k individuos random
        selected = np.random.choice(population, self.k)
        # Seleccionar el mejor basado en el valor de fitness mas bajo
        return sorted(selected)[0]
        
    def proportional(self, population):
        # Calcular el fitness de cada individuo
        fitnesses = [s.fitness for s in population]

        # Calcular fitness inverso
        fitnesses = np.max(fitnesses) - fitnesses + 1
        
        # Calcular la probabilidad de cada individuo
        probs = fitnesses / np.sum(fitnesses)

        # Seleccionar un individuo random
        selected = np.random.choice(population, p=probs)
        return selected
    

if __name__ == "__main__":
    testpop = []
    # Generar 4 objetos de la clase Solution usando las funciones de utils
    for i in range(8):
        s = utils.generate_random_solution(8)
        testpop.append(Solution(s, utils.check_solution(s)))

    for s in testpop:
        print(s)

    selection = Selection("proportional")
    r = selection(testpop)
    print("--------------")
    print("Selected1: ")
    print(r)

    selection = Selection("tournament", 4)
    r = selection(testpop)
    print("--------------")
    print("Selected2: ")
    print(r)


