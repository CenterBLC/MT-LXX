from dataclasses import dataclass
from typing import ClassVar
from .LevelLetters import LevelLetters

@dataclass
class PhraseSyntacticStructureDefinitions:
    LEVELS: ClassVar[dict[int, LevelLetters]] = {
        0: LevelLetters(
            in_subsuming_structure="A", # A (U+0041)
            in_breaking_structure="Ȧ", # Ȧ (U+0226)
            end_of_structure="Ạ", # Ạ (U+1EA0)
        ),
        1: LevelLetters(
            in_subsuming_structure="B", # B (U+0042)
            in_breaking_structure="Ḃ", # Ḃ (U+1E02)
            end_of_structure="Ḅ", # Ḅ (U+1E04)
        ),
        2: LevelLetters(
            in_subsuming_structure="C", # C (U+0043)
            in_breaking_structure="Ċ", # Ċ (U+010A)
            end_of_structure="Ç" # Ç (U+00C7)  -- using cedilla (not a dot) below, because a dot below requires two unicode characters, and I only need one unicode character per character. AI will not differentiate between a cedilla and a dot.
        ),
        3: LevelLetters(
            in_subsuming_structure="D", # D (U+0044)
            in_breaking_structure="Ḋ", # Ḋ (U+1E0A)
            end_of_structure="Ḍ" # Ḍ (U+1E0C)
        ),
    }