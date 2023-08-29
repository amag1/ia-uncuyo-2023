import multiprocessing

class Runner:
    def __init__(self, iters, func,env_list):
        self.iters = iters
        self.func = func
        self.env_list = env_list
        
    def run(self):
        with multiprocessing.Pool() as p:
            return p.map(self.func,self.env_list)
