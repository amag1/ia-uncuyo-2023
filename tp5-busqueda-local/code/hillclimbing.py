from utils import *
import time
from solution import Solution
# Hill climbing para n reinas. 
# INPUTS: un vector solucion y una cantidad maxima de operaciones
# OUTPUTS: una solucion (parcial?), el costo de la misma, la cantidad de iteraciones y el tiempo de ejecucion
def hill_climbing(solution, ITERS, sideways = False, plot = False):
    i = 0
    currentSolution = solution
    flag = True
    t = time.time()
    fitness = [currentSolution.fitness]
    while i < ITERS and currentSolution.fitness > 0 and flag:
        i += 1
        # Obtener vecinos
        neighbors = get_neighbors(currentSolution.value)

        
        # Obtener el mejor vecino
        bestNeighbor = get_best_neighbor(neighbors)

        # Si se permiten movimientos al costado, se acepta el vecino si es igual al costo actual
        # Si no se permiten movimientos al costado, se acepta el vecino si es menor al costo actual
        if sideways:
            if check_solution(bestNeighbor) <= currentSolution.fitness:
                currentSolution = Solution(bestNeighbor, check_solution(bestNeighbor))
            else:
                flag = False

        else:
            if check_solution(bestNeighbor) < currentSolution.fitness:
                currentSolution = Solution(bestNeighbor, check_solution(bestNeighbor))
            else:
                flag = False

        fitness.append(currentSolution.fitness)
    
    t = time.time() - t

    if plot:
        plt.plot(fitness)
        plt.title(f"Hill Climbing - H over {i} iterations")
        plt.savefig("./plots/hill_climbing.png")

    return currentSolution, i, t



if __name__ == "__main__":
    s = generate_random_solution(8)
    
    print(s, check_solution(s))


    print("------------------")
    print(hill_climbing(s, 100, sideways=False))
    
    