import logging
from multiprocessing import Pool

from tasking.Task import Task

log = logging.getLogger(__name__)


class ParallelTask(Task):
    def __init__(self, tasks: list[Task]):
        self.tasks = tasks

    def run_(self, task: Task):
        # This function is there so that we can
        # run tasks in the pool.map function.
        return task.run()

    def run(self):
        with Pool() as pool:
            pool.map(self.run_, self.tasks)
