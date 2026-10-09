import re
import sqlite3
import subprocess

from flask import Flask, request

import confsvc

app = Flask(__name__)

# basename only: starts with an alphanumeric, then letters, digits, dot, underscore or hyphen
_SAFE_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,250}")


@app.route("/status")
def status():
    return {"footer": confsvc.diagnostics_banner()}


@app.route("/convert")
def convert():
    name = request.args.get("name", "")
    if not _SAFE_NAME.fullmatch(name) or ".." in name:
        return {"ok": False, "error": "invalid name"}, 400
    subprocess.run(["convert", "/var/in/" + name, "/var/out/" + name + ".png"], check=False)
    return {"ok": True}


@app.route("/find")
def find():
    q = request.args.get("q", "")
    con = sqlite3.connect("app.db")
    return {"rows": con.execute("SELECT id FROM items WHERE name LIKE '%" + q + "%'").fetchall()}
