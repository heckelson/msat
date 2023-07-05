import logging
import sys

IMAGE_FILE_ENDINGS = (
    '.jpeg',
    '.jpg',
    '.png'
)

NORMALIZATION_RESOLUTION = (1000, 1000)
NORMALIZED_IMAGE_OUTPUT_DIR_NAME = "tmp/normalized"


def configure_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)7s] %(name)-10s: %(message)s",
        stream=sys.stdout
    )
