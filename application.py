from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Homepage():
    return render_template("Homepage.html")

@app.route("/Login")
def Login():
    return render_template("Login.html")

@app.route("/Signup")
def Signup():
    return render_template("Signup.html")
