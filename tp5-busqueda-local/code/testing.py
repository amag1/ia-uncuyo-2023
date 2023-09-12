import sys
sys.path.append("./genetic")

import statistics
import csv
from genetic import Genetic
def test(function, params, iters):
    print("Testing: " + function.__name__)
    
    r = []
    for p in params:
        r.append(function(p, iters))

    heuristic = [s[0].fitness for s in r]
    time = [s[2] for s in r]
    solved = [s[0].fitness == 0 for s in r]
    print("Heuristic: " + str(statistics.mean(heuristic)) + " +- " + str(statistics.stdev(heuristic)))
    print("Time: " + str(statistics.mean(time)) + " +- " + str(statistics.stdev(time)))
    print("Percentage of instances solved: " + str(sum([1 if s[0].fitness == 0 else 0 for s in r]) / len(r)))
    
    # Write results to csv
    with open("./results/results.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerows([[function.__name__, s[0].fitness, s[1], s[2], s[0].fitness == 0] for s in r])
    return heuristic, time, solved

def testGenetic(envs, iters):
    print(f"Testing genetic algorithm ({len(envs)} iterations with a population of {len(envs[0])} and a max of {iters} generations)")

    r = []
    for e in envs:
        g = Genetic(e, iters, target=0)
        r.append(g.run())
    
    heuristic = [s[0].fitness for s in r]
    time = [s[2] for s in r]
    solved = [s[0].fitness == 0 for s in r]

    print("Heuristic: " + str(statistics.mean(heuristic)) + " +- " + str(statistics.stdev(heuristic)))
    print("Time: " + str(statistics.mean(time)) + " +- " + str(statistics.stdev(time)))
    print("Percentage of instances solved: " + str(sum([1 if s[0].fitness == 0 else 0 for s in r]) / len(r)))
    
    # Write results to csv
    with open("./results/results.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerows([["Genetic", s[0].fitness, s[1], s[2], s[0].fitness == 0] for s in r])
    return heuristic, time, solved