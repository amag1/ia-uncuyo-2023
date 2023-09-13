import sys
sys.path.append("./genetic")

from testing import *
from utils import *
from annealing import simmulated_annealing
from hillclimbing import hill_climbing
from genetic import Genetic
import csv
import resultoptions as ro

def csv_fullplot(QUEENS, ITERS):
    # init csv headers
    with open("./results/results.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows([["Algorithm", "Queens", "Best result", "Iterations", "Time", "Solved"]])
    for q in QUEENS:
        print("\nQueens: " + str(q))
        envs = [generate_random_solution(q) for i in range(50)]
        # Testear hill climbing
        h1, t1, s1 = test(hill_climbing, envs, ITERS,q)

        print("------------------")

        # Testear simulated annealing
        h2, t2, s2 = test(simmulated_annealing, envs, ITERS, q)

        print("----------------")

        envs = [envs for _ in range(50)]
        # Testear algoritmo genetico
        h3, t3, s3 = testGenetic(envs, ITERS, q)


        # Plotear resultados
        ro.multiplot([("Hill Climbing", h1, t1, s1), ("Simulated Annealing", h2, t2, s2), ("Genetic", h3, t3, s3)], queens=q)

def plot_genetic_performance(q, ITERS, POPSIZE):
    env = [generate_random_solution(q) for _ in range(POPSIZE)]
    g = Genetic(env, ITERS, target=0, plot=True)
    return g.run()

def plot_hillclimbing_performance(env, ITERS):
    return hill_climbing(env, ITERS, plot=True)

def plot_annealing_performance(env, ITERS):
    return simmulated_annealing(env, ITERS, plot=True)

if __name__ == "__main__":

    ITERS = 200
    QUEENS = [4, 8, 10, 12, 15]

    # plot_genetic_performance(15, ITERS, 50)

    s = generate_random_solution(15)
    # plot_hillclimbing_performance(s, ITERS)
    plot_annealing_performance(s, ITERS)

    
