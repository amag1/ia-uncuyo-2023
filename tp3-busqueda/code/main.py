import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import random
fig, ax = plt.subplots()

min_val, max_val = 0, 10

intersection_matrix = np.random.randint(0, 10, size=(max_val, max_val))

ax.matshow(intersection_matrix, cmap=plt.cm.Blues)

for i in range(10):
    for j in range(10):
        c = intersection_matrix[j,i]
        if c > 0:
            ax.text(i, j, str(c), va='center', ha='center')

plt.show()

