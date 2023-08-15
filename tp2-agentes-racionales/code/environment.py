import random,string
# Clase que representa el entorno en el que se mueve el agente
class Environment:
    # Constructor
    # Recibe el tamaño del entorno y la tasa de suciedad
    # La tasa de suciedad es un número entre 0 y 1 que representa la probabilidad de que una casilla esté sucia
    # Crea una matriz que representa el entorno y la llena de suciedad
    def __init__(self, sizeX, sizeY, dirt_rate):
        self.matrix = [[0 for x in range(sizeX)] for y in range(sizeY)]
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.dirt_rate = dirt_rate
        self.dirty_squares = 0
        self.generate_dirt()
    
    # Imprime el estado actual del entorno
    def __str__(self) -> str:
        output = "Environment:\n"
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                output += f'{self.matrix[i][j]} '
            output += '\n'
        
        return output

    # Llena la matriz del entorno con suciedad segun el parametro dirt_rate
    def generate_dirt(self):
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                if random.random() < self.dirt_rate:
                    self.matrix[i][j] = 1
                    self.dirty_squares += 1

        if self.dirty_squares == 0:
            self.generate_dirt()

        # Guarda numero inicial de casillas sucias para medir performance
        self.initial_dirty_squares = self.dirty_squares
    
    # Devuelve el estado de una casilla
    def is_dirty(self, x, y):
        return self.matrix[x][y] == 1

    def accept_action(self,x,y,action):
        match action:
            case "UP":
                if y < self.sizeY - 1:
                    return True
            case "DOWN":
                if y > 0:
                    return True
            case "LEFT":
                if x > 0:
                    return True
            case "RIGHT":
                if x < self.sizeX - 1:
                    return True
            case "SUCK":
                if self.is_dirty(x,y):
                    self.matrix[x][y] = 0
                    self.dirty_squares -= 1
                    return True
            case _:
                return False
