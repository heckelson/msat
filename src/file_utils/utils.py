import hashlib
import os


def mkdir_p(output_path: str = None):
    if output_path is None:
        raise ValueError("Output path cannot be None!")

    if not os.path.exists(output_path):
        os.makedirs(output_path)


def sha256hash(filename: str) -> str:
    h = hashlib.sha256()

    with open(filename, 'rb') as file:
        while chunk := file.read():
            h.update(chunk)

        return h.hexdigest()


def get_folder_path(filename: str) -> str:
    return os.sep.join(filename.split(os.sep)[:-1])


def get_only_filename(filename: str) -> str:
    return filename.split(os.sep)[-1]
