'''
# Use in Jupyter Notebook:

from tftools import strip_cells
import nbformat

nb = nbformat.read("myfile.ipynb", as_version=4)
nb = strip_cells(nb, "first", 50)   # strip first 50 code cells
nb = strip_cells(nb, "last", 50)   # strip last 50 code cells
nb = strip_cells(nb, "range", (50, 70))   # strip from code cells 50 through 70


# Use from Command Line:

python -m tftools.nbstrip_cells myfile.ipynb first 100
python -m tftools.nbstrip_cells myfile.ipynb range 50 70

'''


import nbformat
import sys
from pathlib import Path

def strip_cells(nb, mode, value):
    """
    Strip outputs from cells based on mode:
    - mode="first", value=N: strip first N code cells
    - mode="last", value=N: strip last N code cells
    - mode="range", value=(start, end): strip code cells in that range (inclusive)
    """
    total_code = sum(1 for c in nb.cells if c.cell_type == "code")
    count = 0

    for i, cell in enumerate(nb.cells, start=1):
        if cell.cell_type != "code":
            continue

        strip = False
        if mode == "first" and count < value:
            strip = True
        elif mode == "last" and (total_code - count) < value:
            strip = True
        elif mode == "range" and value[0] <= count+1 <= value[1]:
            strip = True

        if strip:
            cell.outputs = []
            cell.execution_count = None

        count += 1

    return nb


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python -m tftools.nbstrip_cells notebook.ipynb first N")
        print("  python -m tftools.nbstrip_cells notebook.ipynb last N")
        print("  python -m tftools.nbstrip_cells notebook.ipynb range START END")
        sys.exit(1)

    in_file = Path(sys.argv[1])
    mode = sys.argv[2]
    args = sys.argv[3:]

    if mode == "first" and len(args) == 1:
        N = int(args[0])
        nb = nbformat.read(in_file, as_version=4)
        nb = strip_cells(nb, "first", N)
    elif mode == "last" and len(args) == 1:
        N = int(args[0])
        nb = nbformat.read(in_file, as_version=4)
        nb = strip_cells(nb, "last", N)
    elif mode == "range" and len(args) == 2:
        start, end = map(int, args)
        nb = nbformat.read(in_file, as_version=4)
        nb = strip_cells(nb, "range", (start, end))
    else:
        print("❌ Invalid arguments.")
        sys.exit(1)

    out_file = in_file.with_name(in_file.stem + "_clean.ipynb")
    nbformat.write(nb, out_file)
    print(f"✅ Saved cleaned notebook as {out_file}")


if __name__ == "__main__":
    main()
