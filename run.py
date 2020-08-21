import os
import json
from flask import Flask, render_template, request

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
# app.secret_key= os.environ.get("")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)