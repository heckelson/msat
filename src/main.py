import logging
import queue
import shutil
from argparse import ArgumentParser

from config.Config import config
from file_utils.filecollection import FileCollection
from file_utils.utils import create_output_dir_if_needed
from tasking.ImageScaleTask import ImageScaleTask
from tasking.ImageSizeReportTask import ImageSizeReportTask
from tasking.TaskQueue import TaskQueue

logging.basicConfig(level=logging.DEBUG)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-r', '--replace',
                        action="store_true",
                        help="Replace existing files in the file system as well as "
                             "database entries, if applicable. Basically redoes all "
                             "the work.")

    parser.add_argument('-m', '--mediadir',
                        default='./media',
                        help="Override the directory in which the source media is "
                             "located (Default: './media')")

    parser.add_argument('-o', '--outputdir',
                        default='./out',
                        help="Override the output directory for files created by "
                             "the program (SQLite DB, working files, etc.).")

    parser.add_argument('-c', '--clean',
                        action="store_true",
                        help="Clean out the output directory.")

    return parser.parse_args()


def main():
    args = parse_args()
    config.update(**args.__dict__)

    if args.clean:
        # if we have the "clean" argument set, remove the output dir and do
        # nothing else.
        shutil.rmtree(args.outputdir)
        return

    files = FileCollection(args.mediadir).keep_relevant_files()
    create_output_dir_if_needed(args.outputdir)

    task_queue = TaskQueue()

    target_resolutions = [
        (1000, 1000),
        (800, 800),
        (600, 600),
        (400, 400),
        (200, 200)
    ]

    for file in files:
        task_queue.put(ImageScaleTask(file, target_resolutions))

    task_queue.put(ImageSizeReportTask(args.outputdir))

    try:
        while task := task_queue.get():
            task.run()
    except queue.Empty:
        pass


if __name__ == '__main__':
    main()
