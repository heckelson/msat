import logging
import os

from PIL.Image import Image

from config import NORMALIZATION_RESOLUTION, NORMALIZED_IMAGE_OUTPUT_DIR_NAME
from file_utils.utils import get_folder_path, mkdir_p
from model.ImageFile import ImageFile

log = logging.getLogger(__name__)


def find_center(image: Image) -> tuple[int, int]:
    """
    :param image: The image to analyze.
    :return: A tuple containing the coordinates of the center, rounded down
     if the resolution is even. First element is x, second element is y.
    """
    return (image.width - 1) // 2, (image.height - 1) // 2


class ImageTooSmallException(Exception):
    pass


class NormalizedImage:
    def __init__(self, image_file: ImageFile):
        # set the file paths and image data
        self.original_filename = image_file.filename
        self.export_filename = f"{NORMALIZED_IMAGE_OUTPUT_DIR_NAME}{os.sep}{self.original_filename}"
        self.export_filename = self.export_filename.replace(f"{os.sep}.{os.sep}", os.sep)

        self.image = image_file.image

        log.info(f"Normalizing image `{self.original_filename}`")
        log.debug(f"File output: `{self.export_filename}`")

        # do the operations
        self.__crop_image_to_target()
        self.__standardize_color_format()

    def __crop_image_to_target(self):
        """
        Crops the image to the resolution specified in NORMALIZATION_RESOLUTION.

        :raises ImageTooSmallException: if the image is smaller than that resolution.
        """
        width = self.image.width
        height = self.image.height

        target_x = NORMALIZATION_RESOLUTION[0]
        target_y = NORMALIZATION_RESOLUTION[1]

        if width < target_x or height < target_y:
            raise ImageTooSmallException(f"Image is too small. "
                                         f"Required: {NORMALIZATION_RESOLUTION}, "
                                         f"Yours: {(width, height)}.")
        # find center
        center = find_center(self.image)

        # find out the min and max x and y coordinates to crop correctly
        half_width = target_x // 2
        half_height = target_y // 2

        max_x = center[0] + half_width
        max_y = center[1] + half_height

        if target_x % 2:
            min_x = center[0] - half_width - 1
        else:
            min_x = center[0] - half_width

        if target_y % 2:
            min_y = center[1] - half_height - 1
        else:
            min_y = center[1] - half_width

        # actually crop the image.
        self.image = self.image.crop((min_x, min_y, max_x, max_y))

    def __standardize_color_format(self):
        folder_name = get_folder_path(self.export_filename)

        mkdir_p(folder_name)

        self.image.save(self.export_filename)
