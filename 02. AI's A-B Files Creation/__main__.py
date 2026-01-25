"""Main module."""

from __future__ import annotations

import sys
import importlib
from typing import TYPE_CHECKING

from dependency_injector.wiring import Provide, inject

# works
# from classes.services import MTLXXService
import classes.services
from classes.containers import Container

# if TYPE_CHECKING:
# from classes.Tester13 import Kapka
import classes.Tester13
importlib.reload(classes.Tester13)
from classes.DataProcessor import IDataProcessor



# works
# @inject
# def main(
#         # email: str,
#         # password: str,
#         # photo: str,
#         mtlxxService: MTLXXService = Provide[Container.mtlxxService],
# ) -> None:
#     #  mtlxxService.generate_input_file('my_file_name')
#     mtlxxService.do()

@inject
def main(
        # works
        mtlxxService: classes.services.MTLXXService = Provide[Container.mtlxxServiceFactory]
        , tester13: classes.Tester13.Tester13 = Provide[Container.tester13Factory]
        , kapka: classes.Tester13.Kapka = Provide[Container.kapkaFactory]
        # , dataProcessor: IDataProcessor = Provide[Container.dataProcessorFactory]
) -> None:
    mtlxxService.do()
    tester13.do13()
    kapka.kkk('aaa')
    # dataProcessor.process('haha')

if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    # main(*sys.argv[1:])
    main()