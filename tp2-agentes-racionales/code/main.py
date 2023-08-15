from reflexiveAgent import ReflexiveAgent
from environment import Environment
import random

if __name__ == "__main__":
    # Constants
    env_sizes = [2**k for k in range (1,8)]
    dirt_rates = [0.1,0.2,0.4,0.8]
    iters = 10
    # Array to store performance
    performance = [[None for _ in range(len(env_sizes))] for _ in range(len(dirt_rates))]
    
    for i in range(len(dirt_rates)):
        for j in range(len(env_sizes)):
            size = env_sizes[j]

            # Store avg performance
            points = 0
            moves = 0
            clean_rate = 0
            
            for k in range(iters):
                env = Environment(size,size, dirt_rates[i])
                agent = ReflexiveAgent(random.randint(0,size-1),random.randint(0,size-1),env)
                points += agent.points
                moves += (1000 - agent.remaining_moves)
                clean_rate += 1 - (env.dirty_squares / env.initial_dirty_squares)
            
            performance[i][j] = [points/iters, moves/iters, clean_rate/iters]

    # Plot performance
    for line in performance:
        print(*line)
    

    