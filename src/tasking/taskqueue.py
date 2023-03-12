from queue import Queue

from tasking.paralleltask import ParallelTask
from tasking.task import Task


class TaskQueue:
    def __init__(self):
        self.queue = Queue()

    def put(self, new_task: Task | ParallelTask):
        if isinstance(new_task, (Task, ParallelTask)):
            self.queue.put_nowait(new_task)
        else:
            raise AttributeError("TaskQueues can only hold Tasks or ParallelTasks!")

    def put_all(self, tasks: list[Task]):
        for task in tasks:
            self.put(task)

    def get(self) -> Task | ParallelTask:
        return self.queue.get_nowait()
