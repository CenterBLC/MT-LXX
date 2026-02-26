from typing import TYPE_CHECKING

from classes.GNTWrapper import GNTWrapper
from .PhraseHandler import PhraseHandler
from .WordHandler import WordHandler
from classes.enums.FileBDisplayMode import FileBDisplayMode

if TYPE_CHECKING:
    from classes.Manager import Manager

class VerseHandler():

    def __init__(self, manager: "Manager", verse_id: str) -> None:
        self._manager: "Manager" = manager
        self._gnt_wrapper: GNTWrapper = manager.gnt_wrapper
        self._verse_id: str = verse_id
        self._phrases: tuple[int] = None
        self._words: tuple[int] = None
        self._wordHandlers: tuple[WordHandler] = None
        self._phraseHandlers: tuple[PhraseHandler] = None

        self._nonPhrased_wordHandlers_calculated: bool = False
        self._nonPhrased_wordHandlers: tuple[WordHandler] = None
        # self._unused_words: list[int] = None

    def get_transformed_content(self) -> str:
        
        verse_text = ""

        strCompressedView: str = ""
        if (self._manager.settings.fileB_display_mode == FileBDisplayMode.COMPRESSED):
            tupleCompressed: tuple = tuple(wordHandler.compressedView for wordHandler in self.wordHandlers)
            strCompressedView = " ".join(tupleCompressed)
            verse_text = strCompressedView

        # dummy return
        # phrases_ofthe_verse: tuple = self._gnt_wrapper.L.d(self._verse_id, 'phrase')
        # for phrase_id in phrases_ofthe_verse:
        #     phrase_handler: PhraseHandler = PhraseHandler(self._manager, phrase_id)
        #     verse_text = f"{verse_text}{phrase_handler.abc()}"

        bo, ch, ve = self._gnt_wrapper.T.sectionFromNode(self._verse_id)
        res = "\t".join([bo, str(ch), str(ve), verse_text.strip()])
        return res
    
    @property
    def phraseHandlers(self) -> tuple[PhraseHandler]:
        if self._phraseHandlers is None:
            self._phraseHandlers = tuple(
                PhraseHandler(self._manager, phrase_id) for phrase_id in self.phrases
            )
        return self._phraseHandlers
    
    @property
    def wordHandlers(self) -> tuple[WordHandler]:
        if self._wordHandlers is None:
            res = list[WordHandler]()
            for word_id in self.words:
                res.append(WordHandler(self._manager
                                       , word_id
                                       , self))
            self._wordHandlers = tuple(res)
        return self._wordHandlers

    def getContaining_phraseHandlers(self, word_id: int) -> tuple[WordHandler]:
        containing_phraseHandlers = tuple(
                    phrase_handler for phrase_handler in self.phraseHandlers 
                    if word_id in phrase_handler.words
                ) or None # returns None if the tuple is empty
        return containing_phraseHandlers
    
    def get_subsequent_wordHandler(self, word_id: int) -> WordHandler:
        return next(
            (wh for wh in self.wordHandlers if wh._word_id == word_id + 1)
            , None
        )
    
    @property
    def nonPhrased_wordHandlers(self) -> tuple[WordHandler]:
        if not self._nonPhrased_wordHandlers_calculated:
        # if self._nonPhrased_words is None:
            self._nonPhrased_wordHandlers = tuple(
                    wh for wh in self.wordHandlers 
                    if wh.phrasePosition.is_without_phrase
                ) or None # returns None if the tuple is empty
            self._nonPhrased_wordHandlers_calculated = True
        return self._nonPhrased_wordHandlers

    @property
    def phrases(self) -> tuple[int]:
        if self._phrases is None:
            self._phrases = self._gnt_wrapper.L.d(self._verse_id, 'phrase')
        return self._phrases

    @property
    def words(self) -> tuple[int]:
        if self._words is None:
            self._words = self._gnt_wrapper.L.d(self._verse_id, 'word')
        return self._words

    # @property
    # def unused_words(self) -> list[int]:
    #     if self._unused_words is None:
    #         self._unused_words = list(self.words)
    #     return self._unused_words
    