"""Main module."""

# from dependency_injector.wiring import Provide, inject

# import classes.containers as containers
# import classes.GNTWrapper as GNTWrapper
# import classes.File_A_Generator as File_A_Generator

from classes.Manager import Manager

# @inject
def main(
        manager: Manager

        # container: containers.Container
        # gntWrapper: GNTWrapper.GNTWrapper = Provide[containers.Container.GNTWrapperFactory]
        # , file_A_Generator: File_A_Generator.File_A_Generator = Provide[containers.Container.File_A_Generator]
) -> None:
    
    settings = manager.settings
    gnt_wrapper = manager.gnt_wrapper
    fileA_generator = manager.fileA_generator
    fileB_generator = manager.fileB_generator


    print("MT-LXX  App ready. Type 'help' for commands, 'quit' to exit.")

    fileB_generator.generate()
    print("external report: file B generated.")

    while True:
        cmd = input(">> ").strip()
        if cmd.lower() == "gen a":
            fileA_generator.generate()
            print("external report: file A generated.")
            continue
        if cmd.lower() == "gen b":
            fileB_generator.generate()
            print("external report: file B generated.")
            continue
        if cmd.startswith("datalevel "):
            q = cmd[len("datalevel "):]
            settings.data_level = q.capitalize()
            print(f"DataLevel is set to {q}")
            continue
        if cmd == "gnt":
            value = getattr(gnt_wrapper, "temp_ClassName", None)
            print(f"gntWrapper.temp_ClassName is {value!r}")
            continue
        if cmd in {"quit", "exit"}:
            break
        if cmd == "help":
            print("Commands: gen A[B] | datalevel NT_BOOK[NEW_TESTAMENT] | quit")
            continue
        if cmd.startswith("query "):
            q = cmd[len("query "):]
            # run TF operations using A
            # e.g., A.TF... / A.api... depending on your usage
            print(f"Running query [not implemented yet]: {q}")
            continue

        print("Unknown command. Type 'help'.")

    
# if __name__ == "__main__":

manager = Manager()

# main(*sys.argv[1:])
main(manager)