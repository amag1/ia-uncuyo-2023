from backtracking import backtrack_queens
from forward_checking import fc_mvr_queens
from utils import *
import csv, seaborn as sns, multiprocessing as mp, pandas as pd, matplotlib.pyplot as plt

def iterback(i,q):
    # Run Backtracking
    return(backtrack_queens(q))
    
def iterfc(i,q):
    # Run Forward Checking
    return(fc_mvr_queens(q))

def csv_write(QUEENS, ITERS):
    with open('results.csv', mode='w') as results_file:
        results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        results_writer.writerow(["Algorithm", "N", "Steps", "Time"])

        for q in QUEENS:
            with mp.Pool(8) as pool:
                r = pool.starmap(iterback, [(i,q) for i in range(ITERS)])
                # get results from map
                for i in r:
                    results_writer.writerow(["Backtracking", q, i.steps, i.time])


                # do the same for forward checking
                r = pool.starmap(iterfc, [(i,q) for i in range(ITERS)])
                # get results from map
                for i in r:
                    results_writer.writerow(["Forward Checking", q, i.steps, i.time])

    # close file
    results_file.close()


if __name__ == "__main__":
    # QUEENS = [4, 8, 10, 12,15, 20]
    # ITERS = 30
    # csv_write(QUEENS, ITERS)

    # read csv
    df = pd.read_csv("results.csv")
    
    # First, create a figure with two subplots
    fig, ax1 = plt.subplots(1, 1, figsize=(10, 10))

    # Plot 1: Amount of Steps per N per Algorithm
    sns.lineplot(data=df, x='N', y='Steps', hue='Algorithm', ax=ax1)
    ax1.set_title('Explored states per queen number')
    ax1.set_xlabel('Queens')
    ax1.set_ylabel('Explored States')
    ax1.set_yscale('log')

    plt.tight_layout()
    plt.savefig('steps.png')


    fig, ax2 = plt.subplots(1, 1, figsize=(10, 10))
    

    # Plot 2: Median and Standard Deviation of Time per N per Algorithm
    sns.lineplot(data=df, x='N', y='Time', hue='Algorithm', ax=ax2, estimator='median', ci='sd')
    ax2.set_title('Median and Standard Deviation of Time per queen number')
    ax2.set_xlabel('Queens')
    ax2.set_ylabel('Time (s)')
    ax2.set_yscale('log')

    plt.tight_layout()
    plt.savefig('time.png')
    # plot time
    

    

    

    