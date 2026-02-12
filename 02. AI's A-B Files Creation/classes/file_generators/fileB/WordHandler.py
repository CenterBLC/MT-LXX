from typing import TYPE_CHECKING

from classes.GNTWrapper import GNTWrapper
from .PhraseHandler import PhraseHandler

if TYPE_CHECKING:
    from classes.Manager import Manager
    from .VerseHandler import VerseHandler

class WordHandler():

    def __init__(self, manager: "Manager"
                 , word_id: int
                 , containing_verseHandler: "VerseHandler") -> None:
                #  , containing_phraseHandlers: tuple[PhraseHandler]
                #  , all_words_in_containing_verse: tuple[WordHandler]) -> None:
        self._manager: "Manager" = manager
        self._gnt_wrapper: GNTWrapper = manager.gnt_wrapper
        self._word_id: int = word_id
        
        # self._all_words_in_containing_verse: VerseHandler = all_words_in_containing_verse
        self._containing_verseHandler: "VerseHandler" = containing_verseHandler

        self._is_subsequent_wordHandler_calculated: bool = False
        self._subsequent_wordHandler: WordHandler = None
        
        self._containing_phraseHandlers: tuple[PhraseHandler] = None
        self._compressedView: str = None
        # self._is_inside_lxxPhrase: bool = None
        self._is_without_phrase: bool = None
        self._is_mostRight_element_in_aPhrase: bool = None
        # self._is_only_in_onePhrase_but_not_otherPhrase: bool = None
        self._is_mostRight_in_a_nonPhrased_word_sequence: bool = None
        self._is_lastWord_before_phraseRupture: bool = None
        self._is_lastWord_before_additionalPhraseAppears: bool = None
        
        
    
    @property
    def compressedView(self) -> str:
        """
        'lxx phrase' is a virtual phrase of this program designed for training on GNT and later applied to LXX
        'lxx phrase' is calculated based on the current phrases of GNT, but is not always identical with them
        :return: 'X/Y' view for the 'lxx sub-phrases' now, and a more complex 'A/B" view for lxx sub-phrases, phrases, clauses, and sentences view later
        """
        if self._compressedView is None:
            self._compressedView = (
                "Y" 
                if self.is_mostRight_element_in_aPhrase # standard requirement
                    or (self.is_without_phrase and self.is_mostRight_in_a_nonPhrased_word_sequence) # e.g., 3 John 1:1: Γαΐῳ τῷ ἀγαπητῷ would otherwise create 'YYY' instead of 'XXY'
                    # or self.is_only_in_onePhrase_but_not_otherPhrase # e.g., 3 John 1:9??? don't remember
                    or self.is_lastWord_before_phraseRupture # e.g., 3 John 1:4: phrase:254291 (word: 127310) μειζοτέραν (Y) -- ... -- χαράν
                    or self.is_lastWord_before_additionalPhraseAppears # e.g., 3 John 1:9 phrase 254330 (word 127376) ὁ (Y) 
                else "X"
            )
        return self._compressedView
    
    # @property
    # def is_inside_lxxPhrase(self) -> bool:
    #     if self._is_inside_lxxPhrase is None:
    #         self._is_inside_lxxPhrase = .............
    #     return self._is_inside_lxxPhrase
    
    @property
    def subsequent_wordHandler(self) -> "WordHandler":
        if not self._is_subsequent_wordHandler_calculated:
            self._subsequent_wordHandler = self._containing_verseHandler.get_subsequent_wordHandler(self._word_id)
            self._is_subsequent_wordHandler_calculated = True
        return self._subsequent_wordHandler

    @property
    def is_lastWord_before_additionalPhraseAppears(self) -> bool:
        if self._is_lastWord_before_additionalPhraseAppears is None:
            if (self.is_without_phrase): 
                self._is_lastWord_before_additionalPhraseAppears = False
            else:
                self._is_lastWord_before_additionalPhraseAppears = (
                    len(self.subsequent_wordHandler.containing_phraseHandlers) >
                    len(self.containing_phraseHandlers)
                )
        return self._is_lastWord_before_additionalPhraseAppears

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
    
    # @property
    # def is_only_in_onePhrase_but_not_otherPhrase(self) -> bool:
    #     if self._is_only_in_onePhrase_but_not_otherPhrase is None:
    #         if self.containing_phraseHandlers is None or len(self.containing_phraseHandlers) == 1:
    #             self._is_only_in_onePhrase_but_not_otherPhrase = False
    #         else:
    #             self._is_only_in_onePhrase_but_not_otherPhrase = (
    #                 len(self.containing_phraseHandlers) !=
    #                 len([ph for ph in self.containing_phraseHandlers if self._word_id in ph.words])
    #         )
    #     return self._is_only_in_onePhrase_but_not_otherPhrase
    
    @property
    def is_mostRight_element_in_aPhrase(self) -> bool:
        if self._is_mostRight_element_in_aPhrase is None:
            self._is_mostRight_element_in_aPhrase = (
                self.containing_phraseHandlers is not None and any(
                    phrase_handler.words[-1] == int(self._word_id)
                    for phrase_handler in self.containing_phraseHandlers
                )
            )
        return self._is_mostRight_element_in_aPhrase
    
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
                        for wh in self._containing_verseHandler.nonPhrased_wordHandlers
                    )
                )
        return self._is_mostRight_in_a_nonPhrased_word_sequence
    
    @property
    def containing_phraseHandlers(self) -> tuple[PhraseHandler]:
        """
        Phrase handlers could be calculated through 
        phrases = L.u(w, otype='phrase')
        But creating phrase handlers by the parent Verse object ensures there is only one Phrase Handler instance per phrase across all objects
        """
        if self._containing_phraseHandlers is None:
            self._containing_phraseHandlers = self._containing_verseHandler.getContaining_phraseHandlers(self._word_id)
            # raise Exception('_containing_phraseHandlers are expected to be supplied through the constructor')
        return self._containing_phraseHandlers
    