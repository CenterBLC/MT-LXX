from typing import TYPE_CHECKING

# from classes.GNTWrapper import GNTWrapper
# from .PhraseHandler import PhraseHandler
from .WordPositionInGntSubphrase import WordPositionInGntSubphrase
from .WordPositionInLxxSubphrase import WordPositionInLxxSubphrase

if TYPE_CHECKING:
    from classes.Manager import Manager
    from .GntVerseHandler import GntVerseHandler

class WordHandler():

    def __init__(self
                 , manager: "Manager"
                 , word_id: int
                 , containing_verseHandler: "GntVerseHandler") -> None:
        
        # assigning received objects
        self._manager: "Manager" = manager
        self._word_id: int = word_id
        self._containing_verseHandler: "GntVerseHandler" = containing_verseHandler

        # local objects
        self._wordPositionInGntSubphrase: WordPositionInGntSubphrase = None
        self._wordPositionInLxxSubphrase: WordPositionInLxxSubphrase = None
        self._compressedView: str = None

    @property
    def gntSubphrasePosition(self) -> WordPositionInGntSubphrase:

        if self._wordPositionInGntSubphrase is None:
            self._wordPositionInGntSubphrase = WordPositionInGntSubphrase(self._manager, self._word_id, self._containing_verseHandler)
        return self._wordPositionInGntSubphrase
    
    @property
    def lxxSubphrasePosition(self) -> WordPositionInLxxSubphrase:
        
        if self._wordPositionInLxxSubphrase is None:
            self._wordPositionInLxxSubphrase = WordPositionInLxxSubphrase(self._manager, self._word_id, self._containing_verseHandler, self.gntSubphrasePosition)
        return self._wordPositionInLxxSubphrase

    @property
    def compressedView(self) -> str:

        if self._compressedView is None:
            self._compressedView = f"{self.lxxSubphrasePosition.compressedView}"
        return self._compressedView
    
    

    