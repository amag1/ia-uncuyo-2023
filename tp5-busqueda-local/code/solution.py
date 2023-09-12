class Solution:
    def __init__(self, value, fitness):
        self.fitness = fitness
        self.value = value
    
    def __str__(self):
        return "Value: " + str(self.value) + " Fitness: " + str(self.fitness)
    
    def __lt__(self, other):
        return self.fitness < other.fitness