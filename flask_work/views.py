from flask import render_template, redirect, url_for, Blueprint, request
from favs import space, add_to_list

my_view = Blueprint('my_view', __name__)


@my_view.route("/")
def home():
    return render_template("home.html")

@my_view.route("/contact")
def contact():
    return render_template("contact.html")

@my_view.route('/alt',methods=["GET", "POST"])
def alt():
    if request.method == "POST":
        new = request.form["add_item"]
        add_to_list(new)
    return render_template('alt.html',space=space)

@my_view.route('/home')
def home_redirect():
    return redirect(url_for('my_view.home'))

@my_view.route('/homepage')
def homeb_redirect():
    return redirect(url_for('my_view.home'))