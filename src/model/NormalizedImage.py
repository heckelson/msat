import logging
import os
from typing import Self

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
        self.__determine_export_filename()
        self.image = image_file.image

    def calculate(self) -> Self:
        log.debug(f"Normalizing image `{self.original_filename}`")
        log.debug(f"File output: `{self.export_filename}`")
        self.__crop_image_to_target_resolution()
        self.__standardize_format_and_write_to_disk()
        return self

    def __determine_export_filename(self):
        filepath_without_ending = ".".join(
            self.original_filename.split(".")[:-1])

        self.export_filename = f"{NORMALIZED_IMAGE_OUTPUT_DIR_NAME}" \
                               f"{os.sep}" \
                               f"{filepath_without_ending}.png"
        self.export_filename = self.export_filename.replace(f"{os.sep}.{os.sep}", os.sep)

    def __crop_image_to_target_resolution(self):
        """
        Crops the image to the resolution specified in NORMALIZATION_RESOLUTION.

        :raises ImageTooSmallException: if the image is smaller than that resolution.
        """
        width = self.image.width
        height = self.image.height

        target_x = NORMALIZATION_RESOLUTION.x
        target_y = NORMALIZATION_RESOLUTION.y

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

    def __standardize_format_and_write_to_disk(self):
        """
        Converts the images to 3x8bpp RGB images. We also strip the alpha channel.

        As per the Pillow documentation, "Pillow doesn’t yet support
        multichannel images with a depth of more than 8 bits per channel",
        hence this choice.
        """

        # "RGB" is the 3x8 color mode.
        if self.image.mode != "RGB":
            self.image = self.image.convert(mode="RGB")

        # create folder if necessary
        folder_name = get_folder_path(self.export_filename)
        mkdir_p(folder_name)

        self.image.save(self.export_filename, mode="RGB")
