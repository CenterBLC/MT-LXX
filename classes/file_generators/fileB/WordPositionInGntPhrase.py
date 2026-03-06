from typing import TYPE_CHECKING

from classes.GntApiWrapper import GntApiWrapper
from .GntPhraseHandler import GntPhraseHandler
from .dataclasses.WordPositionInPhraseLevelDescriptors import WordPositionInPhraseLevelDescriptors
from .dataclasses.WordPositionInPhraseLevelViews import WordPositionInPhraseLevelViews
from .dataclasses.LevelDescriptor import LevelDescriptor
from .dataclasses.LevelView import LevelView
from .dataclasses.CompressedView import CompressedView
from .dataclasses.PhraseSyntacticStructureDefinitions import PhraseSyntacticStructureDefinitions

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
        self._containing_subsuming_phraseHandlers: tuple[GntPhraseHandler] = None
        self._containing_anytype_phraseHandlers: tuple[GntPhraseHandler] = None
        self._is_without_subsuming_phrase: bool = None
        self._is_mostRight_element_in_gntPhrase: bool = None
        self._is_mostRight_in_a_nonPhrased_word_sequence: bool = None
        self._is_lastWord_before_phraseRupture: bool = None
        self._is_inside_phrase_but_is_lastWord_before_additionalPhraseAppears: bool = None
        self._phraseAnytypeNestLevelCount: int | None = None
        self._word_position_inPhrase_level_descriptors: WordPositionInPhraseLevelDescriptors = None
        self._word_position_inPhrase_level_compressedViews: WordPositionInPhraseLevelViews = None
        # self._nestedPhraseLevelCountAssigned: bool = False

    @property
    def levelDescriptors(self) -> WordPositionInPhraseLevelDescriptors:
        if self._word_position_inPhrase_level_descriptors is None:
            lds = WordPositionInPhraseLevelDescriptors()
            if self.containing_anytypePhraseHandlers is not None:
                for phrase_handler in sorted(self.containing_anytypePhraseHandlers, key=lambda ph: ph.phrase_id):
                    lds.add(LevelDescriptor(syntacticalStructureId=phrase_handler.phrase_id
                                            , isWordPhysicalPartOfSyntacticStructure=self._word_id in phrase_handler.words))
            self._word_position_inPhrase_level_descriptors = lds
        return self._word_position_inPhrase_level_descriptors
    
    @property
    def levelCompressedViews(self) -> WordPositionInPhraseLevelViews:
        if self._word_position_inPhrase_level_compressedViews is None:
            lcvs = WordPositionInPhraseLevelViews()
                                                        # self._manager
                                                        # #    , self._word_id
                                                        #    , self.subsequent_wordHandler
                                                        #    , self.levelDescriptors)

            for level_index, level_descriptor in enumerate(self.levelDescriptors):
                
                if level_index not in PhraseSyntacticStructureDefinitions.LEVELS:
                    raise IndexError(f"Level index {level_index} not found in PhraseSyntacticStructureDefinitions.LEVELS")

                subsequentWord_level_descriptor = (
                    self.subsequent_wordHandler.gntPhrasePosition.levelDescriptors[level_index]
                    if (self.subsequent_wordHandler 
                        and self.subsequent_wordHandler.gntPhrasePosition.levelDescriptors
                        and level_index < len(self.subsequent_wordHandler.gntPhrasePosition.levelDescriptors))
                    else None
                )
                
                is_same_structure_to_subsequent_Word = (
                    subsequentWord_level_descriptor and 
                    subsequentWord_level_descriptor.syntacticalStructureId == level_descriptor.syntacticalStructureId
                )
                
                compressedView: CompressedView = CompressedView(
                    PhraseSyntacticStructureDefinitions.LEVELS[level_index].end_of_structure
                    if not is_same_structure_to_subsequent_Word
                    else PhraseSyntacticStructureDefinitions.LEVELS[level_index].in_breaking_structure
                    if not level_descriptor.isWordPhysicalPartOfSyntacticStructure
                    else PhraseSyntacticStructureDefinitions.LEVELS[level_index].in_subsuming_structure
                )

                levelView = LevelView(level_descriptor, compressedView)
                lcvs.add(levelView)
                if (level_index != len (lcvs)-1):
                    raise IndexError(f"Level index {level_index} not found in WordPositionInPhraseLevelViews")
                
            self._word_position_inPhrase_level_compressedViews = lcvs
        return self._word_position_inPhrase_level_compressedViews

    @property
    def phraseAnytypeNestLevelCount(self) -> int:
        """
        Count None:     the Count has not been calcualted yet
        Count 0:        the word has no phrases
        Count 1:        the word has only 1 phrase
        Count 2:        the word has 2 phrases where the second phrase is nested under the first phrase
        ...
        Count Z:        the word has Z subnested phrases
        """
        if self._phraseAnytypeNestLevelCount is None:
            self._phraseAnytypeNestLevelCount = len(self.containing_anytypePhraseHandlers) if self.containing_anytypePhraseHandlers is not None else 0
        return self._phraseAnytypeNestLevelCount
    
    
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
            if (self.is_without_subsuming_phrase): 
                self._is_inside_phrase_but_is_lastWord_before_additionalPhraseAppears = False
            elif (self.subsequent_wordHandler is None):
                self._is_inside_phrase_but_is_lastWord_before_additionalPhraseAppears = False
            elif (self.is_mostRight_element_in_gntPhrase):
                self._is_inside_phrase_but_is_lastWord_before_additionalPhraseAppears = False
            # finally, calculating the property
            else:
                self._is_inside_phrase_but_is_lastWord_before_additionalPhraseAppears = (
                    len(self.subsequent_wordHandler.gntPhrasePosition.containing_subsumingPhraseHandlers) >
                    len(self.containing_subsumingPhraseHandlers)
                )
        return self._is_inside_phrase_but_is_lastWord_before_additionalPhraseAppears

    @property
    def is_lastWord_before_phraseRupture(self) -> bool:
        if self._is_lastWord_before_phraseRupture is None:
            if (self.is_without_subsuming_phrase): 
                self._is_lastWord_before_phraseRupture = False
            else:
                self._is_lastWord_before_phraseRupture = any(
                        self._word_id != phrase_handler.words[-1]
                        and (self._word_id + 1) not in phrase_handler.words
                        for phrase_handler in self.containing_subsumingPhraseHandlers
                    )
        return self._is_lastWord_before_phraseRupture
    
    @property
    def is_mostRight_element_in_gntPhrase(self) -> bool:
        if self._is_mostRight_element_in_gntPhrase is None:
            self._is_mostRight_element_in_gntPhrase = (
                self.containing_subsumingPhraseHandlers is not None and any(
                    phrase_handler.words[-1] == int(self._word_id)
                    for phrase_handler in self.containing_subsumingPhraseHandlers
                )
            )
        return self._is_mostRight_element_in_gntPhrase
    
    @property
    def is_without_subsuming_phrase(self) -> bool:
        if self._is_without_subsuming_phrase is None:
            self._is_without_subsuming_phrase = self.containing_subsumingPhraseHandlers is None
        return self._is_without_subsuming_phrase
    
    @property
    def is_mostRight_in_a_nonPhrased_word_sequence(self) -> bool:
        if self._is_mostRight_in_a_nonPhrased_word_sequence is None:
            if (not self.is_without_subsuming_phrase): # there is at least one phrase for this word
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
    def containing_anytypePhraseHandlers(self) -> tuple[GntPhraseHandler]:
        """
        "Anytype" includes both subsuming and breaking phrases.
        This method returns all types of phrases
        """
        if self._containing_anytype_phraseHandlers is None:
            self._containing_anytype_phraseHandlers = self._containing_verseHandler.getContaining_gntAnytypePhraseHandlers(self._word_id)
        return self._containing_anytype_phraseHandlers
    

    @property
    def containing_subsumingPhraseHandlers(self) -> tuple[GntPhraseHandler]:
        """
        Phrase handlers could be calculated through 
        phrases = L.u(w, otype='phrase')
        But creating phrase handlers by the parent Verse object ensures there is only one Phrase Handler instance per phrase across all objects
        """
        if self._containing_subsuming_phraseHandlers is None:
            self._containing_subsuming_phraseHandlers = self._containing_verseHandler.getContaining_gntSubsumingPhraseHandlers(self._word_id)
        return self._containing_subsuming_phraseHandlers
    