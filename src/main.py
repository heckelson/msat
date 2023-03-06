import shutil
from argparse import ArgumentParser

from config.Config import config
from file_utils.filecollection import FileCollection
from file_utils.utils import create_output_dir_if_needed
from tasking.ImageScaleTask import ImageScaleTask


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-r', '--replace',
                        action="store_true",
                        help="Replace existing entries in the table.")

    parser.add_argument('-m', '--mediadir',
                        default='./media',
                        help="Override the directory in which the source "
                             "media is located (Default: './media')")

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
        shutil.rmtree(args.outputdir)
        return

    files = FileCollection(args.mediadir)
    create_output_dir_if_needed(args.outputdir)

    target_resolutions = [
        (1000, 1000),
        (800, 800),
        (600, 600),
        (400, 400),
        (200, 200)
    ]

    for file in files:
        ImageScaleTask(file, target_resolutions).run()


if __name__ == '__main__':
    main()
