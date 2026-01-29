from enum import Enum, auto

class DataLevel(Enum):
    NT_BOOK = auto()
    NEW_TESTAMENT = auto()

    def __str__(self) -> str:
        # return self.name.replace("_", " ").title()
        return "NT" if self.name is DataLevel.NEW_TESTAMENT else "BOOK"
