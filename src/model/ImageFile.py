from PIL import Image

from config import IMAGE_FILE_ENDINGS


class NotAnImageFileException(Exception):
    pass


class ImageFile:
    def __init__(self, filepath):
        if not self.is_image_filepath(filepath):
            raise NotAnImageFileException("The file is not an image file!")

        self.image = Image.open(filepath)
        self.filename = filepath

    @staticmethod
    def is_image_filepath(filepath: str) -> bool:
        return filepath.endswith(IMAGE_FILE_ENDINGS)

    def __repr__(self):
        return f"ImageFile({self.filename})"
