from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from classes.Manager import Manager

class BookHandler():

    def __init__(self, manager: "Manager", book_id: str, book_name: str) -> None:
        self._book_id = book_id
        self._book_name = book_name

    def get_transformed_content(self) -> list[str]:
        # this is the dummy line to be changed (stopped here)
        # another error: now the files are not being generated. the whole folder is empty.
        return [self._book_name]
        