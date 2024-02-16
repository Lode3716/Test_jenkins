"""
   
 auth : l.devigne

"""
from flask import Flask, render_template

from UserDAO import UserDao

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/moche")
def users_moche():
    html = ""
    with UserDao("users_db.db") as dao:
        for user in dao.findAll():
            html += f"<li>{user.first_name} {user.last_name}</li>"
    return f"<ul>{html}</ul>"


@app.route("/users")
def users():
    with UserDao("users_db.db") as dao:
        users = list(dao.findAll())
    return render_template("users_list.html", users=users)
