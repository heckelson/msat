from argparse import ArgumentParser

from file_utils import collect_filenames_in_dir, filter_nonmedia_files, create_output_dir


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

    filenames = collect_filenames_in_dir(args.mediadir)
    print(filter_nonmedia_files(filenames))

    create_output_dir(args.outputdir)
