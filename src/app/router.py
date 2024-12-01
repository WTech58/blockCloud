from . import client,app
from ..install import install_image,install_mach
from flask import render_template,request

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/dash")
def dash():
  return render_template("dash.html")

@app.route("/shop")
def shop():
  return render_template("shop.html")

@app.route("/start")
def start_mach():
  target = request.args.get("target")
  if not taget or target == "" or target == None:
    return "找不到目標"
  else:
    image = install_image(target)
    vm = install_mach(image)
    return render_template("dash.html",image=image,vm=vm)
