from flask import Blueprint
from flask import render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("index.html")

@views.route('/JaneDoe')
def professor():
    return render_template("professor.html")

@views.route('/creators')
def groupMembers():
    return render_template("creators.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/results')
def results():
    return render_template("results.html")

@views.route('/review')
def review():
    return render_template("review.html")