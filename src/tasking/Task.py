from abc import ABC, abstractmethod


class Task(ABC):
    """
    A Strategy pattern used to queue up different types of tasks, be it resizing,
    saving to disk and writing to the database, or changing the color space of different
    source media.
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass
