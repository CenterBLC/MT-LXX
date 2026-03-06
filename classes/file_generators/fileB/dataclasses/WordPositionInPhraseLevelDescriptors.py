from typing import Iterator

from .LevelDescriptor import LevelDescriptor

class WordPositionInPhraseLevelDescriptors():
    """
    The indexer of this class (or its internal list) is the 
    level number (int): 0...Z. 

    The len(this class) is the number of syntactical structure levels.
    Level 0 is the topmost structure,
    Level Z is the lowest strusture that is the more immediate to the word.
    """
    def __init__ (self) -> None:
        self._levels: list[LevelDescriptor] = []

    def add(self, levelDescriptor: LevelDescriptor):
        if not isinstance(levelDescriptor, LevelDescriptor):
            raise TypeError("Value must be a LevelDescriptor")
        self._levels.append(levelDescriptor)

    def __getitem__(self, index: int) -> LevelDescriptor:
        return self._levels[index]

    def __setitem__(self, index: int, value: LevelDescriptor):
        if not isinstance(value, LevelDescriptor):
            raise TypeError("Value must be a LevelDescriptor")
        self._levels[index] = value
    
    def __iter__(self) -> Iterator[LevelDescriptor]:
        return iter(self._levels)

    def __len__(self):
        return len(self._levels)