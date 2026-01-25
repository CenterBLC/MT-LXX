"""Main module."""

from dependency_injector.wiring import Provide, inject

# import classes.services as services
# import classes.Tester13 as Tester13
# import classes.DataProcessor as DataProcessor

import classes.containers as containers
import classes.GNTWrapper as GNTWrapper

# in case changes are not picked-up, use this workaround
# import importlib
# importlib.reload(classes.Tester13)

@inject
def main(
        # mtlxxService: services.MTLXXService = Provide[containers.Container.MTLXXServiceFactory]
        # , tester13: Tester13.Tester13 = Provide[containers.Container.Tester13Factory]
        # , tester13_2: Tester13.Tester13 = Provide[containers.Container.Tester13Factory]
        # , kapka: Tester13.Kapka = Provide[containers.Container.KapkaFactory]
        # , iDataProcessor: DataProcessor.IDataProcessor = Provide[containers.Container.IDataProcessorFactory]

        gntWrapper: GNTWrapper.GNTWrapper = Provide[containers.Container.GNTWrapperFactory]
        , gntWrapper2: GNTWrapper.GNTWrapper = Provide[containers.Container.GNTWrapperFactory]
) -> None:
    
    print(gntWrapper.temp_ClassName)
    print("printing debug info...")
    print("gntWrapper == gntWrapper2: " + str(gntWrapper == gntWrapper2))

    print("TF App ready. Type 'help' for commands, 'quit' to exit.")

    while True:
        cmd = input("> ").strip()
        if cmd in {"quit", "exit"}:
            break
        if cmd == "help":
            print("Commands: stats | query <q> | quit")
            continue
        if cmd == "stats":
            # whatever you want
            print("OK")
            continue
        if cmd == "class_name":
            print(gntWrapper.temp_ClassName)
            continue
        if cmd.startswith("query "):
            q = cmd[len("query "):]
            # run TF operations using A
            # e.g., A.TF... / A.api... depending on your usage
            print(f"Running query: {q}")
            continue

        print("Unknown command. Type 'help'.")

    # mtlxxService.do()
    # tester13.do13()
    # tester13_2.do13()
    # print ("tester13 == tester13_2: " + str(tester13 == tester13_2)) # 
    # kapka.kkk('aaa')
    # iDataProcessor.process('interfaced haha')
    # print (isinstance(iDataProcessor, DataProcessor.IDataProcessor)) # true
    # print (isinstance(iDataProcessor, DataProcessor.DataProcessor)) # true
    
if __name__ == "__main__":
    container = containers.Container()
    container.init_resources()
    container.wire(modules=[__name__])

    # main(*sys.argv[1:])
    main()