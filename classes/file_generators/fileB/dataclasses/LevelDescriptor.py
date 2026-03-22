from dataclasses import dataclass
from classes.file_generators.fileB.GntPhraseHandler import GntPhraseHandler

@dataclass
class LevelDescriptor:
    """
    This class operates in the context of a syntactical structure
    (e.g., phrases/ clauses etc.) 
    containing the word as reported by Text-Fabric (subsuming structure), 
    as well as the structures that do not contain the word, 
    yet locate it within its extremetes (breaking structure). 

    isWordPhysicalPartOfSyntacticStructure (bool).
    For subsuming structure, this value is True.
    For breaking structure, this value is False.
    """
    syntacticalStructureId: int
    isWordPhysicalPartOfSyntacticStructure: bool
    gntPhraseHandler: GntPhraseHandler