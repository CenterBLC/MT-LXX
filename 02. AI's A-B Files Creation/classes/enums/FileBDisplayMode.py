from enum import Enum, auto

class FileBDisplayMode(Enum):
    COMPRESSED = auto()
    PLAIN_TEXT = auto()

    def __str__(self) -> str:
        return self.name.title().lower()