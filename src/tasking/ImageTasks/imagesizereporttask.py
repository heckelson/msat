import logging
import os
from dataclasses import dataclass, field

from file_utils.filecollection import FileCollection
from tasking.task import Task

log = logging.getLogger(__name__)


@dataclass
class ImageSizeReport:
    """
    A report holding the information for image sizes for an original image.

    "hash" contains the hash of the original image,
    "dict" maps a tuple (width, height) to the size in bytes.

    """
    hash: str
    file_sizes: dict[tuple[int, int], int] = field(default_factory=dict)

    def add_result(self, width, height, filesize):
        """
        A Helper function to simplify the interface to add new reports.
        """
        self.file_sizes[(width, height)] = filesize

    def __repr__(self):
        return f"{self.hash[:16]}: {self.file_sizes}"


class ImageSizeReportTask(Task):
    """
    Create a report of image sizes vs. file size for a collection of images.

    The directory structure should look like this:

        image_collection_path/
        ├── 059852fd920ff4afabb5168376e58a6f1e35cd4eb0d7e00a5306ed146d0ccab1
        │   ├── 1000x1000.png
        │   ├── 200x200.png
        │   ├── 400x400.png
        │   ├── 600x600.png
        │   └── 800x800.png
        ├── 0b1ae42f230153922d76527912b742268e2e1eba6d963ce4f535fead566b902d
        │   ├── 1000x1000.png
        │   ├── 200x200.png
        │   ├── 400x400.png
        ...

    So the files have the path format:
    <output_dir>/<media_out_dir>/<hash>/<width>x<height>.<type>
    """

    def __init__(self, directory: str):
        self.directory = directory

    def run(self):
        reports = []

        # the output collection is the folder with the hash of the input image
        for output_collection in os.listdir(self.directory):
            current_output_media_folder = f"{self.directory}{os.sep}{output_collection}"

            report = ImageSizeReport(output_collection)

            for filename in FileCollection(current_output_media_folder) \
                    .keep_relevant_files():
                width, height = filename \
                    .split('/')[-1] \
                    .split('.')[0] \
                    .split('x')
                width, height = int(width), int(height)

                image_size_bytes = os.path.getsize(filename)
                report.add_result(width, height, image_size_bytes)

            reports.append(report)

        log.info(f"Generated {len(reports)} image size reports.")
