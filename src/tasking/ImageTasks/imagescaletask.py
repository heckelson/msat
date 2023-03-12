import logging
import os

from PIL import Image

from config import config
from file_utils.utils import sha256hash, create_output_dir_if_needed
from tasking.task import Task

log = logging.getLogger(__name__)


class ImageScaleTask(Task):
    """
    A task that rescales the target image to specific width-height pairs.
    """

    def __init__(self, image_path: str, target_resolutions: list[tuple[int, int]]):
        """
        :param image_path: The path of the image for which the task is going to run.
        :param target_resolutions: A list of (width, height) tuples that determine
        the target image resolutions.
        """
        self.image_path = image_path
        self.target_resolutions = target_resolutions
        pass

    def run(self):
        if not os.path.isfile(self.image_path):
            raise FileNotFoundError(f"Can not find image: {self.image_path}")

        # create the right folder structure
        media_dir = f"{config.get('outputdir')}" \
                    f"{os.sep}{config.get('OUTPUT_MEDIA_DIRNAME')}"
        create_output_dir_if_needed(media_dir)

        # calculate an image's hash, creating a folder for each unique hash.
        file_hash = sha256hash(self.image_path)
        unique_folder_location = f"{media_dir}{os.sep}{file_hash}"
        create_output_dir_if_needed(unique_folder_location)

        # if everything is set, we can start working now!
        with Image.open(self.image_path) as image:
            image_format = image.format.lower()

            for res in self.target_resolutions:
                width, height = res

                output_name = f"{unique_folder_location}{os.sep}" \
                              f"{width}x{height}.{image_format}"

                if os.path.exists(output_name) and os.path.isfile(output_name):
                    log.warning(f"Skipping already existing file :`{output_name}`")
                    continue

                log.debug(f"Scaling image {self.image_path} to ({width}, {height}).")
                scaled_image = image.resize(size=(width, height))

                if scaled_image.format == "JPEG":
                    scaled_image.save(output_name, quality="keep")
                else:
                    scaled_image.save(output_name, optimize=False)
