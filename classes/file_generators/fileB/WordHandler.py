from typing import TYPE_CHECKING

# from classes.GNTWrapper import GNTWrapper
# from .PhraseHandler import PhraseHandler
from .WordPositionInPhrase import WordPositionInPhrase

if TYPE_CHECKING:
    from classes.Manager import Manager
    from .VerseHandler import VerseHandler

class WordHandler():

    def __init__(self
                 , manager: "Manager"
                 , word_id: int
                 , containing_verseHandler: "VerseHandler") -> None:
        
        # assigning received objects
        self._manager: "Manager" = manager
        self._word_id: int = word_id
        self._containing_verseHandler: "VerseHandler" = containing_verseHandler

        # creating aggregated objects
        # wrapper of functionality / properties relating to various syntactical positions of the word
        self._wordPositionInPhrase = WordPositionInPhrase(self._manager, self._word_id, self._containing_verseHandler)
        
        # local functions
        self._compressedView: str = None

        # obsolete code
        # self._gnt_wrapper: GNTWrapper = manager.gnt_wrapper
    
    @property
    def phrasePosition(self) -> WordPositionInPhrase:
        return self._wordPositionInPhrase

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
                if self.phrasePosition.is_mostRight_element_in_aPhrase # standard requirement
                    or (self.phrasePosition.is_without_phrase and self.phrasePosition.is_mostRight_in_a_nonPhrased_word_sequence) # e.g., 3 John 1:1: Γαΐῳ τῷ ἀγαπητῷ would otherwise create 'YYY' instead of 'XXY'
                    # or phrasePos.is_only_in_onePhrase_but_not_otherPhrase # e.g., 3 John 1:9??? don't remember -- but this is a confirmed superflous condition which is probably covered by other conditions
                    or self.phrasePosition.is_lastWord_before_phraseRupture # e.g., 3 John 1:4: phrase:254291 (word: 127310) μειζοτέραν (Y) -- ... -- χαράν
                    or self.phrasePosition.is_inside_phrase_but_lastWord_before_additionalPhraseAppears # e.g., 3 John 1:9 phrase 254330 (word 127376) ὁ (Y) 

                else "X"
            )
        return self._compressedView
    
    

    