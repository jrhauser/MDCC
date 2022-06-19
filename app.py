from flask import Flask, render_template, request, g, session, redirect
from flask_session import Session
from cs50 import SQL
from functools import wraps;
from werkzeug.security import check_password_hash, generate_password_hash
import os

#FROM FINANCE ----------------------------------------------------------------
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"]

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# https://cs50.readthedocs.io/heroku/
uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgres://")
db = SQL(uri)

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
#---------------------------------------------------------------------------------

@app.route("/", methods=["GET"])
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

@app.route("/announcements")
def announcement():
    return render_template("announcements.html")

@app.route("/newAnnouncement", methods=["GET", "POST"])
@login_required
def admin():
        return render_template("newAnnouncement.html")

@app.route("/delete", methods=['POST'])
@login_required
def delete():
    return redirect("/announcements")
