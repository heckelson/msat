import hashlib
import os


# TODO: We could wrap all this stuff in a FileCollection class?

def collect_filenames_in_dir(start_dir: str) -> list[str]:
    """
    This function returns all filenames starting from a directory
    if given a directory, or just a list with 1 element
    if given a file.

    This function is taken and modified from my MRE course.
    Copyright Alexander Hecke 2022.
    """

    if not os.path.exists(start_dir):
        raise ValueError("The start directory does not exist!")

    if os.path.isdir(start_dir):
        # gather files down the file tree
        file_collection = []
        for path, _, files in os.walk(start_dir):
            for file in files:
                file_collection.append(f"{path}{os.sep}{file}")

        # replace double // with single / for consistency
        file_collection = [filename.replace(f'{os.sep}{os.sep}', f'{os.sep}')
                           for filename in file_collection]

    else:
        # else we just put the filename into an array of size 1
        file_collection = [start_dir]

    return file_collection


def filter_nonmedia_files(filenames: list, allowed_file_endings: tuple[str] = None) -> list:
    """
    Filters filenames according to their file endings.
    One can optionally pass a tuple of file endings to override the default endings,
    which are (jpeg, jpg, png)
    """

    if allowed_file_endings is None:
        allowed_file_endings = ('jpeg', 'jpg', 'png')

    # this works only with tuples!
    filtered_files = list(filter(
        lambda file: file.lower().endswith(allowed_file_endings), filenames))

    return filtered_files


def create_output_dir(output_path: str = "out/"):
    if not os.path.exists(output_path):
        os.mkdir(output_path)


def sha256hash(filename: str) -> str:
    h = hashlib.sha256()

    with open(filename, 'rb') as file:
        while chunk := file.read():
            h.update(chunk)

        return h.hexdigest()
