from collections import namedtuple
from dataclasses import dataclass, field
from enum import Enum, auto

Resolution = namedtuple("Resolution", ['x', 'y'])


class ResampleMethod(Enum):
    NEAREST_NEIGHBOR = auto()
    BILINEAR = auto()
    BICUBIC = auto()


class ImageFileType(Enum):
    JPEG = ".jpg"
    PNG = ".png"


@dataclass
class ResampleConfiguration:
    resolution: Resolution = field()
    method: ResampleMethod = field()
    image_file_type: ImageFileType = field()
