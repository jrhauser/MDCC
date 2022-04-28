from flask import Flask, render_template, request
from cs50 import SQL
app = Flask(__name__)

db=SQL("sqlite:///MDCC.db")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/join")
def join():
    return render_template("join.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/memorial")
def memorial():
    return render_template("memorial.html")

@app.route("/links")
def links():
    return render_template("links.html")

@app.route("/discussion", methods=["GET", "POST"])
def discussion():
    if request.method == "GET":
        return render_template("discussion.html")
    