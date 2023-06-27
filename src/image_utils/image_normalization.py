from PIL import Image


class NormalizedImage:
    def __init__(self, filename: str):
        self.__filename = filename

    def __normalize(self):
        image = Image.open(self.__filename)
        image.show()
