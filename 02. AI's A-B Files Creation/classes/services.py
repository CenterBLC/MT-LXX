"""Services module."""

import logging
from typing import Dict

class BaseService:

    def __init__(self) -> None:
        pass
        # self.logger = logging.getLogger(
        #     f"{__name__}.{self.__class__.__name__}",
        # )

# temporary
class MTLXXService(BaseService):

    def __init__(self) -> None:
        super().__init__()

    def generate_input_file(self, file_name: str) -> None: #, user: Dict[str, str], photo_path: str) -> None:
        pass
        # generate input file

        # self.logger.debug(
        #     "File %s has been successfully generated", # "Photo %s has been successfully uploaded by user %s",
        #     file_name
        # )

    def do(self) -> None:
        print('abcde')
        