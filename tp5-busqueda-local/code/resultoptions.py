import matplotlib.pyplot as plt

# Expects a list of 4-uples: (Algorithm, Result, Time, Solve Rate)
def multiplot(results, queens=8):
    algorithms = [res[0] for res in results]
    data = [res[1] for res in results]
    time = [res[2] for res in results]
    solved = [res[3] for res in results]

    fig, ax = plt.subplots(3,1, figsize=(6,12))
    fig.suptitle(f'Comparacion de algoritmos de busqueda local \n para el problema de las {queens} reinas')
    #subplot 1
    ax[0].boxplot(data, vert=True, labels=algorithms, patch_artist=True)
    ax[0].set_ylabel('Valor de la funcion de fitness al finalizar')
    ax[0].yaxis.grid(True)

    #subplot 2
    ax[1].boxplot(time, vert=True, labels=algorithms, patch_artist=True)
    ax[1].set_ylabel('Tiempo de ejecucion (s)')
    ax[1].yaxis.grid(True)

    #subplot 3
    
    #transformar booleanos a int suponiendo que solved es una lista de listas
    solved = [[int(i) for i in sublist] for sublist in solved]

    #calcular porcentaje
    solved = [sum(sublist)/len(sublist) for sublist in solved]
    
    #plot using barchart
    ax[2].bar(algorithms, solved)
    ax[2].set_ylabel('Porcentaje de instancias resueltas')
    ax[2].yaxis.grid(True)
    ax[2].set_ylim(0,1)

    
    plt.tight_layout()
    #save figure
    plt.savefig('./plots/multiplot.png')



    
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