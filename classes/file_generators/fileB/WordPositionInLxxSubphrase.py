from typing import TYPE_CHECKING

from classes.GntApiWrapper import GntApiWrapper
from .GntPhraseHandler import GntPhraseHandler
from .WordPositionInGntPhrase import WordPositionInGntPhrase
from .dataclasses.SubphraseSyntacticStructureDefinitions import SubphraseSyntacticStructureDefinitions
from .enums.SyntacticStructure import SyntacticStructure

if TYPE_CHECKING:
    from classes.Manager import Manager
    from .GntVerseHandler import GntVerseHandler
    from .WordHandler import WordHandler

class WordPositionInLxxSubphrase():

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
        self._is_previous_wordHandler_calculated: bool = False
        self._previous_wordHandler: WordHandler = None
        self._is_most_right_word_calculated: bool = False
        self._is_most_right_word: bool | None = None
        self._is_most_left_word_calculated: bool = False
        self._is_most_left_word: bool | None = None

    @property
    def previous_wordHandler(self) -> "WordHandler":
        if not self._is_previous_wordHandler_calculated:
            self._previous_wordHandler = self._containing_verseHandler.get_previous_wordHandler(self._word_id)
            self._is_previous_wordHandler_calculated = True
        return self._previous_wordHandler

    @property
    def isMostRightWord(self) -> bool:
        """
        Not inheriting the subphrases' structure from GNT unchnaged, but modifying it to make it better and building not on GNT subphrases (which are too many), but on GNT phrases.
        """
        if not self._is_most_right_word_calculated:
            gntPhrPos = self._word_position_in_gntPhrase
            if gntPhrPos is not None:
                self._is_most_right_word = (gntPhrPos.is_mostRight_element_in_gntPhrase # standard requirement
                        or (gntPhrPos.is_without_subsuming_phrase and gntPhrPos.is_mostRight_in_a_nonPhrased_word_sequence) # e.g., 3 John 1:1: Γαΐῳ τῷ ἀγαπητῷ would otherwise create 'YYY' instead of 'XXY'
                        # or phrasePos.is_only_in_onePhrase_but_not_otherPhrase # e.g., 3 John 1:9??? don't remember -- but this is a confirmed superflous condition which is probably covered by other conditions
                        or gntPhrPos.is_lastWord_before_phraseRupture # e.g., 3 John 1:4: phrase:254291 (word: 127310) μειζοτέραν (Y) -- ... -- χαράν
                        or gntPhrPos.is_inside_phrase_but_is_lastWord_before_additionalPhraseAppears # e.g., 3 John 1:9 phrase 254330 (word 127376) ὁ (Y) 
                )
            self._is_most_right_word_calculated = True
        return self._is_most_right_word
    
    @property
    def isMostLeftWord(self) -> bool:
        """
        The most left word can simultaneously be the most right word, when there is only one word in the subphrase.
        """
        if not self._is_most_left_word_calculated:
            if self.previous_wordHandler is None:
                self._is_most_left_word = True
            elif self.previous_wordHandler.lxxSubphrasePosition.isMostRightWord:
                self._is_most_left_word = True
            else:
                self._is_most_left_word = False
            self._is_most_left_word_calculated = True
        return self._is_most_left_word

    @property
    def compressedView(self) -> str:
        """
        'lxx phrase' is a virtual phrase of this program designed for training on GNT and later applied to LXX
        'lxx phrase' is calculated based on the current phrases of GNT, but is not always identical with them
        :return: 'X/Y' view for the 'lxx sub-phrases' now, and a more complex 'A/B" view for lxx sub-phrases, phrases, clauses, and sentences view later
        """


        if self._compressedView is None:
            if self.isMostRightWord is not None:
                self._compressedView = (

                    self.getStructureSymbolAccordingToSettings(SyntacticStructure.END_OF_STRUCTURE)
                    if self.isMostRightWord

                    else self.getStructureSymbolAccordingToSettings(SyntacticStructure.START_OF_STRUCTURE)
                    if self.isMostLeftWord # that is, it is not simuletaneously the most right word

                    else self.getStructureSymbolAccordingToSettings(SyntacticStructure.IN_SUBSUMING_STRUCTURE)
                )
            else:
                self._compressedView = "not_defined"
        return self._compressedView

    def getStructureSymbolAccordingToSettings(self, structure_part: SyntacticStructure) -> str:
        
        if structure_part == SyntacticStructure.START_OF_STRUCTURE:
            if self._manager.settings.fileB_include_structurePart_start:
                return SubphraseSyntacticStructureDefinitions.start_of_structure
            else:
                return self._manager.settings.orphan_symbol
        
        if structure_part == SyntacticStructure.END_OF_STRUCTURE:
            if self._manager.settings.fileB_include_structurePart_end:
                return SubphraseSyntacticStructureDefinitions.end_of_structure
            else:
                return self._manager.settings.orphan_symbol
        
        if structure_part == SyntacticStructure.IN_SUBSUMING_STRUCTURE:
            if self._manager.settings.fileB_include_structurePart_subsuming:
                return SubphraseSyntacticStructureDefinitions.in_subsuming_structure
            else:
                return self._manager.settings.orphan_symbol
        
        # there is no breaking structure notion in subphrases
        # if structure_part == SyntacticStructure.IN_BREAKING_STRUCTURE:
        #     if self._manager.settings.fileB_include_structurePart_breaking:
        #         return SubphraseSyntacticStructureDefinitions.in_breaking_structure
        #     else:
        #         return self._manager.settings.orphan_symbol
            
        raise Exception(f"Unknown structure_part {structure_part}")
    