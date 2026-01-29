from enum import Enum, auto

class FileBDisplayMode(Enum):
    CODED = auto()
    TEXTED = auto()

    def __str__(self) -> str:
        return self.name.title().lower()