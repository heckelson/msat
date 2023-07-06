from dataclasses import dataclass, field

from model.resolution import ResampleConfiguration


@dataclass
class SampleImage:
    configuration: ResampleConfiguration = field()
    original_path: str = field()
    sample_path: str = field()
