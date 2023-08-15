from abc import ABC, abstractmethod


class Agent(ABC):
    def __init__(self, posX, posY, env):
        if not isinstance(posX, int) or not isinstance(posY, int):
            raise TypeError("posX and posY must be integers")
        if posX < 0 or posY < 0:
            raise ValueError("posX and posY must be positive")
        self.posX = posX
        self.posY = posY
        self.env = env
        self.points = 0
        self.remaining_moves = 1000

        while self.remaining_moves > 0 and env.dirty_squares > 0:
            self.think()

    def up(self):
        if self.env.accept_action(self.posX, self.posY, "UP"):
            self.posY += 1

        self.remaining_moves -= 1

    def down(self):
        if self.env.accept_action(self.posX, self.posY, "DOWN"):
            self.posY -= 1

        self.remaining_moves -= 1

    def left(self):
        if self.env.accept_action(self.posX, self.posY, "LEFT"):
            self.posX -= 1

        self.remaining_moves -= 1

    def right(self):
        if self.env.accept_action(self.posX, self.posY, "RIGHT"):
            self.posX += 1

        self.remaining_moves -= 1

    def suck(self):
        if self.env.accept_action(self.posX, self.posY, "SUCK"):
            self.points += 1

        self.remaining_moves -= 1

    def idle(self):
        self.remaining_moves -= 1

    def perspective(self):
        return self.env.is_dirty(self.posX, self.posY)

    @abstractmethod
    def think():
        pass
