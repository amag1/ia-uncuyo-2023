import time
from utils import *
import numpy as np
import math
from solution import Solution
def simmulated_annealing(solution, ITERS, plot=False):
    i = 0
    currentSolution = solution
    t = time.time()
    fitness = [currentSolution.fitness]
    # Funcion de probabilidad
    alpha = 0.95
    k = 0.9
    while i < ITERS and currentSolution.fitness > 0:
        i += 1
        # Obtener vecinos
        neighbors = get_neighbors(currentSolution.value)

        # Obtener un vecino random
        neighbor = neighbors[np.random.randint(0, len(neighbors))]

        # Calcular la diferencia de costos
        delta = check_solution(neighbor) - currentSolution.fitness

        # Si el vecino es mejor, se acepta
        if delta < 0:
            currentSolution = Solution(neighbor, check_solution(neighbor))

        # Si el vecino es peor, se acepta con una probabilidad
        else:
            p = np.random.rand()
            k = k * alpha
            if p < k - 0.05*delta:
                currentSolution = Solution(neighbor, check_solution(neighbor))

        fitness.append(currentSolution.fitness)
    
    t = time.time() - t

    if plot:
        plt.plot(fitness)
        plt.savefig("./plots/simmulated_annealing.png")
        

    return currentSolution, i, t

if __name__ == "__main__":
    s = generate_random_solution(8)
    
    print(s, check_solution(s))


    print("------------------")
    print(simmulated_annealing(s, 100))