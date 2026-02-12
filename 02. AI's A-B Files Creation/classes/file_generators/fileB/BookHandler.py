from typing import TYPE_CHECKING

from classes.GNTWrapper import GNTWrapper
from .VerseHandler import VerseHandler

if TYPE_CHECKING:
    from classes.Manager import Manager

class BookHandler():

    def __init__(self, manager: "Manager", book_id: str, book_name: str) -> None:
        self._manager: "Manager" = manager
        self._gnt_wrapper: GNTWrapper = manager.gnt_wrapper
        self._book_id: str = book_id
        self._book_name: str = book_name

    def get_transformed_content(self) -> list[str]:
        
        res: list[str] = list[str]()
        # res.append(self._book_name)
        verses_ofthe_Book: tuple = self._gnt_wrapper.L.d(self._book_id, 'verse')
        for verse_id in verses_ofthe_Book:
            verse_handler: VerseHandler = VerseHandler(self._manager, verse_id)
            verse_content: str = verse_handler.get_transformed_content()
            res.append(verse_content)
        
        return res
        