import numpy as np
import sys
sys.path.append("..")

import utils, time
from solution import Solution

from selection import Selection
from crossover import Crossover
from mutation import Mutation
from replace import Replace

# Clase para implementar el algoritmo genético
class Genetic:
    def __init__(self, population, generations, target = 0, mutation = Mutation(), crossover = Crossover(), selection = Selection(),replace = Replace(), plot=False):
        self.population = population
        self.mutation = mutation
        self.crossover = crossover
        self.selection = selection
        self.generations = generations
        self.replace = replace
        self.target = target
        self.plot = plot

    def run(self):
        t = time.time()
        currentBest = self.population[0]
        i = 0
        while currentBest.fitness != self.target and i < self.generations:
            # Seleccionar padres usando la funcion de seleccion
            parents = [self.selection(self.population) for _ in range(len(self.population) // 2)]
            # Obtener pares de padres de la lista parents usando utils.fold_list
            parentPairs = utils.fold_list(parents)
            # Cruzar padres usando la funcion de crossover
            children = [self.crossover(p1, p2) for p1, p2 in parentPairs]
            # flatten children list
            children = [c for pair in children for c in pair]
            # Mutar hijos
            children = [self.mutation(c) for c in children]
            # Reemplazar
            self.population = self.replace(self.population, children)
            # Obtener el mejor
            currentBest = self.population[0]

            # Incrementar contador
            i += 1
        return currentBest, i, time.time() - t
    
    
        
if __name__ == "__main__":

    initialPopulation = []
    for i in range(20):
        s = utils.generate_random_solution(8)
        initialPopulation.append(Solution(s, utils.check_solution(s)))
    
    maxGen = 100
    target = 0
    genetic = Genetic(initialPopulation, maxGen, target, mutation=Mutation(type="random"), selection=Selection(type="proportional"))
    best, generations = genetic.run()
    print(best, "Generations:", generations)
