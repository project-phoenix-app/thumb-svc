import os
import sqlite3

from flask import Flask, request

import confsvc

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
    # bind q as a parameter and escape LIKE metacharacters so it matches literally
    pattern = "%" + q.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_") + "%"
    con = sqlite3.connect("app.db")
    return {"rows": con.execute("SELECT id FROM items WHERE name LIKE ? ESCAPE '\\'", (pattern,)).fetchall()}
