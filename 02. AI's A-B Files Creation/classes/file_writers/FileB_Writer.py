from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from classes.Manager import Manager

from .FileWriterAbstract import FileWriterAbstract

from classes.enums.DataLevel import DataLevel
from classes.enums.FileBDisplayMode import FileBDisplayMode

class FileB_Writer(FileWriterAbstract):

    def __init__(self, manager: "Manager") -> None:
        super().__init__(manager)
        self._fileB_display_mode: FileBDisplayMode = manager.settings.fileB_display_mode
    
    def get_file_path(self) -> str:
        return f"./{self._path_folder}/fileB__{str(self.data_level if (self.data_level is DataLevel.NEW_TESTAMENT) else self._selected_book)}__{str(self._fileB_display_mode)}.txt"
    
    def WriteContents(self, file_content: list[str]) -> None:
        super().WriteContents(file_content)