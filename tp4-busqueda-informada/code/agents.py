from abc import ABC, abstractmethod
import heapq as hq

# Clase para representar los nodos dentro del arbol de busqueda


class Node:
    parent = None
    depth = None
    status = None

    def __init__(self, x, y):
        self.position = (x, y)


class UniformNode(Node):
    def __init__(self, x, y, cost):
        super().__init__(x, y)
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


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

    def createInitialNode(self, posX, posY):
        start = Node(posX, posY)
        start.depth = 0
        start.status = 'V'
        return start

    def createNode(self, posX, posY, parent, depth):
        node = Node(posX, posY)
        node.parent = parent
        node.depth = depth
        node.status = 'V'
        return node
    # Metodo para obtener el camino que debe seguir el agente

    def findPath(self, plot=False):
        # Creo el nodo inicial
        start = self.createInitialNode(self.posX, self.posY)

        # Agrego el nodo inicial a la frontera
        self.frontier.append(start)

        # Mientras la frontera no este vacia
        while self.frontier:
            # Extraer el nodo de la frontera segun el tipo de agente
            node = self.extractNode()
            self.steps += 1
            # Si el nodo es el goal, termino
            if self.env.matrix[node.position[0]][node.position[1]] == 2:
                self.success = True
                return self.getSolution(node, plot)

            self.exploreNode(node)

        return self.getSolution(None)

    def exploreNode(self, node):
        # Si el nodo no esta en explored, lo agrego
            if node.position not in self.explored:
                self.explored[node.position] = node

                # Obtengo los nodos hijos
                children = [s for s in self.env.get_surrounding_squares(
                    node.position[0], node.position[1]) if s not in self.explored]

                # Por cada hijo, creo un nodo y lo agrego a la frontera
                for child in children:
                    child_node = self.createNode(
                        child[0], child[1], node, node.depth + 1)
                    self.addNode(child_node)

            else:
                self.handleExplored(node)


    def getSolution(self, node, plot=False):
        if node is None:
            return (self.__class__.__name__, [], self.steps, float("inf"), self.success, self.env.id)
        path = []
        depth = node.depth
        while node.parent != None:
            path.append(node.position)
            node = node.parent
        path.reverse()
        if plot:
            self.plotSolution(path)
            
        return (self.__class__.__name__, path, self.steps, depth, self.success, self.env.id)

    def handleExplored(self, node):
        pass

    def plotSolution(self, path):
        if path == []:
            return

        import matplotlib.pyplot as plt
        from matplotlib import colors

        fig, ax = plt.subplots(figsize=(10, 10))

        m = self.env.matrix.copy()
        m[self.posX][self.posY] = 3

        for node in path[:-1]:
            m[node[0]][node[1]] = 4

        colorlist = ["white", "black", "green", "red", "lightblue"]
        cm = colors.ListedColormap(colorlist)

        for i in range(len(path)-1):
            node = path[i]

            arrow = self.getDirection(node, path[i+1])
            ax.text(node[1], node[0], arrow, ha="center", va="center")

        ax.imshow(m, cmap=cm)
        plt.savefig(f"./plots/{self.__class__.__name__}.png")
        plt.show()

    def getDirection(self, node1, node2):
        if node1[0] == node2[0]:
            if node1[1] < node2[1]:
                return '→'
            else:
                return '←'
        else:
            if node1[0] < node2[0]:
                return '↓'
            else:
                return '↑'

    @abstractmethod
    def extractNode(self):
        pass

    @abstractmethod
    def addNode(self, node):
        pass

class AStarAgent(Agent):
    def __init__(self, env):
        super().__init__(env)

    # Se define una heuristica para el problema
    def heuristic(self, x,y):
        return abs(x - self.env.goal[0]) + abs(y - self.env.goal[1])
    
    def cost(self, x,y,node):
        return 1 + node.depth + 2*self.heuristic(x,y)
    
    def createInitialNode(self, posX, posY):
        start = UniformNode(posX, posY, 0)
        start.depth = 0
        start.status = 'V'
        return start
    
    def createNode(self, posX, posY, parent, depth):
        node = UniformNode(posX, posY, self.cost(posX,posY,parent))
        node.parent = parent
        node.depth = depth
        node.status = 'V'
        return node
    
    def exploreNode(self, node):
        if not (node.position[0],node.position[1], node.parent) in self.explored:
            self.explored[(node.position[0],node.position[1], node.parent)] = node
        
        # Obtengo los nodos hijos
            children = [s for s in self.env.get_surrounding_squares(
                node.position[0], node.position[1])]

            # Por cada hijo, creo un nodo y lo agrego a la frontera
            for child in children:
                child_node = self.createNode(
                    child[0], child[1], node, node.depth + 1)
                self.addNode(child_node)

        else:
            self.handleExplored(node)

    def addNode(self, child_node):
        hq.heappush(self.frontier,  child_node)
    
    def extractNode(self):
        return hq.heappop(self.frontier)
        

        
class UniformAgent(Agent):
    def __init__(self, env):
        super().__init__(env)

    # Como las aristas no tienen pesos, la funcion de costos es una constante
    def cost(self, node):
        return 1 + node.cost

    def handleExplored(self, node):
        if self.explored[node.position].cost > node.cost:
            self.explored[node.position].cost = node.cost
            self.explored[node.position].parent = node.parent
            self.explored[node.position].depth = node.depth + 1

            self.explored.heapify()

    def createInitialNode(self, posX, posY):
        start = UniformNode(posX, posY, 0)
        start.depth = 0
        start.status = 'V'
        return start

    def createNode(self, posX, posY, parent, depth):
        node = UniformNode(posX, posY, self.cost(parent))
        node.parent = parent
        node.depth = depth
        node.status = 'V'
        return node

    def addNode(self, node):
        hq.heappush(self.frontier,  node)

    def extractNode(self):
        return hq.heappop(self.frontier)
        


class BFSAgent(Agent):
    def __init__(self, env):
        super().__init__(env)

    def extractNode(self):
        return self.frontier.pop(0)

    def addNode(self, node):
        self.frontier.append(node)


class DFSAgent(Agent):
    def __init__(self, env):
        super().__init__(env)

    def extractNode(self):
        return self.frontier.pop()

    def addNode(self, node):
        self.frontier.append(node)


class DFSLimitedAgent(DFSAgent):
    def __init__(self, env, depth):
        super().__init__(env)
        self.depth = depth

    def addNode(self, node):
        if node.depth <= self.depth:
            self.frontier.append(node)


