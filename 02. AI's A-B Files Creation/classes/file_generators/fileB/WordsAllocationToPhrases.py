# from typing import TYPE_CHECKING
# from collections import defaultdict

# from classes.GNTWrapper import GNTWrapper
# from .WordsUnallocatedToPhrases_Key import WordsUnallocatedToPhrases_Key

# if TYPE_CHECKING:
#     from classes.Manager import Manager

# class WordsAllocationToPhrases():

#     def __init__(self, manager: "Manager") -> None:
#         self._manager: "Manager" = manager
#         self._gnt_wrapper: GNTWrapper = manager.gnt_wrapper
#         self._registry = defaultdict(bool)
    
#     def is_allocated(self
#             , book_name: str
#             , chapter_num: int
#             , verse_num: int
#             , word_id: int
#             ) -> bool:
        
#         key = WordsUnallocatedToPhrases_Key(
#             book_name
#             , chapter_num
#             , verse_num
#             , word_id
#         )
#         return self._registry[key] 

#     def set_allocated(self
#             , book_name: str
#             , chapter_num: int
#             , verse_num: int
#             , word_id: int
#             ) -> None:
        
#         key = WordsUnallocatedToPhrases_Key(
#             book_name
#             , chapter_num
#             , verse_num
#             , word_id
#         )
#         self._registry[key] = True
    
    