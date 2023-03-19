import importlib
import sys
from pathlib import Path

# Import all showcased scenes, in order for them to be registered in ShowcaseMeta

all_python_files = [
    f for f in Path(__file__).parent.rglob("*.py") if f.is_file() and not f.name.endswith("__init__.py")
]
for m in all_python_files:
    # TODO: fix this hack to get the module name
    module_name = ".".join(str(m.with_suffix("").relative_to(Path(__file__).parent.parent)).split("/"))

    spec = importlib.util.spec_from_file_location(module_name, m)
    foo = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = foo
    spec.loader.exec_module(foo)
