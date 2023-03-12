import os
import queue
import shutil
from argparse import ArgumentParser

from config.config import config
from file_utils.filecollection import FileCollection
from file_utils.utils import create_output_dir_if_needed
from tasking.ImageTasks.imagescaletask import ImageScaleTask
from tasking.ImageTasks.imagesizereporttask import ImageSizeReportTask
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
        # if we have the "clean" argument set, remove the output dir and do
        # nothing else.
        shutil.rmtree(args.outputdir)
        return

    generated_media_dir = f"{args.outputdir}{os.sep}{config.get('OUTPUT_MEDIA_DIRNAME')}"

    # set up dir structure for the outputs
    create_output_dir_if_needed(args.outputdir)
    create_output_dir_if_needed(generated_media_dir)

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

    task_queue.put(ImageSizeReportTask(generated_media_dir))

    try:
        while task := task_queue.get():
            task.run()
    except queue.Empty:
        pass


if __name__ == '__main__':
    main()
