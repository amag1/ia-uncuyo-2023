# N queens problem.
# La solucion puede ser modelada como un vector de enteros, donde cada posicion corresponde a una columna y el valor al numero de fila donde se encuentra la reina.

import random
import numpy as np
import matplotlib.pyplot as plt
from solution import Solution

# Funcion para verificar si una solucion es valida.
# Devuelve 0 si no hay dos reinas atacandose
# De otro modo devuelve el numero de pares de reinas atacandose
def check_solution(solution):
    r = 0
    # Chequear cada fila
    for i in range(len(solution)):
        # Chequear cada columna
        for j in range(i + 1, len(solution)):
            # Si estan en la misma fila o en la misma diagonal
            if solution[i] == solution[j] or abs(solution[i] - solution[j]) == j - i:
                r += 1

    return r

def generate_random_solution(SIZE):
    s = [random.randint(0, SIZE-1) for _ in range(SIZE)]
    return Solution(s, check_solution(s))

def plot_grid_with_lines(L):
    n = len(L)

    # Create an n x n array with zeros (white squares by default)
    grid = np.zeros((n, n))

    # Set the squares to 1 (black) where L[i] == j
    for i in range(n):
        grid[i][L[i]] = 1

    # Create the figure and axis
    fig, ax = plt.subplots()

    # Create a colormap with white and black colors
    cmap = plt.get_cmap()

    # Plot the grid with colored squares
    ax.imshow(grid, cmap="Blues")

    # Add grid lines in the middle
    ax.set_xticks(np.arange(-0.5, n, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, n, 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)

    # Remove axis labels
    ax.set_xticks([])
    ax.set_yticks([])

    # Show the plot
    plt.show()


def get_neighbors(solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(len(solution)):
            if solution[i] != j:
                neighbor = solution.copy()
                neighbor[i] = j
                neighbors.append(neighbor)
    return neighbors

def get_best_neighbor(neighbors):
    bestNeighbor = neighbors[0]
    bestCost = check_solution(bestNeighbor)
    for neighbor in neighbors:
        cost = check_solution(neighbor)
        if cost < bestCost:
            bestNeighbor = neighbor
            bestCost = cost
    return bestNeighbor

def boxplot(results, title, ylabel):
    labels = [res[0] for res in results]
    data = [res[1] for res in results]

    fig, ax = plt.subplots()
    bplot = ax.boxplot(data, vert=True, labels=labels, patch_artist=True)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel('Algoritmo')
    ax.yaxis.grid(True)

    colors = ['pink', 'lightblue', 'lightgreen', 'lightgrey']
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

    plt.savefig('./plots/boxplot.png')
    plt.show()

def fold_list(lst):
    return [(lst[i], lst[i + 1]) for i in range(0, len(lst), 2) if i + 1 < len(lst)]


if __name__ == "__main__":
    l = [0, 1, 2, 3, 4, 5, 6, 7]
    print(fold_list(l))