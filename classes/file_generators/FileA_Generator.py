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
        
        i=0
        file_contents=[]
        # outputfile_suffix = '_normalized'

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

                file_contents.append(final)
                if i<3:
                    print(final)
                i=i+1

        self._file_writer.WriteContents(file_contents)

        # with open('./data_gnt/input_' + selected_book + outputfile_suffix, 'w', encoding='utf-8') as file_contents:
        #     for line in file_contents:
        #         file_contents.write(line + '\n')

        print("internal report: file A generated.")

