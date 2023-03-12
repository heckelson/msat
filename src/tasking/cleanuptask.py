import os
import shutil

from config import config
from tasking.task import Task


class CleanupTask(Task):
    def __init__(self, root_path: str):
        self.root_path = root_path

    def run(self):
        if os.path.exists(config.get('outputdir')):
            shutil.rmtree(config.get('outputdir'))
            print("All clean!")
        else:
            print("Nothing to clean!")
