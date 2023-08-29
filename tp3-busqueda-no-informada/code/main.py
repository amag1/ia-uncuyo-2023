from runner import Runner
from environment import Environment
import agents as a
from resultoptions import *
import time

SIZE = 100
ITERS = 100
OBSTACLE_RATE = 0.08


def run_bfs(env):
    agent = a.BFSAgent(env)
    return agent.findPath()

def run_dfs(env):
    agent = a.DFSAgent(env)
    return agent.findPath()

def run_dfs_limited(env):
    agent = a.DFSLimitedAgent(env, 2000)
    return agent.findPath()

def run_uniform(env):
    agent = a.UniformAgent(env)
    return agent.findPath()

def get_results():
    env_list = [Environment(OBSTACLE_RATE, SIZE) for _ in range(ITERS)]
    r = []
    
    print("Running BFS")
    runner = Runner(ITERS, run_bfs, env_list)
    r.append(runner.run())

    print("Running DFS")
    runner = Runner(ITERS, run_dfs, env_list)
    r.append(runner.run())

    print("Running DFS Limited")
    runner = Runner(ITERS, run_dfs_limited, env_list)
    r.append(runner.run())

    print("Running Uniform cost")
    runner = Runner(ITERS, run_uniform, env_list)
    r.append(runner.run())

    print("Done!")

    return r



if __name__ == "__main__":
    t = time.time()

    results = get_results()
    csv_write(results)

    print(f"Time elapsed: {time.time() - t}")

    
    box_args = [(res[0][0], [r[2] for r in res]) for res in results]
    boxplot(box_args)
