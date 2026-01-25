"""Main module."""

from dependency_injector.wiring import Provide, inject

import classes.services as services
import classes.containers as containers
import classes.Tester13 as Tester13
import classes.DataProcessor as DataProcessor

# in case changes are not picked-up, use this workaround
# import importlib
# importlib.reload(classes.Tester13)

@inject
def main(
        mtlxxService: services.MTLXXService = Provide[containers.Container.MTLXXServiceFactory]
        , tester13: Tester13.Tester13 = Provide[containers.Container.Tester13Factory]
        , tester13_2: Tester13.Tester13 = Provide[containers.Container.Tester13Factory]
        , kapka: Tester13.Kapka = Provide[containers.Container.KapkaFactory]
        , iDataProcessor: DataProcessor.IDataProcessor = Provide[containers.Container.IDataProcessorFactory]
) -> None:
    mtlxxService.do()
    tester13.do13()
    tester13_2.do13()
    print ("tester13 == tester13_2: " + str(tester13 == tester13_2)) # 
    kapka.kkk('aaa')
    iDataProcessor.process('interfaced haha')
    print (isinstance(iDataProcessor, DataProcessor.IDataProcessor)) # true
    print (isinstance(iDataProcessor, DataProcessor.DataProcessor)) # true
    
if __name__ == "__main__":
    container = containers.Container()
    container.init_resources()
    container.wire(modules=[__name__])

    # main(*sys.argv[1:])
    main()