import logging
import sys

from model.resolution import Resolution, ResampleConfiguration, ResampleMethod, ImageFileType

IMAGE_FILE_ENDINGS = (
    '.jpeg',
    '.jpg',
    '.png'
)

NORMALIZATION_RESOLUTION = Resolution(1000, 1000)
NORMALIZED_IMAGE_OUTPUT_DIR_NAME = "tmp/normalized"

ANALYSIS_IMAGES_OUTPUT_DIR_NAME = "tmp/analysis"

ANALYSIS_CONFIGURATIONS: list[ResampleConfiguration] = [
    ResampleConfiguration(
        Resolution(1000, 1000), ResampleMethod.BILINEAR, ImageFileType.JPEG),
    ResampleConfiguration(
        Resolution(800, 800), ResampleMethod.BILINEAR, ImageFileType.JPEG),
    ResampleConfiguration(
        Resolution(600, 600), ResampleMethod.BILINEAR, ImageFileType.JPEG),
    ResampleConfiguration(
        Resolution(400, 400), ResampleMethod.BILINEAR, ImageFileType.JPEG),
    ResampleConfiguration(
        Resolution(200, 200), ResampleMethod.BILINEAR, ImageFileType.JPEG),
    ResampleConfiguration(
        Resolution(100, 100), ResampleMethod.BILINEAR, ImageFileType.JPEG),
    ResampleConfiguration(
        Resolution(50, 50), ResampleMethod.BILINEAR, ImageFileType.JPEG),
]


def configure_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [ %(levelname)5s ] %(name)-10s: %(message)s",
        stream=sys.stdout
    )
