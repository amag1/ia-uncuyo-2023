import sys
sys.path.append("./genetic")

from selection import Selection
from crossover import Crossover
from mutation import Mutation
from replace import Replace

import statistics, csv, multiprocessing
from genetic import Genetic


def process_object(object):
    return object.run()


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



def compareGeneticSelection(envs, iters):
    # Initialize genetic algorithms using different selection methods
    # and compare their results
    print('Testing genetic algorithm with different selection methods')
    print("Proportional selection...")
    r1 = []
    for e in envs:
        r1.append(Genetic(e, iters, target=0, selection=Selection(type="proportional")))
    
    pool = multiprocessing.Pool()
    r1 = pool.map(process_object, r1)
    pool.close()
    pool.join()



    print("Tournament selection...")
    r2 = []
    for e in envs:
        r2.append(Genetic(e, iters, target=0, selection=Selection(type="tournament", k=8)))
    
    pool = multiprocessing.Pool()
    r2 = pool.map(process_object, r2)
    pool.close()
    pool.join()
    
    print("-----------------")

    heuristic1 = [s[0].fitness for s in r1]
    time1 = [s[2] for s in r1]
    solved1 = [s[0].fitness == 0 for s in r1]

    heuristic2 = [s[0].fitness for s in r2]
    time2 = [s[2] for s in r2]
    solved2 = [s[0].fitness == 0 for s in r2]

    print("Heuristic1: " + str(statistics.mean(heuristic1)) + " +- " + str(statistics.stdev(heuristic1)))
    print("Time1: " + str(statistics.mean(time1)) + " +- " + str(statistics.stdev(time1)))
    print("Solved1: " + str(sum(solved1)) + " / " + str(len(solved1)))
    print("-----------")
    print("Heuristic2: " + str(statistics.mean(heuristic2)) + " +- " + str(statistics.stdev(heuristic2)))
    print("Time2: " + str(statistics.mean(time2)) + " +- " + str(statistics.stdev(time2)))
    print("Solved2: " + str(sum(solved2)) + " / " + str(len(solved2)))

    return "seleccion", ["proportional", "tournament"], [heuristic1, heuristic2], [time1, time2], [solved1, solved2]

def compareGeneticMutation(envs, iters):
    # Initialize genetic algorithms using different selection methods
    # and compare their results
    print('Testing genetic algorithm with different mutation methods')
    print("Random mutation...")
    r1 = []
    for e in envs:
        r1.append(Genetic(e, iters, target=0, mutation=Mutation(type="random")))
    
    pool = multiprocessing.Pool()
    r1 = pool.map(process_object, r1)
    pool.close()
    pool.join()



    print("Swap mutation...")
    r2 = []
    for e in envs:
        r2.append(Genetic(e, iters, target=0, mutation=Mutation(type="swap")))
    
    pool = multiprocessing.Pool()
    r2 = pool.map(process_object, r2)
    pool.close()
    pool.join()
    
    print("-----------------")

    heuristic1 = [s[0].fitness for s in r1]
    time1 = [s[2] for s in r1]
    solved1 = [s[0].fitness == 0 for s in r1]

    heuristic2 = [s[0].fitness for s in r2]
    time2 = [s[2] for s in r2]
    solved2 = [s[0].fitness == 0 for s in r2]

    print("Heuristic1: " + str(statistics.mean(heuristic1)) + " +- " + str(statistics.stdev(heuristic1)))
    print("Time1: " + str(statistics.mean(time1)) + " +- " + str(statistics.stdev(time1)))
    print("Solved1: " + str(sum(solved1)) + " / " + str(len(solved1)))
    print("-----------")
    print("Heuristic2: " + str(statistics.mean(heuristic2)) + " +- " + str(statistics.stdev(heuristic2)))
    print("Time2: " + str(statistics.mean(time2)) + " +- " + str(statistics.stdev(time2)))
    print("Solved2: " + str(sum(solved2)) + " / " + str(len(solved2)))

    return "mutacion", ["random", "swap"], [heuristic1, heuristic2], [time1, time2], [solved1, solved2]


def compareGeneticReplacement(envs, iters):
    # Initialize genetic algorithms using different selection methods
    # and compare their results
    print('Testing genetic algorithm with different replacement methods')
    print("Elitist replacement...")
    r1 = []
    for e in envs:
        r1.append(Genetic(e, iters, target=0, replace=Replace(type="elitism")))
    
    pool = multiprocessing.Pool()
    r1 = pool.map(process_object, r1)
    pool.close()
    pool.join()



    print("Random replacement (odds = 0.5)...")
    r2 = []
    for e in envs:
        r2.append(Genetic(e, iters, target=0, replace=Replace(type="random")))
    
    pool = multiprocessing.Pool()
    r2 = pool.map(process_object, r2)
    pool.close()
    pool.join()
    
    print("-----------------")

    heuristic1 = [s[0].fitness for s in r1]
    time1 = [s[2] for s in r1]
    solved1 = [s[0].fitness == 0 for s in r1]

    heuristic2 = [s[0].fitness for s in r2]
    time2 = [s[2] for s in r2]
    solved2 = [s[0].fitness == 0 for s in r2]

    print("Heuristic1: " + str(statistics.mean(heuristic1)) + " +- " + str(statistics.stdev(heuristic1)))
    print("Time1: " + str(statistics.mean(time1)) + " +- " + str(statistics.stdev(time1)))
    print("Solved1: " + str(sum(solved1)) + " / " + str(len(solved1)))
    print("-----------")
    print("Heuristic2: " + str(statistics.mean(heuristic2)) + " +- " + str(statistics.stdev(heuristic2)))
    print("Time2: " + str(statistics.mean(time2)) + " +- " + str(statistics.stdev(time2)))
    print("Solved2: " + str(sum(solved2)) + " / " + str(len(solved2)))

    return "reemplazo", ["elitist", "random"], [heuristic1, heuristic2], [time1, time2], [solved1, solved2]
