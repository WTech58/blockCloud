from . import client,app
from .. import BlockSave
from flask import render_template,request.abort
from hashlib import sha256

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/dash")
def dash():
  return render_template("dash.html")

@app.route("/upload",methods=["GET","POST"])
def upload():
  if request.method == "GET":
    return redirect("/dash")
  elif request.method == "POST":
    blockID = request.form.get("blockID")
    data = request.form.get("data")
    prevHash = request.form.get("relaHash")
    if not prevHash:
      pass
    else:
      pass
  else:
    return abort(502)

app.run(host="0.0.0.0",port=5000)
