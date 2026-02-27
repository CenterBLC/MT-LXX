from typing import TYPE_CHECKING

from classes.GntApiWrapper import GntApiWrapper
from .GntPhraseHandler import GntPhraseHandler

if TYPE_CHECKING:
    from classes.Manager import Manager
    from .GntVerseHandler import GntVerseHandler
    from .WordHandler import WordHandler

class WordPositionInGntPhrase():

    def __init__(self
                 , manager: "Manager"
                 , word_id: int
                 , containing_verseHandler: "GntVerseHandler") -> None:

        # assigning received objects        
        self._manager: "Manager" = manager
        self._word_id: int = word_id
        self._containing_verseHandler: "GntVerseHandler" = containing_verseHandler

        # local objects
        self._compressedView: str = None
        self._is_subsequent_wordHandler_calculated: bool = False
        self._subsequent_wordHandler: WordHandler = None
        self._containing_phraseHandlers: tuple[GntPhraseHandler] = None
        self._is_without_phrase: bool = None
        self._is_mostRight_element_in_gntPhrase: bool = None
        self._is_mostRight_in_a_nonPhrased_word_sequence: bool = None
        self._is_lastWord_before_phraseRupture: bool = None
        self._is_inside_phrase_but_is_lastWord_before_additionalPhraseAppears: bool = None
        self._phraseSubsumingNestLevelCount: int | None = None
        # self._nestedPhraseLevelCountAssigned: bool = False

    @property
    def phraseSubsumingNestLevelCount(self) -> int:
        """
        Level None:     the Count has not been calcualted yet
        Level 0:        the word has no phrases
        Level 1:        the word has only 1 phrase
        Level 2:        the word has 2 phrases where the second phrase is nested under the first phrase
        ...
        Level Z:        the word has Z subnested phrases
        """
        if self._phraseSubsumingNestLevelCount is None:
            # stoppedAt: 
            # read all the phraseHandlers from the verseHandler (ref. self.containing_phraseHandlers) 
            # and assign levels according to the ascending order of the phraseHandler's id's 
            self._phraseSubsumingNestLevelCount = len(self.containing_phraseHandlers) if self.containing_phraseHandlers is not None else 0
        return self._phraseSubsumingNestLevelCount
    
    @property
    def subsequent_wordHandler(self) -> "WordHandler":
        if not self._is_subsequent_wordHandler_calculated:
            self._subsequent_wordHandler = self._containing_verseHandler.get_subsequent_wordHandler(self._word_id)
            self._is_subsequent_wordHandler_calculated = True
        return self._subsequent_wordHandler

    @property
    def is_inside_phrase_but_is_lastWord_before_additionalPhraseAppears(self) -> bool:
        if self._is_inside_phrase_but_is_lastWord_before_additionalPhraseAppears is None:
            # first, ruling out scenarios that are not relevant for this property
            if (self.is_without_phrase): 
                self._is_inside_phrase_but_is_lastWord_before_additionalPhraseAppears = False
            elif (self.subsequent_wordHandler is None):
                self._is_inside_phrase_but_is_lastWord_before_additionalPhraseAppears = False
            elif (self.is_mostRight_element_in_gntPhrase):
                self._is_inside_phrase_but_is_lastWord_before_additionalPhraseAppears = False
            # finally, calculating the property
            else:
                self._is_inside_phrase_but_is_lastWord_before_additionalPhraseAppears = (
                    len(self.subsequent_wordHandler.gntPhrasePosition.containing_phraseHandlers) >
                    len(self.containing_phraseHandlers)
                )
        return self._is_inside_phrase_but_is_lastWord_before_additionalPhraseAppears

    @property
    def is_lastWord_before_phraseRupture(self) -> bool:
        if self._is_lastWord_before_phraseRupture is None:
            if (self.is_without_phrase): 
                self._is_lastWord_before_phraseRupture = False
            else:
                self._is_lastWord_before_phraseRupture = any(
                        self._word_id != phrase_handler.words[-1]
                        and (self._word_id + 1) not in phrase_handler.words
                        for phrase_handler in self.containing_phraseHandlers
                    )
        return self._is_lastWord_before_phraseRupture
    
    @property
    def is_mostRight_element_in_gntPhrase(self) -> bool:
        if self._is_mostRight_element_in_gntPhrase is None:
            self._is_mostRight_element_in_gntPhrase = (
                self.containing_phraseHandlers is not None and any(
                    phrase_handler.words[-1] == int(self._word_id)
                    for phrase_handler in self.containing_phraseHandlers
                )
            )
        return self._is_mostRight_element_in_gntPhrase
    
    @property
    def is_without_phrase(self) -> bool:
        if self._is_without_phrase is None:
            self._is_without_phrase = self.containing_phraseHandlers is None
        return self._is_without_phrase
    
    @property
    def is_mostRight_in_a_nonPhrased_word_sequence(self) -> bool:
        if self._is_mostRight_in_a_nonPhrased_word_sequence is None:
            if (not self.is_without_phrase): # there is at least one phrase for this word
                self._is_mostRight_in_a_nonPhrased_word_sequence = False
            else:
                self._is_mostRight_in_a_nonPhrased_word_sequence = not ( #negation
                    any(# there is a non-phrased word to the right of the current word
                        wh._word_id == self._word_id + 1
                        for wh in self._containing_verseHandler.nonGntPhrased_wordHandlers
                    )
                )
        return self._is_mostRight_in_a_nonPhrased_word_sequence
    
    @property
    def containing_phraseHandlers(self) -> tuple[GntPhraseHandler]:
        """
        Phrase handlers could be calculated through 
        phrases = L.u(w, otype='phrase')
        But creating phrase handlers by the parent Verse object ensures there is only one Phrase Handler instance per phrase across all objects
        """
        if self._containing_phraseHandlers is None:
            self._containing_phraseHandlers = self._containing_verseHandler.getContaining_gntPhraseHandlers(self._word_id)
        return self._containing_phraseHandlers
    