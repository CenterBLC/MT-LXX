from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from classes.Manager import Manager

from classes.enums.DataLevel import DataLevel
from classes.enums.FileAMergeMode import FileAMergeMode

class FileWriterAbstract(ABC):

    def __init__(self, manager: "Manager") -> None:
        # self.data_level: DataLevel = manager.settings.data_level
        self._manager = manager
        self._selected_book: str = manager.settings.selected_book
        self._path_folder: str = manager.settings.path_folder
    
    @property
    def data_level(self) -> DataLevel:
        return self._manager.settings.data_level
    
    @abstractmethod
    def get_file_path(self) -> str:
        pass
    
    @abstractmethod
    def WriteContents(self, file_content: list[str]) -> None:
        
        full_path = self.get_file_path()

        # './data_gnt/input_' + selected_book + outputfile_suffix
        with open(full_path, 'w', encoding='utf-8') as file:
            for line in file_content:
                file.write(line + '\n')
        