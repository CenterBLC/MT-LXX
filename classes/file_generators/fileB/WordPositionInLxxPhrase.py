from typing import TYPE_CHECKING

from classes.GntApiWrapper import GntApiWrapper
from .GntPhraseHandler import GntPhraseHandler
from .WordPositionInGntPhrase import WordPositionInGntPhrase
from .dataclasses.WordPositionInPhraseLevelDescriptors import WordPositionInPhraseLevelDescriptors
from .dataclasses.WordPositionInPhraseLevelViews import WordPositionInPhraseLevelViews


if TYPE_CHECKING:
    from classes.Manager import Manager
    from .GntVerseHandler import GntVerseHandler
    from .WordHandler import WordHandler

class WordPositionInLxxPhrase():

    def __init__(self
                 , manager: "Manager"
                 , word_id: int
                 , containing_verseHandler: "GntVerseHandler"
                 , word_position_in_gntPhrase: WordPositionInGntPhrase) -> None:

        # assigning received objects        
        self._manager: "Manager" = manager
        self._word_id: int = word_id
        self._containing_verseHandler: "GntVerseHandler" = containing_verseHandler
        self._word_position_in_gntPhrase: WordPositionInGntPhrase = word_position_in_gntPhrase

        # local objects
        self._compressedView: str = None
        self._level_descriptors: WordPositionInPhraseLevelDescriptors = None
        self._level_compressed_views: WordPositionInPhraseLevelViews = None


    @property
    def levelDescriptors(self) -> WordPositionInPhraseLevelDescriptors:
        """
        Transferring the GNT multi-level syntactical structures 
        without change to the structures that will be applied to LXX
        """
        if self._level_descriptors is None:
            self._level_descriptors = self._word_position_in_gntPhrase.levelDescriptors
        return self._level_descriptors

    @property
    def levelCompressedViews(self) -> WordPositionInPhraseLevelViews:
        """
        Transferring the GNT multi-level compressed views 
        without change to the structures that will be applied to LXX
        """
        if self._level_compressed_views is None:
            self._level_compressed_views = self._word_position_in_gntPhrase.levelCompressedViews
        return self._level_compressed_views
    
    @property
    def compressedView(self) -> str:
        """
        'lxx phrase' is a virtual phrase of this program designed for training on GNT and later applied to LXX
        'lxx phrase' is calculated based on the current phrases of GNT, but is not always identical with them
        :return: 'X/Y' view for the 'lxx sub-phrases' now, and a more complex 'A/B" view for lxx sub-phrases, phrases, clauses, and sentences view later
        """

        # gntPhrPos = self._word_position_in_gntPhrase

        if self._compressedView is None: # and gntPhrPos is not None:
            
            compressed = "".join(lcv.compressedView.text for lcv in self.levelCompressedViews)
            self._compressedView = compressed if compressed else self._manager.settings._orphan_symbol # "∅" # ␀


            # self._compressedView = (
            #     "B" 
            #     if gntPhrPos.is_mostRight_element_in_gntPhrase # standard requirement
            #         or (gntPhrPos.is_without_subsuming_phrase and gntPhrPos.is_mostRight_in_a_nonPhrased_word_sequence) # e.g., 3 John 1:1: Γαΐῳ τῷ ἀγαπητῷ would otherwise create 'YYY' instead of 'XXY'
            #         # gntPhrPos.level

            #         # or gntSubphrPos.is_lastWord_before_phraseRupture # e.g., 3 John 1:4: phrase:254291 (word: 127310) μειζοτέραν (Y) -- ... -- χαράν
            #         # or gntSubphrPos.is_inside_phrase_but_is_lastWord_before_additionalPhraseAppears # e.g., 3 John 1:9 phrase 254330 (word 127376) ὁ (Y) 

            #     else "A"
            # )
        return self._compressedView

    