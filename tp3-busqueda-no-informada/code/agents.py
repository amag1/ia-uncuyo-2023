from abc import ABC, abstractmethod


# Clase para representar los nodos dentro del arbol de busqueda
class Node:
    parent = None
    depth = None
    status = None

    def __init__(self, x, y):
        self.position = (x, y)


# Clase abstracta para agentes
class Agent(ABC):
    def __init__(self, env):
        self.env = env

        # Medidas de performance del agente
        self.success = False
        self.steps = 0

        # Estructuras para el algoritmo de busqueda
        self.frontier = []
        self.explored = {}

        # Start the agent in a random position
        self.posX, self.posY = self.env.get_random_position()

    # Metodo para obtener el camino que debe seguir el agente

    @abstractmethod
    def getPath(self):
        pass

    def getSolution(self, node):
        path = []
        while node.parent != None:
            path.append(node.position)
            node = node.parent
        path.reverse()
        return (self.__class__.__name__, path, self.steps)


class BFSAgent(Agent):
    def __init__(self, env):
        super().__init__(env)

    def getPath(self):
        # Creo el nodo inicial
        start = Node(self.posX, self.posY)
        start.depth = 0
        start.status = 'V'

        # Agrego el nodo inicial a la frontera
        self.frontier.append(start)

        # Mientras la frontera no este vacia
        while self.frontier:
            # Obtengo el primer nodo de la frontera
            node = self.frontier.pop(0)
            self.steps += 1
            # Si el nodo es el goal, termino
            if self.env.matrix[node.position[0]][node.position[1]] == 2:
                self.success = True
                return self.getSolution(node)

            # Si el nodo no esta en explored, lo agrego
            if node.position not in self.explored:
                self.explored[node.position] = node

                # Obtengo los nodos hijos
                children = [s for s in self.env.get_surrounding_squares(
                    node.position[0], node.position[1]) if s not in self.explored]

                # Por cada hijo, creo un nodo y lo agrego a la frontera
                for child in children:
                    child_node = Node(child[0], child[1])
                    child_node.parent = node
                    child_node.depth = node.depth + 1
                    self.frontier.append(child_node)
