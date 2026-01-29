from enum import Enum
from .enums.DataLevel import DataLevel
from .enums.FileAMergeMode import FileAMergeMode
from .enums.FileBDisplayMode import FileBDisplayMode


class Settings():
    
    def __init__(self):
        self._data_level: DataLevel = DataLevel.NT_BOOK
        # III_John
        # Matthew
        self._selected_book: str = 'III_John'
        self._fileA_merge_mode: FileAMergeMode = FileAMergeMode.NLCGPNMST
        self._fileB_display_mode: FileBDisplayMode = FileBDisplayMode.CODED
        self._path_folder: str = "sp_data_gnt"

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
    
    @property
    def fileA_merge_mode(self) -> FileAMergeMode:
        return self._fileA_merge_mode
