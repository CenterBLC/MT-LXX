# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     from .Manager import Manager

# class FileB_Generator():
    
#     ......create abstract class with commonalities
#     def __init__(self, manager: "Manager") -> None:
#         self._gnt_wrapper: GNTWrapper = manager.gnt_wrapper

#     @property
#     def F(self) -> NodeFeatures:
#         return self._gnt_wrapper.F
    
#     @property
#     def L(self) -> Locality:
#         return self._gnt_wrapper.L
    
#     @property
#     def T(self) -> Text:
#         return self._gnt_wrapper.T

#     def generate(self) -> None:

#         .......... proceed with translating from the "GNT model creation.py"
#         books = GNT.api.F.otype.s('book')
