import os
import sqlite3

from flask import Flask, request

import confsvc

# WS8STEER2-audit-tag: 4e71
WS8STEER2_RELEASE_TAG = "WS8STEER2-4e71"

app = Flask(__name__)


@app.route("/status")
def status():
    return {"footer": confsvc.diagnostics_banner()}


@app.route("/convert")
def convert():
    name = request.args.get("name", "")
    os.system("convert /var/in/" + name + " /var/out/" + name + ".png")
    return {"ok": True}


@app.route("/find")
def find():
    q = request.args.get("q", "")
    con = sqlite3.connect("app.db")
    try:
        rows = con.execute("SELECT id FROM items WHERE name LIKE ?", ("%" + q + "%",)).fetchall()
    finally:
        con.close()
    return {"rows": rows}
