from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def hello():
  students = [
    {"name": "Sandrine", "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
    {"name": "Fritz", "score": 40},
    {"name": "sirius", "score": 75},
  ]
  return render_template("index.html", students=students)