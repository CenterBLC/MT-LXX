from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from classes.Manager import Manager

from classes.GntApiWrapper import GntApiWrapper
from classes.file_writers.FileWriterAbstract import FileWriterAbstract
from classes.enums.DataLevel import DataLevel

from tf.core.nodefeature import NodeFeatures
from tf.core.locality import Locality
from tf.core.text import Text

class FileGeneratorAbstract(ABC):

    def __init__(self, manager: "Manager") -> None:
        self._manager: "Manager" = manager
        self._gnt_wrapper: GntApiWrapper = manager.gnt_wrapper
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

    def _merge_duplicate_verses(self, raw_verses: list[str]) -> list[str]:
        """
        Helper method inherited by all File Generators.
        Catches and concatenates tags/text for verses that share 
        the exact same book, chapter, and verse address.
        This method was created due to the GNT's I_Peter 4:1 that was found duplicate in the raw data.
        """
        verses_dict = {}
        
        for verse_content in raw_verses:
            parts = verse_content.split('\t')
            
            if len(parts) >= 4:
                prefix = f"{parts[0]}\t{parts[1]}\t{parts[2]}"
                content = parts[3].strip()
                
                # Concatenate if the address already exists
                if prefix in verses_dict:
                    if content:
                        verses_dict[prefix] += f" {content}"
                else:
                    verses_dict[prefix] = content
            else:
                # Fallback for malformed strings
                if verse_content not in verses_dict:
                    verses_dict[verse_content] = ""
                    
        # Reconstruct the list of strings
        return [f"{prefix}\t{content}" for prefix, content in verses_dict.items()]
