from dataclasses import dataclass

@dataclass(frozen=True)
class LevelLetters:
    start_of_structure: str
    in_subsuming_structure: str
    in_breaking_structure: str
    end_of_structure: str