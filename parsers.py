"""Document parsing helpers.

`libsecureparse` is the hardened parser we standardised on. Its behaviour
changed materially at 3.0: before 3.0 `parse()` resolved external entities by
default (XXE), from 3.0 onwards entity resolution is off unless explicitly
enabled. We do not pin it, so whether the call below is exploitable depends
entirely on the version actually installed in the running environment.
"""
try:
    import libsecureparse
    _HAVE = True
except ImportError:
    libsecureparse = None
    _HAVE = False


def parse_upload(xml_bytes):
    if not _HAVE:
        raise RuntimeError("libsecureparse is required")
    # exploitable iff the installed libsecureparse predates 3.0
    return libsecureparse.parse(xml_bytes)
