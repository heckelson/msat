from queue import Queue

from tasking.Task import Task


class TaskQueue:
    def __init__(self):
        self.queue = Queue()

    def put(self, new_task: Task):
        if isinstance(new_task, Task):
            self.queue.put_nowait(new_task)
        else:
            raise AttributeError("TaskQueues can only hold Tasks!")

    def put_all(self, tasks: list[Task]):
        for task in tasks:
            self.put(task)

    def get(self) -> Task:
        return self.queue.get_nowait()
