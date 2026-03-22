from enum import Enum, auto

class SyntacticStructure(Enum):
    START_OF_STRUCTURE = auto()
    IN_SUBSUMING_STRUCTURE = auto()
    IN_BREAKING_STRUCTURE = auto()
    END_OF_STRUCTURE = auto()
