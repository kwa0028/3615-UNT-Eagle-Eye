from flask import Blueprint, request
from flask import render_template
import psycopg2

views = Blueprint('views', __name__)


#Database connection
dbParameters = {
    "host": "localhost",
    "dbname": "eagleeye_db",
    "user": "postgres",
    "password": "eagleeye", #Store this
    "port": 5432
}

def get_db_connect():
    return psycopg2.connect(**dbParameters)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/JaneDoe')
def professor():
    name = request.args.get("name", "Jane Doe")

    conn = get_db_connect()
    cur = conn.cursor()
    cur.execute("SELECT course_title, rating, review_text, created_at FROM reviews WHERE professor_name = %s ORDER BY created_at DESC", (name,))
    reviews = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("professor.html", name=name, reviews=reviews)

@views.route('/creators')
def groupMembers():
    return render_template("creators.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/results')
def results():
    return render_template("results.html")

@views.route('/review', methods=["GET", "POST"])
def review():
    if request.method == "POST":
        professor_name = request.form.get("professor_name")
        course_title = request.form.get("course_title")
        rating = request.form.get("rating")
        review_text = request.form.get("review_text")

        conn = get_db_connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO reviews (professor_name, course_title, rating, review_text) VALUES (%s, %s, %s, %s)",
            (professor_name, course_title, rating, review_text)
        )
        conn.commit()
        cur.close()
        conn.close()

        return render_template("professor.html", name=professor_name, reviews=[(course_title, rating, review_text, "Just now")])

    return render_template("review.html")