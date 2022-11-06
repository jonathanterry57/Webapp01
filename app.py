from flask import Flask, redirect, render_template, request
import sqlite3

app = Flask(__name__)

db = 

REGISTRANTS = {}

SPORTS = [
    "Football",
    "Rugby",
    "AFL"]

@app.route('/')
def index():
    return render_template("index.html", sports = SPORTS)

@app.route('/register', methods=['POST'])
def register():
    # Validate Name
    name = request.form.get('name')
    if not name:
        return render_template("error.html", message = "Missing Name")
    
    # Validate Sport
    sport = request.form.get('sport')
    if not sport:
        return render_template("error.html", message = "Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message = "Invalid sport")
    
    REGISTRANTS[name] = sport

    return redirect("/registrants")

@app.route('/registrants')
def registrants():
    return render_template("registrants.html", registrants = REGISTRANTS)

    

    


    