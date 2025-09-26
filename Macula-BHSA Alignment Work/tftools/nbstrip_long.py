'''
# Use in Jupyter Notebook:

from tftools import strip_long
import nbformat

nb = nbformat.read("MT-LXX_Workbench.ipynb", as_version=4)
nb = strip_long(nb, 20000)          # strip outputs > 20k chars

# Use from Command Line:

python -m tftools.nbstrip_long myfile.ipynb 15000          # stips outputs > 15k chars

'''



import nbformat
import sys
from pathlib import Path

def is_large_output(cell, max_chars=10000):
    """
    Detect if a cell has large output (> max_chars).
    Looks at text and data size.
    """
    total_size = 0
    for out in cell.get("outputs", []):
        if "text" in out:
            total_size += sum(len(t) for t in out["text"])
        if "data" in out:
            for mime, val in out["data"].items():
                if isinstance(val, str):
                    total_size += len(val)
                elif isinstance(val, list):
                    total_size += sum(len(v) for v in val if isinstance(v, str))
    return total_size > max_chars


def strip_long(nb, max_chars=10000):
    """
    Strip outputs from cells with very large outputs.
    """
    for cell in nb.cells:
        if cell.cell_type == "code" and is_large_output(cell, max_chars):
            cell.outputs = []
            cell.execution_count = None
    return nb


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m tftools.nbstrip_long notebook.ipynb [max_chars]")
        sys.exit(1)

    in_file = Path(sys.argv[1])
    max_chars = int(sys.argv[2]) if len(sys.argv) > 2 else 10000

    nb = nbformat.read(in_file, as_version=4)
    nb = strip_long(nb, max_chars)

    out_file = in_file.with_name(in_file.stem + "_clean.ipynb")
    nbformat.write(nb, out_file)

    print(f"✅ Stripped outputs > {max_chars} chars.")
    print(f"📄 Saved as {out_file}")


if __name__ == "__main__":
    main()
