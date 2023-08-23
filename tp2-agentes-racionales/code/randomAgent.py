from agent import Agent
import random


class RandomAgent(Agent):
    def think(self):
        match random.randint(0, 5):
            case 0:
                self.up()
            case 1:
                self.down()
            case 2:
                self.left()
            case 3:
                self.right()
            case 4:
                self.suck()
            case 5:
                self.idle()
