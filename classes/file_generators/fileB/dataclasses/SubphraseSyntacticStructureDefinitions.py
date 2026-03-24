from dataclasses import dataclass
from typing import ClassVar
from .LevelLetters import LevelLetters

@dataclass
class SubphraseSyntacticStructureDefinitions:
    start_of_structure="Y" # Y U+0059
    in_subsuming_structure="Ỹ" # Ỹ U+1EF8

    # there is no breaking parts within a subphrase
    # in_breaking_structure="", 

    end_of_structure="Ỵ" # Ỵ U+1EF4