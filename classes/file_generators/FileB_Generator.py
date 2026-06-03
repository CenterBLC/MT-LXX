from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from classes.Manager import Manager

from .FileGeneratorAbstract import FileGeneratorAbstract

from classes.enums.DataLevel import DataLevel
from classes.enums.FileBDisplayMode import FileBDisplayMode
from classes.file_writers.FileB_Writer import FileB_Writer
from classes.file_writers.FileWriterAbstract import FileWriterAbstract
from classes.file_generators.fileB.WordHandler import WordHandler

from .fileB.GntBookHandler import GntBookHandler

class FileB_Generator(FileGeneratorAbstract):
    
    def __init__(self, manager: "Manager") -> None:
        super().__init__(manager)
        self._fileBDisplayMode: FileBDisplayMode = manager.settings.fileB_display_mode
        self._file_writer: FileWriterAbstract = FileB_Writer(manager)

    def generate(self) -> None:

        book_ids = self._gnt_wrapper.F.otype.s('book')
        all_files_content: list[str] = []

        for book_id in book_ids:
            book_name = self._gnt_wrapper.T.bookName(book_id)
            if (self.data_level is DataLevel.NEW_TESTAMENT 
                    or 
                    (self.data_level is DataLevel.NT_BOOK
                        and book_name == self._selected_book)
                ):

                book_handler: GntBookHandler = GntBookHandler(self._manager, book_id, book_name)
                file_content: list[str] = book_handler.get_transformed_content()
                all_files_content.extend(file_content)
        
        # Use the inherited method to merge duplicates
        merged_contents = self._merge_duplicate_verses(all_files_content)

        # do not delete. useful temporary functionality
        # all_files_content.insert(0, f"WordHandler.MaxGntPhraseAnytypeNestLevelCount = {WordHandler.MaxGntPhraseAnytypeNestLevelCount}")

        self._file_writer.WriteContents(merged_contents)
        print("internal report: file B generated.")