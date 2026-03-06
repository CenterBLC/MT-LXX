from dataclasses import dataclass

@dataclass(frozen=True)
class LevelLetters:
    in_subsuming_structure: str
    in_breaking_structure: str
    end_of_structure: str