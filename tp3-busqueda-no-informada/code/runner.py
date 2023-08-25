import concurrent.futures


class Runner:
    def __init__(self, iters, func):
        self.iters = iters
        self.func = func

    def run(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = [executor.submit(self.func) for _ in range(self.iters)]
            return [f.result() for f in future]
