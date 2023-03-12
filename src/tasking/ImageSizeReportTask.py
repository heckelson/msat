import os

from tasking.Task import Task


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
        print(os.listdir('./out/generated_media'))

    def run(self):
        pass  # TODO
