import importlib
import sys
from pathlib import Path

all_python_files = [
    f for f in Path(__file__).parent.rglob("*.py") if f.is_file() and not f.name.endswith("__init__.py")
]
for m in all_python_files:
    spec = importlib.util.spec_from_file_location(str(m.with_suffix("")), m)
    foo = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = foo
    spec.loader.exec_module(foo)
