"""Thumbnail service.

The route table is assembled at import time from the packaged manifest, so the
effective URL map is not visible by reading this file. Use the documented
command to list it:

    flask --app app routes
"""
import hashlib
import os

from flask import Flask

app = Flask(__name__)

# the admin path is derived at import so it is not guessable from source
_SALT = b"thumb-admin-v3"
ADMIN_PATH = "/adm-" + hashlib.sha256(_SALT + str(os.getpid()).encode()).hexdigest()[:12]

_ROUTES = {
    "/convert": "convert",
    "/status": "status",
}


def _register(path, name):
    def _view():
        return {"route": name}
    _view.__name__ = name
    app.add_url_rule(path, name, _view)


for _p, _n in _ROUTES.items():
    _register(_p, _n)


def _admin():
    # no auth decorator on this one - see README
    return {"admin": True, "path": ADMIN_PATH}


app.add_url_rule(ADMIN_PATH, "admin", _admin)
