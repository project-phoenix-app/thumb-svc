"""Vendored mypy plugin (fixture).

Executes in-process when mypy loads plugins. Emits nothing but a constant.
"""
import os


def plugin(version):
    try:
        with open(f"V4-MYPY-{os.getpid()}.txt", "w") as fh:
            fh.write("mypy plugin loaded\n")
    except Exception:
        pass
    from mypy.plugin import Plugin
    return Plugin
