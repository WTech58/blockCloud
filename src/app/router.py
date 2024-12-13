from blockchain import BlockSave
from flask import Flask,render_template,request,abort,session,redirect,jsonify
from hashlib import sha256
import os,datetime

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
    proof,id,blockhash = BlockSave(data)._upload(blockID)
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

@app.route("/get/chain/latest")
def get_latest_of_block():
  chain = BlockSave("test").get_all()
  for block in chain:
    block['time'] = datetime.datetime.strptime(block['rawData'].split('--')[-1], '%Y/%m/%d, %H:%M:%S')
  latest_block = max(chain, key=lambda x: x['time'])
  return jsonify(latest_block)
    
