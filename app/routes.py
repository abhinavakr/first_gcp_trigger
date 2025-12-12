from flask import Blueprint, render_template, request, redirect, url_for, session, flash

bp = Blueprint('main', __name__)

# Simple in-memory user for demo (username: admin, password: secret)
FAKE_USER = {"username": "admin", "password": "secret"}


@bp.route("/")
def index():
    if session.get("logged_in"):
        return f"<h1>Welcome, {session['username']}!</h1><a href='/logout'>Logout</a>"
    return redirect(url_for("main.login"))


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if (username == FAKE_USER["username"] and
                password == FAKE_USER["password"]):
            session["logged_in"] = True
            session["username"] = username
            return redirect(url_for("main.index"))
        else:
            flash("Invalid credentials", "error")
    return render_template("login.html")


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.login"))