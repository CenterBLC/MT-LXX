from enum import Enum
from .enums.DataLevel import DataLevel
from .enums.FileAMergeMode import FileAMergeMode
from .enums.FileBDisplayMode import FileBDisplayMode


class Settings():
    
    def __init__(self):
        self._data_level: DataLevel = DataLevel.NEW_TESTAMENT
        self._selected_book: str = 'III_John' # III_John # Matthew
        self._fileA_merge_mode: FileAMergeMode = FileAMergeMode.NLCGPNMST
        self._fileB_display_mode: FileBDisplayMode = FileBDisplayMode.COMPRESSED
        self._path_folder: str = "sp_data_gnt"


        self._fileB_include_lxxSubphrases: bool = False

        self._fileB_include_lxxPhrases: bool = True
        self._fileB_include_lxxPhrases_level0: bool = True
        self._fileB_include_lxxPhrases_level1: bool = False
        self._fileB_include_lxxPhrases_level2: bool = False
        self._fileB_include_lxxPhrases_level3: bool = False

        self._fileB_include_structurePart_subsuming: bool = False
        self._fileB_include_structurePart_breaking: bool = False
        self._fileB_include_structurePart_end: bool = True

        # 3-byte alternative: ∅ (U+2205) (3 bytes); 
        # 2-bytes alternatives: Ø (U+00D8); ø (U+00F8); 
        # 1-byte alternative: ~ (Tilde - U+007E); . (Period / Full Stop - U+002E); | (Vertical Line / Pipe - U+007C); 0 (Zero - U+0030 [used now])
        self._orphan_symbol = "0"  

    @property
    def orphan_symbol(self) -> str:
        return self._orphan_symbol

    @property
    def fileB_include_structurePart_subsuming(self) -> bool:
        return self._fileB_include_structurePart_subsuming

    @property
    def fileB_include_structurePart_breaking(self) -> bool:
        return self._fileB_include_structurePart_breaking

    @property
    def fileB_include_structurePart_end(self) -> bool:
        return self._fileB_include_structurePart_end


    @property
    def fileB_include_lxxSubphrases(self) -> bool:
        return self._fileB_include_lxxSubphrases

    @property
    def fileB_include_lxxPhrases(self) -> bool:
        return self._fileB_include_lxxPhrases

    @property
    def fileB_include_lxxPhrases_level0(self) -> bool:
        return self._fileB_include_lxxPhrases_level0

    @property
    def fileB_include_lxxPhrases_level1(self) -> bool:
        return self._fileB_include_lxxPhrases_level1

    @property
    def fileB_include_lxxPhrases_level2(self) -> bool:
        return self._fileB_include_lxxPhrases_level2

    @property
    def fileB_include_lxxPhrases_level3(self) -> bool:
        return self._fileB_include_lxxPhrases_level3

    @property
    def fileB_display_mode(self) -> FileBDisplayMode:
        return self._fileB_display_mode
    
    @property
    def path_folder(self) -> str:
        return self._path_folder

    @property
    def selected_book(self) -> str:
        return self._selected_book
    
    @property
    def data_level(self) -> DataLevel:
        return self._data_level
    @data_level.setter
    def data_level(self, value):
        if isinstance(value, str):
            value = DataLevel[value]
        self._data_level = value
    
    @property
    def fileA_merge_mode(self) -> FileAMergeMode:
        return self._fileA_merge_mode
