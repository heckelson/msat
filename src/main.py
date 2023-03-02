from argparse import ArgumentParser

from file_utils.filecollection import FileCollection
from file_utils.utils import create_output_dir


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

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    files = FileCollection(args.mediadir)
    create_output_dir(args.outputdir)

    files.keep_files_with_ending_in()
