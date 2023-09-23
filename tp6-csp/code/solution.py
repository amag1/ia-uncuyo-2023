from typing import Any


class Solution:
    value = None
    steps = None
    time = None

    def __init__(self, value, steps, time ):
        self.value = value
        self.steps = steps
        self.time = time

    def __str__(self):
        return "Solution: " + str(self.value) + " found in " + str(self.steps) + " steps in " + str(self.time) + " seconds"
        
    
    

