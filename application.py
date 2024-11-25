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

@app.route("/Forgotpassword")
def Forgotpassword():
    return render_template("Forgotpassword.html")

@app.route("/Getstarted")
def Getstarted():
    return render_template("Getstarted.html")

@app.route("/Profile")
def Profile():
    return render_template("Profile.html")
