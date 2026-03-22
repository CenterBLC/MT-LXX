from typing import TYPE_CHECKING

from classes.GntApiWrapper import GntApiWrapper

if TYPE_CHECKING:
    from classes.Manager import Manager

class GntPhraseHandler():
    """
    The class includes all words found between the extremeties of the phrase (that is, including the words not physically belonging to the phrase if found between those extremeties)
    """
    def __init__(self, manager: "Manager", phrase_id: str) -> None:
        self._manager: "Manager" = manager
        self._gnt_wrapper: GntApiWrapper = manager.gnt_wrapper
        self._phrase_id: str = phrase_id
        self._words: tuple = None    
        self._the_most_right_word: int = None
        self._the_most_left_word: int = None

    @property
    def phrase_id(self) -> str:
        return self._phrase_id
    
    @property
    def words(self) -> tuple:
        if self._words is None:
            self._words = self._gnt_wrapper.L.d(self._phrase_id, 'word')
        return self._words
    
    @property
    def theMostRightWord(self) -> int:
        if self._the_most_right_word is None:
            self._the_most_right_word = max (self.words)
        return self._the_most_right_word

    @property
    def theMostLeftWord(self) -> int:
        if self._the_most_left_word is None:
            self._the_most_left_word = min (self.words)
        return self._the_most_left_word