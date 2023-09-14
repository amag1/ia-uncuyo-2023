import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker
# Expects a list of 4-uples: (Algorithm, Result, Time, Solve Rate)
def multiplot(results, queens=8):
    algorithms = [res[0] for res in results]
    data = [res[1] for res in results]
    time = [res[2] for res in results]
    solved = [res[3] for res in results]

    fig, ax = plt.subplots(3,1, figsize=(6,12))
    fig.suptitle(f'Comparacion de algoritmos de busqueda local \n para el problema de las {queens} reinas')
    #subplot 1
    b1 = ax[0].boxplot(data, vert=True, labels=algorithms, patch_artist=True)
    ax[0].set_ylabel('Valor de la funcion de fitness al finalizar')
    # Set y-axis grid to only have integers
    ax[0].yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    # Set y-grid to use major ticks
    ax[0].yaxis.grid(True)

    colors = ['pink', 'lightblue', 'lightgreen']
    for patch, color in zip(b1['boxes'], colors):
        patch.set_facecolor(color)

    # Add jitter to the data points
    for i, algorithm_data in enumerate(data):
        jitter = np.random.normal(0, 0.04, size=len(algorithm_data))
        ax[0].plot(i + 1 + jitter, algorithm_data, 'ro', alpha=0.5)  # 'ro' for red circles

    #subplot 2
    b2 = ax[1].boxplot(time, vert=True, labels=algorithms, patch_artist=True)
    ax[1].set_ylabel('Tiempo de ejecucion (s)')
    ax[1].yaxis.grid(True)
    ax[1].set_yscale('log')

    colors = ['pink', 'lightblue', 'lightgreen']
    for patch, color in zip(b2['boxes'], colors):
        patch.set_facecolor(color)
    
    # Add jitter to the data points
    for i, algorithm_time in enumerate(time):
        jitter = np.random.normal(0, 0.04, size=len(algorithm_time))
        ax[1].plot(i + 1 + jitter, algorithm_time, 'ro', alpha=0.5)

    #subplot 3
    
    #transformar booleanos a int suponiendo que solved es una lista de listas
    solved = [[int(i) for i in sublist] for sublist in solved]

    #calcular porcentaje
    solved = [sum(sublist)/len(sublist) for sublist in solved]
    
    #plot using barchart
    ax[2].bar(algorithms, solved, color=['pink', 'lightblue', 'lightgreen'])
    ax[2].set_ylabel('Porcentaje de instancias resueltas')
    ax[2].yaxis.grid(True)
    ax[2].set_ylim(0,1)

    
    plt.tight_layout()
    #save figure
    plt.savefig(f'./plots/multiplot_{queens}.png')



    
def compareGenetic(results):
    var = results[0]
    algorithms = results[1]
    time = results[3]
    solved = results[4]

    fig, ax = plt.subplots(2,1, figsize=(6,12))
    fig.suptitle(f"Comparacion de funciones de {var} para el problema de las n reinas")

    #subplot 2
    ax[0].boxplot(time, vert=True, labels=algorithms, patch_artist=True)
    ax[0].set_ylabel('Tiempo de ejecucion (s)')
    ax[0].yaxis.grid(True)

    #subplot 3

    #transformar booleanos a int suponiendo que solved es una lista de listas
    solved = [[int(i) for i in sublist] for sublist in solved]

    #calcular porcentaje
    solved = [sum(sublist)/len(sublist) for sublist in solved]
    
    #plot using barchart
    ax[1].bar(algorithms, solved)
    ax[1].set_ylabel('Porcentaje de instancias resueltas')
    ax[1].yaxis.grid(True)
    ax[1].set_ylim(0,1)

    plt.tight_layout()
    plt.savefig(f'./plots/compareGenetic_{var}.png')

def plot_queens(v):
    from matplotlib import colors
    solution = v.value
    f = v.fitness
    n = len(solution)
    chessboard = np.zeros((n, n))

    for row, col in enumerate(solution):
        chessboard[row, col] = 1

    fig, ax = plt.subplots()
    colorlist = ["white", "lightblue"]
    cm = colors.ListedColormap(colorlist)
    ax.imshow(chessboard, cmap=cm)

    # Draw grid lines
    for i in range(n + 1):
        ax.axhline(i - 0.5, color="black", linewidth=1)
        ax.axvline(i - 0.5, color="black", linewidth=1)
    
    # Add queen text
    for row, col in enumerate(solution):
        ax.text(col, row, '♛', ha="center", va="center", fontsize=20)
    ax.set_title(f"Configuracion para el problema de las {n} reinas \n Pares de reinas amenazados: {f}")

    # Set ticks
    ax.set_xticks(np.arange(-0.5, n, 1))
    ax.set_yticks(np.arange(-0.5, n, 1))

    ax.set_xticklabels([])
    ax.set_yticklabels([])

    plt.savefig(f"./plots/config_{n}_queens.png")
    plt.show()