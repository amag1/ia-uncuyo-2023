import numpy as np


class Environment:
    def __init__(self, obstacle_rate, size):
        self.matrix = np.zeros((size, size))
        self.size = size
        self.obstacle_rate = obstacle_rate
        self.generate_obstacles()
        self.set_goal()

    def __str__(self):
        output = "Environment:\n"
        for i in range(self.size):
            for j in range(self.size):
                output += f'{self.matrix[i][j]} '
            output += '\n'

        return output

    def generate_obstacles(self):
        for i in range(self.size):
            for j in range(self.size):
                if np.random.rand() < self.obstacle_rate:
                    self.matrix[i][j] = 1

    def set_goal(self):
        x, y = np.random.randint(0, self.size, 2)
        while self.matrix[x][y] == 1:
            x, y = np.random.randint(0, self.size, 2)
        self.matrix[x][y] = 2
        self.goal = (x, y)

    # Metodo para obtener una posicion random que este vacia
    def get_random_position(self):
        x, y = np.random.randint(0, self.size, 2)
        while self.matrix[x][y] == 1 or self.matrix[x][y] == 2:
            x, y = np.random.randint(0, self.size, 2)
        return (x, y)

    # Dada una posicion, obtiene los cuadrados cercanos
    def get_surrounding_squares(self, x, y):
        surrounding_squares = []
        if x > 0 and self.matrix[x-1][y] != 1.0:
            surrounding_squares.append((x-1, y))
        if x < self.size-1 and self.matrix[x+1][y] != 1.0:
            surrounding_squares.append((x+1, y))
        if y > 0 and self.matrix[x][y-1] != 1.0:
            surrounding_squares.append((x, y-1))
        if y < self.size-1 and self.matrix[x][y+1] != 1.0:
            surrounding_squares.append((x, y+1))
        return surrounding_squares
