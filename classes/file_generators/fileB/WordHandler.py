from typing import TYPE_CHECKING

# from classes.GNTWrapper import GNTWrapper
# from .PhraseHandler import PhraseHandler
from .WordPositionInGntPhrase import WordPositionInGntPhrase
from .WordPositionInLxxSubphrase import WordPositionInLxxSubphrase
from .WordPositionInLxxPhrase import WordPositionInLxxPhrase

if TYPE_CHECKING:
    from classes.Manager import Manager
    from .GntVerseHandler import GntVerseHandler

class WordHandler():

    # class static variables
    # do not delete: useful temporary functionality 
    MaxGntPhraseAnytypeNestLevelCount: int = 0

    def __init__(self
                 , manager: "Manager"
                 , word_id: int
                 , containing_verseHandler: "GntVerseHandler") -> None:
        
        # assigning received objects
        self._manager: "Manager" = manager
        self._word_id: int = word_id
        self._containing_verseHandler: "GntVerseHandler" = containing_verseHandler

        # local objects
        self._wordPositionInGntPhrase: WordPositionInGntPhrase = None
        self._wordPositionInLxxSubphrase: WordPositionInLxxSubphrase = None
        self._wordPositionInLxxPhrase: WordPositionInLxxPhrase = None
        self._compressedView: str = None

    @property
    def gntPhrasePosition(self) -> WordPositionInGntPhrase:

        if self._wordPositionInGntPhrase is None:
            self._wordPositionInGntPhrase = WordPositionInGntPhrase(self._manager, self._word_id, self._containing_verseHandler)
        return self._wordPositionInGntPhrase
    
    @property
    def lxxSubphrasePosition(self) -> WordPositionInLxxSubphrase:
        
        if self._wordPositionInLxxSubphrase is None:
            self._wordPositionInLxxSubphrase = WordPositionInLxxSubphrase(self._manager, self._word_id, self._containing_verseHandler, self.gntPhrasePosition)
        return self._wordPositionInLxxSubphrase
    
    @property
    def lxxPhrasePosition(self) -> WordPositionInLxxPhrase:
        
        if self._wordPositionInLxxPhrase is None:
            self._wordPositionInLxxPhrase = WordPositionInLxxPhrase(self._manager, self._word_id, self._containing_verseHandler, self.gntPhrasePosition)
        return self._wordPositionInLxxPhrase

    @property
    def compressedView(self) -> str:

        if self._compressedView is None:

            # this version shows subsuming nest level count for every word, for temporary technical analysis purposes -- useful line, do not delete
            # self._compressedView = f"{self.lxxSubphrasePosition.compressedView}c{self.gntPhrasePosition.phraseAnytypeNestLevelCount}"
            WordHandler.MaxGntPhraseAnytypeNestLevelCount = max(WordHandler.MaxGntPhraseAnytypeNestLevelCount, self.gntPhrasePosition.phraseAnytypeNestLevelCount)

            # self._compressedView = f"{self.lxxSubphrasePosition.compressedView}·{self.lxxPhrasePosition.compressedView}"
            self._compressedView = f"{self.lxxPhrasePosition.compressedView}"
        return self._compressedView
    

    