"""Manager module."""
from .Settings import Settings
from .file_generators.FileA_Generator import FileA_Generator
from .file_generators.FileB_Generator import FileB_Generator
from .GntApiWrapper import GntApiWrapper
from .FeatureMerger import FeatureMerger
# from .file_generators.fileB.WordsAllocationToPhrases import WordsAllocationToPhrases
# from classes.file_writers.FileWriter import FileWriter

class Manager():

    def __init__(self):
        self._gnt_wrapper: GntApiWrapper = None
        self._settings: Settings = None
        self._fileA_generator: FileA_Generator = None
        self._fileB_generator: FileB_Generator = None
        self._feature_merger: FeatureMerger = None
        # self._words_allocation_to_phrases: WordsAllocationToPhrases = None
        
    
    # @property
    # def words_allocation_to_phrases(self) -> WordsAllocationToPhrases:
    #     if self._words_allocation_to_phrases is None:
    #         self._words_allocation_to_phrases = WordsAllocationToPhrases(self)
    #     return self._words_allocation_to_phrases

    @property
    def feature_merger(self) -> FeatureMerger:
        if self._feature_merger is None:
            self._feature_merger = FeatureMerger(self)
        return self._feature_merger

    @property
    def fileB_generator(self) -> FileB_Generator:
        if self._fileB_generator is None:
            self._fileB_generator = FileB_Generator(self)
        return self._fileB_generator

    @property
    def fileA_generator(self) -> FileA_Generator:
        if self._fileA_generator is None:
            self._fileA_generator = FileA_Generator(self)
        return self._fileA_generator

    # expensive resource
    @property
    def gnt_wrapper(self) -> GntApiWrapper:
        if self._gnt_wrapper is None:
            self._gnt_wrapper = GntApiWrapper()
        return self._gnt_wrapper

    # keeping this instance here allows changing settings on the fly
    @property
    def settings(self) -> Settings:
        if self._settings is None:
            self._settings = Settings()
        return self._settings
    
    
