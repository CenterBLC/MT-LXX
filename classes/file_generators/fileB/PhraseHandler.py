from typing import TYPE_CHECKING

from classes.GNTWrapper import GNTWrapper

if TYPE_CHECKING:
    from classes.Manager import Manager

class PhraseHandler():

    def __init__(self, manager: "Manager", phrase_id: str) -> None:
        self._manager: "Manager" = manager
        self._gnt_wrapper: GNTWrapper = manager.gnt_wrapper
        self._phrase_id: str = phrase_id
        self._words: tuple = None
    
    def abc(self):
        return "abc"
    
    @property
    def words(self) -> tuple:
        if self._words is None:
            self._words = self._gnt_wrapper.L.d(self._phrase_id, 'word')
        return self._words