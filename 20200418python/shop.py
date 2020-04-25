from flask import Flask, render_template
from flask import request, redirect
import sqlite3
conn = sqlite3.connect('shop.html')

import sqlite_test as mydb

app = Flask(__name__)


@app.route("/")
def hello():
    title = "WEBSITE"
    
    conn = sqlite3.connect("myshop.db")
    pds = mydb.getproducts(conn)

    total = 0
    for pd in pds:
        total += pd[2] + pd[3]
    return render_template("shop.html", title=title, products = pds, total = total)