import matplotlib.pyplot as plt
import csv

def boxplot(results):
    labels = [res[0] for res in results]
    data = [res[1] for res in results]

    fig, ax = plt.subplots()
    bplot = ax.boxplot(data, vert=True, labels=labels, patch_artist=True)
    ax.set_title('Comparación de algoritmos de búsqueda no informada')
    ax.set_ylabel('Cantidad de pasos')
    ax.set_xlabel('Algoritmo')
    ax.yaxis.grid(True)


    colors = ['pink', 'lightblue', 'lightgreen', 'lightgrey']
    for patch,color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

    plt.savefig('boxplot.png')
    plt.show()

def csv_write(results):
    headers = ["Agent", "Path", "Steps", "Path Depth"]
    with open("results.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        f.close()

    with open("results.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerows([item for sublist in results for item in sublist])
        f.close()

    


