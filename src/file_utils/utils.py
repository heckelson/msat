import hashlib
import os


def create_output_dir(output_path: str = None):
    if output_path is None:
        raise ValueError("Output path cannot be None!")

    if not os.path.exists(output_path):
        os.mkdir(output_path)


def sha256hash(filename: str) -> str:
    h = hashlib.sha256()

    with open(filename, 'rb') as file:
        while chunk := file.read():
            h.update(chunk)

        return h.hexdigest()
