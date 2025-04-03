from flask import Blueprint
from flask import render_template

views = Blueprint('auth', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/about')
def home():
    return render_template("about.html")