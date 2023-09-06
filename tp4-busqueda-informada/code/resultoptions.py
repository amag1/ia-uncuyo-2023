import matplotlib.pyplot as plt
import csv


def boxplot(results):
    labels = [res[0] for res in results]
    data = [res[1] for res in results]

    fig, ax = plt.subplots()
    bplot = ax.boxplot(data, vert=True, labels=labels, patch_artist=True)
    ax.set_title('Comparación de algoritmos de búsqueda')
    ax.set_ylabel('Cantidad de pasos')
    ax.set_xlabel('Algoritmo')
    ax.yaxis.grid(True)

    colors = ['pink', 'lightblue', 'lightgreen', 'lightgrey']
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

    plt.savefig('./plots/boxplot.png')
    plt.show()


def prune_results(item):
    return [item[0],item[5], item[2], item[4]]

def csv_write(results):
    headers = ["Agent", "env_n", "explored_states", "success"]
    with open("./results/results.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        f.close()

    with open("./results/results.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerows([prune_results(item) for sublist in results for item in sublist])
        f.close()