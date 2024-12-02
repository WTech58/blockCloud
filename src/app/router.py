from . import client,app
from ..install import install_image,install_mach
from flask import render_template,request

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/dash")
def dash():
  return render_template("dash.html")



app.run(host="0.0.0.0",port=5000)
