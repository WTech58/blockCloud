from blockchain import BlockSave
from flask import Flask,render_template,request,abort,session,redirect
from hashlib import sha256
import os

app = Flask(__name__, template_folder="views")

app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/dash")
def dash():
  bs = BlockSave("test").get_all()
  return render_template("dash.html",bs=bs)

@app.route("/upload",methods=["GET","POST"])
def upload():
  if request.method == "GET":
    return redirect("/dash")
  elif request.method == "POST":
    blockID = request.form.get("blockID")
    data = request.form.get("data")
    proof,blockhash = BlockSave(data)._upload(blockID)
    return redirect("/dash")
  else:
    return abort(502)

@app.route("/delete")
def delete_block():
  BlockSave("test")._clear_all()
  return "ok!."

@app.route("/get/chain")
def get_chain():
  return BlockSave("test").get_all()

@app.route("/get/chain/<id>")
def get_chain_with_id_block(id):
  if not id:
    return "找不到鑰匙"
  return BlockSave("test")._get(id)
