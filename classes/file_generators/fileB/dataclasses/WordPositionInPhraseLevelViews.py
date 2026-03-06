from typing import Iterator
from typing import TYPE_CHECKING

from .WordPositionInPhraseLevelDescriptors import WordPositionInPhraseLevelDescriptors
from .LevelDescriptor import LevelDescriptor
from .LevelView import LevelView

if TYPE_CHECKING:
    from classes.Manager import Manager
    from ..GntVerseHandler import GntVerseHandler
    from ..WordHandler import WordHandler

class WordPositionInPhraseLevelViews():
    """
    The indexer of this class (or its internal list) is the 
    level number (int): 0...Z. 

    The len(this class) is the number of syntactical structure levels.
    Compressed View 0 is the view of the topmost structure,
    Compressed View Z is the view of the lowest strusture that is the more immediate to the word.
    """
    def __init__(self) -> None:
                #  , manager: "Manager"
                # #  , word_id: int
                #  , subsequent_wordHandler: "WordHandler"
                #  , word_position_inPhrase_level_descriptors: WordPositionInPhraseLevelDescriptors) -> None:

        # # assigning received objects        
        # self._manager: "Manager" = manager
        # # self._word_id: int = word_id
        # self._subsequent_wordHandler: "WordHandler" = subsequent_wordHandler
        # self._word_position_inPhrase_level_descriptors = word_position_inPhrase_level_descriptors

        # local objects
        self._levelViews: list[LevelView] = []

    def add(self, levelView: LevelView):
        self._levelViews.append(levelView)

    def __getitem__(self, index: int) -> LevelView:
        return self._levelViews[index]

    def __setitem__(self, index: int, value: LevelView):
        self._levelViews[index] = value
    
    def __iter__(self) -> Iterator[LevelView]:
        return iter(self._levelViews)

    def __len__(self):
        return len(self._levelViews)
