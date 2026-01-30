from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from classes.Manager import Manager

from classes.GNTWrapper import GNTWrapper
from classes.file_writers.FileWriterAbstract import FileWriterAbstract
from classes.enums.DataLevel import DataLevel

from tf.core.nodefeature import NodeFeatures
from tf.core.locality import Locality
from tf.core.text import Text

class FileGeneratorAbstract(ABC):

    def __init__(self, manager: "Manager") -> None:
        self._manager: "Manager" = manager
        self._gnt_wrapper: GNTWrapper = manager.gnt_wrapper
        # self.data_level: DataLevel = manager.settings.data_level
        self._selected_book: str = manager.settings.selected_book
        self._file_writer: FileWriterAbstract = None
    
    @property
    def data_level(self) -> DataLevel:
        return self._manager.settings.data_level

    @property
    def F(self) -> NodeFeatures:
        return self._gnt_wrapper.F
    
    @property
    def L(self) -> Locality:
        return self._gnt_wrapper.L
    
    @property
    def T(self) -> Text:
        return self._gnt_wrapper.T

    @abstractmethod
    def generate(self) -> None:
        pass
