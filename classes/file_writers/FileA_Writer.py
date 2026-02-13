from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from classes.Manager import Manager

from .FileWriterAbstract import FileWriterAbstract

from classes.enums.DataLevel import DataLevel
from classes.enums.FileAMergeMode import FileAMergeMode

class FileA_Writer(FileWriterAbstract):

    def __init__(self, manager: "Manager") -> None:
        super().__init__(manager)
        self._fileA_merge_mode: FileAMergeMode = manager.settings.fileA_merge_mode
    
    def get_file_path(self) -> str:
        return f"./{self._path_folder}/fileA__{str(self.data_level if (self.data_level is DataLevel.NEW_TESTAMENT) else self._selected_book)}__{str(self._fileA_merge_mode)}.txt"
    
    def WriteContents(self, file_content: list[str]) -> None:
        super().WriteContents(file_content)