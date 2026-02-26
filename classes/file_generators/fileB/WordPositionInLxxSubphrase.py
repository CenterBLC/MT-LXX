from typing import TYPE_CHECKING

from classes.GntApiWrapper import GntApiWrapper
from .GntPhraseHandler import GntPhraseHandler
from .WordPositionInGntSubphrase import WordPositionInGntSubphrase

if TYPE_CHECKING:
    from classes.Manager import Manager
    from .GntVerseHandler import GntVerseHandler
    from .WordHandler import WordHandler

class WordPositionInLxxSubphrase():

    def __init__(self
                 , manager: "Manager"
                 , word_id: int
                 , containing_verseHandler: "GntVerseHandler"
                 , word_position_in_gntSubphrase: WordPositionInGntSubphrase) -> None:

        # assigning received objects        
        self._manager: "Manager" = manager
        self._word_id: int = word_id
        self._containing_verseHandler: "GntVerseHandler" = containing_verseHandler
        self._word_position_in_gntSubphrase: WordPositionInGntSubphrase = word_position_in_gntSubphrase

        # local objects
        self._compressedView: str = None

    @property
    def compressedView(self) -> str:
        """
        'lxx phrase' is a virtual phrase of this program designed for training on GNT and later applied to LXX
        'lxx phrase' is calculated based on the current phrases of GNT, but is not always identical with them
        :return: 'X/Y' view for the 'lxx sub-phrases' now, and a more complex 'A/B" view for lxx sub-phrases, phrases, clauses, and sentences view later
        """

        gntSubphrPos = self._word_position_in_gntSubphrase

        if self._compressedView is None and gntSubphrPos is not None:
            self._compressedView = (
                "Y" 
                if gntSubphrPos.is_mostRight_element_in_gntPhrase # standard requirement
                    or (gntSubphrPos.is_without_phrase and gntSubphrPos.is_mostRight_in_a_nonPhrased_word_sequence) # e.g., 3 John 1:1: Γαΐῳ τῷ ἀγαπητῷ would otherwise create 'YYY' instead of 'XXY'
                    # or phrasePos.is_only_in_onePhrase_but_not_otherPhrase # e.g., 3 John 1:9??? don't remember -- but this is a confirmed superflous condition which is probably covered by other conditions
                    or gntSubphrPos.is_lastWord_before_phraseRupture # e.g., 3 John 1:4: phrase:254291 (word: 127310) μειζοτέραν (Y) -- ... -- χαράν
                    or gntSubphrPos.is_inside_phrase_but_lastWord_before_additionalPhraseAppears # e.g., 3 John 1:9 phrase 254330 (word 127376) ὁ (Y) 

                else "X"
            )
        return self._compressedView

    