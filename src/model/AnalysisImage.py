import os
from typing import Self

from config import ANALYSIS_IMAGES_OUTPUT_DIR_NAME
from file_utils.utils import mkdir_p, get_only_filename, get_folder_path
from model.NormalizedImage import NormalizedImage
from model.SampleImage import SampleImage
from model.resolution import ResampleConfiguration


class AnalysisImage:
    def __init__(self, normalized_image: NormalizedImage,
                 target_configurations: list[ResampleConfiguration]):
        if not target_configurations:
            raise AttributeError("Cannot create analysis without any configurations!")

        self.original_filename = normalized_image.original_filename
        self.normalized_filename = normalized_image.export_filename
        self.normalized_image = normalized_image.image
        self.target_configurations = target_configurations

        self.sample_images: list[SampleImage] = []

    def calculate(self) -> Self:
        self.__resample_to_target_resolutions()

        return self

    def __resample_to_target_resolutions(self):
        # create a folder matching the name of the image in the analysis folder.

        only_filename = get_only_filename(self.normalized_filename)
        original_dir_no_filename = get_folder_path(self.original_filename)

        folder_name = f"{ANALYSIS_IMAGES_OUTPUT_DIR_NAME}{os.sep}" \
                      f"{original_dir_no_filename}{os.sep}{only_filename}"

        mkdir_p(folder_name)

        for configuration in self.target_configurations:
            ...  # TODO:
            # read config

            # resize

            # save to disk

            # add sample to collection
