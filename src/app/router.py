from ..app import app
from .. import BlockSave
from flask import render_template,request,abort,session
from hashlib import sha256
import os

app.config['SECRET_KEY'] = os.urandom(24)
session["blocksave"] = []

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/dash")
def dash():
  bs = session["blocksave"]
  return render_template("dash.html",bs=bs)

@app.route("/upload",methods=["GET","POST"])
def upload():
  if request.method == "GET":
    return redirect("/dash")
  elif request.method == "POST":
    blockID = request.form.get("blockID")
    data = request.form.get("data")
    if not prevHash:
      proof,blockhash = BlockSave(data)._upload(blockID)
      session["blocksave"].append({"blockID":blockID,"proof":proof,"rawData":data,"blockhash":blockhash})
      return redirect("/dash")
    else:
      return redirect("/dash")
  else:
    return abort(502)

@app.route("/delete")
def delete_block():
  session["blocksave"].clear()
  return "ok!."

app.run(host="0.0.0.0",port=5000)
