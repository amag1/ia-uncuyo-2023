import random
# Agente racional que implementa la clase abstracta agent
from agent import Agent

class ReflexiveAgent(Agent):
    def think(self):
        if self.perspective():
            self.suck()
        else:
            action = random.randint(0,4)
            match action:
                case 0:
                    self.up()
                case 1:
                    self.down()
                case 2:
                    self.left()
                case 3:
                    self.right()
