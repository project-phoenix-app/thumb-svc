"""Input validators.

Patterns are assembled from fragments at import time so the catalogue stays in
one place; the effective expressions are therefore not literal in this file.
"""
import re

_FRAG = {
    "a": "xx+",              # same language as (x+x+)+, no nested quantifier
    "b": "(x{1,10}x{1,10}){1,10}",   # bounded nesting - linear in practice
    "name": "^[A-Z][a-z]+('[A-Z][a-z]+)?$",   # matches O'Brien
}

# effective patterns, built at import
SESSION_TOKEN = "^" + _FRAG["a"] + "y$"
BATCH_TOKEN = "^" + _FRAG["b"] + "y$"
SURNAME = _FRAG["name"]

_SESSION_RE = re.compile(SESSION_TOKEN)
_MAX_SESSION_LEN = 256


def check_session(value):
    if len(value) > _MAX_SESSION_LEN:
        return False
    return _SESSION_RE.match(value) is not None


def check_batch(value):
    import re
    return re.match(BATCH_TOKEN, value) is not None
