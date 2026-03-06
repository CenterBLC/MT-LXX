from dataclasses import dataclass
from .CompressedView import CompressedView
from .LevelDescriptor import LevelDescriptor
from .CompressedView import CompressedView

@dataclass
class LevelView:
    levelDescriptor: LevelDescriptor
    compressedView: CompressedView