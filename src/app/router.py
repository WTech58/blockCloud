from blockchain import BlockSave
from flask import Flask,render_template,request,abort,session,redirect,jsonify
from hashlib import sha256
from flask_discord import DiscordOAuth2Session, requires_authorization, Unauthorized
import os,datetime

app = Flask(__name__, template_folder="views")

app.config['SECRET_KEY'] = os.urandom(24)
app.config["DISCORD_CLIENT_ID"] = "1308052771626422304"    # Discord client ID.
app.config["DISCORD_CLIENT_SECRET"] = "CklemdSKyKH2LnEPzPsM8qn2ZQRArBXu"                # Discord client secret.
app.config["DISCORD_REDIRECT_URI"] = "https://bc.wtechhk.xyz/auth/discord"                 # URL to your callback endpoint.
app.config["DISCORD_BOT_TOKEN"] = os.environ.get("dcToken")

discord = DiscordOAuth2Session(app)

users = []

@app.route("/")
def index():
  if not session.get('user'):
    session['user'] = ""
  if not session.get("dc"):
    session["dc"] = "0"
  return render_template("index.html")

@app.route("/logout")
def auth_logout():
  session["user"] = None
  if session["dc"] == "1":
    discord.revoke()
    session["dc"] = "0"
  return redirect("/auth/login")

@app.route("/auth/login",methods=["GET","POST"])
def auth_login():
  if request.method == "GET":
    return render_template("login.html")
  else:
    code = str(request.form.get("auth_code"))
    if users == []:
      return "不要玩了，都沒有東西的"
    for user in users:
      ncode = f"bc-{user['username']}"
      scode = sha256(ncode.encode('utf-8')).hexdigest()
      if code == scode:
        session["user"] = str(user["username"])
        return redirect("/dash")
    return redirect("/auth/login")

@app.route("/auth/dc")
def login_with_dc():
  return discord.create_session(scope=["identify"])

@app.route("/auth/discord")
@requires_authorization
def login_discord_session():
  if not discord.authorized:
    return jsonify({"dc-status":False,"msg":"請登入discord"})
  user = discord.fetch_user()
  session["user"] = user.name
  session["dc"] = "1"
  return redirect("/dash")

@app.route("/dash")
def dash():
  u = session["user"]
  if not u:
    session["user"] = ""
  if u is None or u == "":
    return redirect("/")
  bs = BlockSave("test").get_all()
  return render_template("dash.html",bs=bs,u=u)

@app.route("/store")
def go_store():
  return render_template("store.html")

@app.route("/create/auth/code")
def create_auth_code():
  user = str(request.args.get("user"))
  token = str(request.args.get("apikey"))
  if not user:
    return "找不到東西"
  if not token:
    return "你不能建立"
  bs = BlockSave("test").get_all()
  for block in bs:
    if str(block["blockID"]).startswith("119"):
      rawData = str(block["rawData"]).split("--")[1]
      if token == rawData:
        users.append({"username":user})
        return {"apiKey":sha256(f"bc-{user}".encode("utf-8")).hexdigest()}
  return "不行"

@app.route("/upload",methods=["GET","POST"])
def upload():
  if request.method == "GET":
    return redirect("/dash")
  elif request.method == "POST":
    blockID = request.form.get("blockID")
    data = request.form.get("data")
    proof,id,blockhash = BlockSave(data)._upload(blockID)
    return {"status":True}
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
    
@app.route("/get/chain/hash")
def get_block_for_hash():
  code = request.args.get("code")
  if not code:
    return jsonify(error=True)
  statement = BlockSave.get_with_hash(code)
  if statement is None:
    return jsonify(error=True,notfound=True,youwilldied=True)
  return statement
