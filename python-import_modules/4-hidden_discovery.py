#!/usr/bin/python3
import marshal
import types

if __name__ == "__main__":
    # Read the .pyc file skipping the header (first 16 bytes for Python 3.7+)
    with open("hidden_4.pyc", "rb") as f:
        f.read(16)  # skip header
        code = marshal.load(f)

    # Create a module object from the code object
    module = types.ModuleType("hidden_4")
    exec(code, module.__dict__)

    # Get names defined in the module, filter out names starting with '__'
    names = [name for name in module.__dict__ if not name.startswith("__")]
    for name in sorted(names):
        print(name)

