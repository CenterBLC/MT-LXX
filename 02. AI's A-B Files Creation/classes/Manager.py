"""Manager module."""
from .Settings import Settings
from .file_generators.FileA_Generator import FileA_Generator
from .file_generators.FileB_Generator import FileB_Generator
from .GNTWrapper import GNTWrapper
from .FeatureMerger import FeatureMerger
# from classes.file_writers.FileWriter import FileWriter

class Manager():

    def __init__(self):
        self._gnt_wrapper: GNTWrapper = None
        self._settings: Settings = None
        self._fileA_generator: FileA_Generator = None
        self._fileB_generator: FileB_Generator = None
        self._feature_merger: FeatureMerger = None
        # self._file_writer: FileWriter = None
        
    
    # @property
    # def file_writer(self) -> FileWriter:
    #     if self._file_writer is None:
    #         self._file_writer = FileWriter(self)
    #     return self._file_writer

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
    def gnt_wrapper(self) -> GNTWrapper:
        if self._gnt_wrapper is None:
            self._gnt_wrapper = GNTWrapper()
        return self._gnt_wrapper

    # keeping this instance here allows changing settings on the fly
    @property
    def settings(self) -> Settings:
        if self._settings is None:
            self._settings = Settings()
        return self._settings
    
    
