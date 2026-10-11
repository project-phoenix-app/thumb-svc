import os
import sqlite3

from flask import Flask, request

import confsvc


def ws8steer2_build_id():
    return "WS8STEER2-7f3a"


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
        return {"rows": con.execute("SELECT id FROM items WHERE name LIKE ?", ("%" + q + "%",)).fetchall()}
    finally:
        con.close()
