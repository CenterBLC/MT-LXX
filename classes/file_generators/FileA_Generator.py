from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from classes.Manager import Manager

from .FileGeneratorAbstract import FileGeneratorAbstract

from classes.FeatureMerger import FeatureMerger
from classes.enums.DataLevel import DataLevel
from classes.file_writers.FileA_Writer import FileA_Writer
from classes.file_writers.FileWriterAbstract import FileWriterAbstract

class FileA_Generator(FileGeneratorAbstract):

    def __init__(self, manager: "Manager") -> None:
        super().__init__(manager)
        self._feature_merger: FeatureMerger = manager.feature_merger
        self._file_writer: FileWriterAbstract = FileA_Writer(manager)
    
    def generate(self) -> None:
        
        i = 0
        raw_file_contents = []

        for verse in self.F.otype.s('verse'):
            text = "".join([self._feature_merger.get_word(word) + " " 
                            for word in self.L.d(verse,'word')])
            bo, ch, ve = self.T.sectionFromNode(verse)
            final = "\t".join([bo, str(ch), str(ve), text.strip()])

            if (self.data_level is DataLevel.NEW_TESTAMENT 
                    or 
                    (self.data_level is DataLevel.NT_BOOK
                        and bo == self._selected_book)
                ):

                raw_file_contents.append(final)
                if i < 3:
                    print(final)
                i += 1

        # Use the inherited method to merge duplicates
        merged_contents = self._merge_duplicate_verses(raw_file_contents)

        self._file_writer.WriteContents(merged_contents)
        print("internal report: file A generated.")