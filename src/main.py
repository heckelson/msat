"""
msat - The Multimedia Storage Analysis Toolkit
===

This program consists of a couple of distinct stages.

1. Normalization Stage

In the first stage, input images are read from disk and normalized,
which creates the following images:
* 24-bit full RGB (no chroma subsampling)
* 1500x1500 px

2. Processing Stage

Creation of Resampled images for analysis

This step is a bit interwoven with the 3rd step, however there should
be some tasks available for each image in the pipeline:

* Downsizing using NN, Bilinear, Bicubic, and some more!
* Upsizing using NN, Bilinear, Bicubic, and some more!
* Color spaces; YCrCb, and different chroma subsampling ratios
* Image aware scaling methods?

3. Analysis Stage

Analysis of the created images

The images shall be analyzed according to different parameters, the storage
space is the first parameter we're investigating.

4. Report Generation

From all the analysis information, a report shall be generated (1) showing
some statistics, graphics, etc. and (2) the data shall be exported in a
standard data exchange format (i.e., JSON). This allows for easy further analysis
in some other context, most likely a Jupyter notebook.

"""

import logging

from config import configure_logger
from file_utils.filecollection import FileCollection
from file_utils.utils import mkdir_p
from image_utils.image_normalization import NormalizedImage

configure_logger()

log = logging.getLogger(__name__)


def main():
    """Main function"""
    setup_directories()

    # collect files from input folder
    files = FileCollection("./media")
    files = files.keep_relevant_files()

    start_normalization_stage(files)
    start_processing_stage(files)
    start_analysis_stage(files)
    start_report_stage(files)


def setup_directories():
    """
    Create needed directories to work in.
    """
    # temporary working files
    mkdir_p("./tmp")

    # output for reports etc.
    mkdir_p("./out")


def start_normalization_stage(image_files: FileCollection):
    log.info(f"Starting normalization stage on {len(image_files)} files.")

    mkdir_p("./tmp/normalized")

    for i, image in enumerate(image_files):
        NormalizedImage(image)


def start_processing_stage(files: FileCollection):
    log.info(f"Starting processing stage on {len(files)} files.")


def start_analysis_stage(files: FileCollection):
    log.info(f"Starting analysis stage on {len(files)} files.")


def start_report_stage(files: FileCollection):
    log.info(f"Starting reporting stage on {len(files)} files.")


if __name__ == '__main__':
    main()
