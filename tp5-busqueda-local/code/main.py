import sys
sys.path.append("./genetic")

from testing import *
from utils import *
from annealing import simmulated_annealing
from hillclimbing import hill_climbing
from genetic import Genetic
import csv
import resultoptions as ro

if __name__ == "__main__":
    # init csv headers
    with open("./results/results.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows([["Algorithm", "Best result", "Iterations", "Time", "Solved"]])

    ITERS = 200
    QUEENS = 8
    envs = [generate_random_solution(QUEENS) for i in range(50)]
    # Testear hill climbing
    h1, t1, s1 = test(hill_climbing, envs, ITERS)

    print("------------------")

    # Testear simulated annealing
    h2, t2, s2 = test(simmulated_annealing, envs, ITERS)

    print("----------------")
    envs = [envs for _ in range(50)]
    # Testear algoritmo genetico
    h3, t3, s3 = testGenetic(envs, ITERS)


    # Plotear resultados
    ro.multiplot([("Hill Climbing", h1, t1, s1), ("Simulated Annealing", h2, t2, s2), ("Genetic", h3, t3, s3)], queens=QUEENS)
