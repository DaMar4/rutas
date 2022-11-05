from flask import Blueprint, render_template
index = Blueprint("index",__name__)
@index.route("/")
@index.route("/home")
def home():
    return render_template("index.html")
@index.route("/about")
def about():
    return "<h1>Home</h1>"
