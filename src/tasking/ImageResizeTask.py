import os

from PIL import Image

from config.Config import config
from file_utils.utils import sha256hash, create_output_dir_if_needed
from tasking.Task import Task


class ImageResizeTask(Task):
    def __init__(self):
        pass

    def run(self, image_name: str):
        # we wanna have the output dir ready
        output_dir = config.get("outputdir")

        # calculate an image's hash, creating a folder for each unique hash.
        file_hash = sha256hash(image_name)
        unique_folder_location = f"{output_dir}{os.sep}{file_hash}"
        create_output_dir_if_needed(unique_folder_location)

        with Image.open(image_name) as image:
            width = image.width
            height = image.height
            image_format = image.format.lower()

            # we want scales from 0.1, 0.2, ... to 1.0 and up to 2.0.
            for i in range(1, 21):
                scale_factor = i / 10
                scaled_width = int(scale_factor * width)
                scaled_height = int(scale_factor * height)

                # scale the image
                scaled_image = image.resize(size=(scaled_width, scaled_height))
                # and write to the file.
                output_name = f"{unique_folder_location}{os.sep}" \
                              f"{scale_factor}_{scaled_width}x{scaled_height}.{image_format}"
                scaled_image.save(output_name)
