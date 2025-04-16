from flask import render_template #import from flask
from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS
import psycopg2
import bcrypt
import jwt
import os
import datetime

auth = Blueprint('auth', __name__)
SECRET_KEY = "h4?+Do^^XZVsxr^uT*g;6=8C*asvFj(/6Va;i=gZeI$Lvo!&fm;{f'^Zc:ZiuK|" #for JWT tokens
CORS(auth)

#Database connection
dbParameters = {
    "host": "localhost",
    "dbname": "postgres",
    "user": "postgres",
    "password": "eagleeye", #Store this
    "port": 5432
}

def get_db_connect():
    return psycopg2.connect(**dbParameters)


@auth.route('/login', methods=["GET"])
def login():
    return render_template("login.html") # goes to the login.html file

@auth.route('/logout', methods=["GET"])
def logout():
    return "<p>Logout</p>"

@auth.route('/SignUp', methods=["GET"])
def signUp():
    return render_template("signup.html") # goes to the signup.html file

#API login route
@auth.route('/api/SignUp', methods=["POST"])
def apiSignUp():
    data = request.json
    password = data.get("password")
    username = data.get("username")

    if not username or not password:
        return jsonify({"error": "Your username and password are required"}), 400
    
    hashedPassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    conn = get_db_connect()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO students (username, passwords) VALUES (%s, %s)", (username, hashedPassword))
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        return jsonify({"error": "Database error", "details": str(e)})
    finally:
        cur.close()
        conn.close()
    
    return jsonify({"message": "User registered successfully!"})

#API login route
@auth.route('/api/login', methods=["POST"])
def apiLogin():
    data = request.json
    password = data.get("password")
    username = data.get("username")

    if not username or not password:
        return jsonify({"error": "Your username and password are required"}), 400
    
    hashedPassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    conn = get_db_connect()
    cur = conn.cursor()
    
    cur.execute("SELECT password FROM students WHERE username = %s", (username,))
    user = cur.fetchone()

    cur.close()
    conn.close()

    if user and bcrypt.checkpw(password.encode('utf-8'), user[0].encode('utf-8')):
        token = jwt.encode({"username": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token})
    else:
        return jsonify({"error": "Wrong credentials"}), 401