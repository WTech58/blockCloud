from . import client,app
from flask import render_template

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/dash")
def dash():
  return render_template("dash.html")

@app.route("/shop")
def shop():
  return render_template("shop.html")
