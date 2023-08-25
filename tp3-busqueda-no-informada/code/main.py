from runner import Runner
from environment import Environment
import agents as a
import time
import statistics

SIZE = 100
ITERS = 30
OBSTACLE_RATE = 0.2


def run_bfs():
    env = Environment(OBSTACLE_RATE, SIZE)
    agent = a.BFSAgent(env)
    return agent.getPath()


if __name__ == "__main__":
    t = time.time()
    runner = Runner(ITERS, run_bfs)
    results = runner.run()

    print(f'Running time: {time.time() - t} seconds')

    null_results = 0
    for result in results:
        if result is None:
            null_results += 1

    print(f'Null results: {null_results}/{ITERS}')

    steps = [result[2] for result in results if result is not None]
    print(f'Mean steps: {statistics.mean(steps)}')
    print(f'Std steps: {statistics.stdev(steps)}')
