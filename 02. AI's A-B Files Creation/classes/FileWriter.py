from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Manager import Manager

from .Settings import Settings
from .enums.DataLevel import DataLevel
from .enums.FileAMergeMode import FileAMergeMode

class FileWriter():

    def __init__(self, manager: "Manager") -> None:
        self._data_level: DataLevel = manager.settings.data_level
        self._selected_book: str = manager.settings.selected_book
        self._path_folder: str = manager.settings.path_folder
        self._fileA_merge_mode: FileAMergeMode = manager.settings.fileA_merge_mode
    
    def WriteContents(self, file_contents: list[str]) -> None:


        full_path = f"./{self._path_folder}/fileA__{str(self._data_level if self._data_level is DataLevel.NEW_TESTAMENT else self._selected_book)}__{str(self._fileA_merge_mode)}"

        # './data_gnt/input_' + selected_book + outputfile_suffix
        with open(full_path, 'w', encoding='utf-8') as file:
            for line in file_contents:
                file.write(line + '\n')
        