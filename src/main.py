import os
import queue
from argparse import ArgumentParser

from config import config
from file_utils.filecollection import FileCollection
from file_utils.utils import create_output_dir_if_needed
from tasking import CleanupTask
from tasking.ImageTasks import ImageScaleTask
from tasking.ImageTasks import ImageSizeReportTask
from tasking.paralleltask import ParallelTask
from tasking.taskqueue import TaskQueue


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
        CleanupTask(config.get('outputdir')).run()

        return

    full_output_media_dir = f"{args.outputdir}{os.sep}{config.get('OUTPUT_MEDIA_DIRNAME')}"

    config['FULL_OUTPUT_MEDIA_DIR'] = full_output_media_dir

    # set up dir structure for the outputs
    create_output_dir_if_needed(config.get('outputdir'))
    create_output_dir_if_needed(config.get('FULL_OUTPUT_MEDIA_DIR'))

    task_queue = TaskQueue()

    target_resolutions = [
        (1000, 1000),
        (800, 800),
        (600, 600),
        (400, 400),
        (200, 200)
    ]

    files = FileCollection(args.mediadir).keep_relevant_files()
    task_queue.put(ParallelTask([
        ImageScaleTask(file, target_resolutions) for file in files
    ]))

    task_queue.put(ImageSizeReportTask(full_output_media_dir))

    try:
        while task := task_queue.get():
            task.run()
    except queue.Empty:
        pass


if __name__ == '__main__':
    main()
