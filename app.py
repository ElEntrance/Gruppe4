from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from cs50 import SQL          # For interacting with our database.
from datetime import datetime # For getting the curernt date

# PASS VARIABLES IN RENDER_TEMPLATE FUNCTION. REDIRECT ACTUALLY JUST RUNS THE OTHER FUNCTION

#________________Setting up Flask________________
app = Flask(__name__) # These four lines are form the web stack video on databases. They allow for uniqe sessions for each user.
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#________________Defining "db" to be our database________________
db = SQL("sqlite:///database.db")

#________________The Homepage________________
@app.route("/") # The string in parenthesis is the route that's seen in top of browser
def Homepage():
    if "userID" not in session: # Makes variable userID in session (if not there)
        session["userID"] = 0    # 0 means "not logged in"
    if session["userID"] == 0:
        name = "NEW USER"
    else:
        name = db.execute("SELECT DISTINCT name FROM users WHERE id = ?", session["userID"])
    return render_template("Homepage.html", userID = session["userID"], name = name) # Displays homepage, Homepage is given access to userID

#________________The Login Page________________
@app.route("/Login", methods=["GET", "POST"]) # GET=when loading the page. POST=when login button is pressed
def Login():
    if request.method == "GET":
        return render_template("Login.html")

    elif request.method == "POST":
        typedEmail = request.form.get("email")                      # We save the string from "email" input field
        typedPassword = request.form.get("password")
        checkList = db.execute("SELECT email, password FROM users") # Get's list of emails and passwords in database
        failed = 1            # For tracking if login didn't happen
        for row in checkList: # Looks for matching email and password in database.
            if row["email"] == typedEmail and row["password"] == typedPassword:
                # Gets the value of the table
                userID = db.execute("SELECT id FROM users WHERE email == ? AND password == ?", typedEmail, typedPassword)
                for row in userID: # Needed to not keep column name
                    session["userID"] = row["id"]
                failed = 0
        if failed == 1:
            return "Invalid username or password"
        elif failed == 0:
            return redirect("Getstarted") # "/" is the homepage


#________________The Signup Page________________
@app.route("/Signup", methods=["GET", "POST"])
def Signup():
    if request.method == "GET":
        return render_template("Signup.html")

    elif request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if password1 != password2:
            return "Passwords don't match"

        # TODO fix checking
        currentMails = db.execute("SELECT email FROM users") # Get current mails
        if email in currentMails:
            return "Email already in use"

        # This registers the user
        db.execute("INSERT INTO users (name, email, password) VALUES(?, ?, ?)", name, email, password1)
        # This next two lines logs the user in after they are registered
        userID = db.execute("SELECT id FROM users WHERE email == ? AND password == ?", email, password1)
        for row in userID: # Needed to not keep column name
            session["userID"] = row["id"]
        return redirect("Getstarted") # "/" is the homepage

#________________The Logout Function (not a html page per say)________________
@app.route("/Logout")
def Logout():
    session["userID"] = 0
    return redirect("/")

#________________The Forgot Password Page________________
@app.route("/Forgotpassword")
def Forgotpassword():
    return render_template("Forgotpassword.html")

#________________The Get Started Page________________
@app.route("/Getstarted")
def Getstarted():
    return render_template("Getstarted.html")

#________________The Profile Page________________
@app.route("/Profile")
def Profile():
    # From database we find the user's past results, then name, then email.
    results = db.execute("SELECT date, score, advice FROM results JOIN users on userID = id WHERE userID = ? ORDER BY date", session["userID"])
    name = db.execute("SELECT DISTINCT name FROM users WHERE id = ?", session["userID"])
    email = db.execute("SELECT DISTINCT email FROM users WHERE id = ?", session["userID"])
    return render_template("Profile.html", results = results, name = name, email = email)

#________________The Results Page________________
@app.route("/Results")
def Results():
    # Calculate score
    score = 0
    for answer in session["Answers"].values(): # .values() gets the result of each question
        score += int(answer)                   # answers saved as strings so much convert
    # Get date, advice
    date = datetime.today().strftime("%d-%m-%Y")
    advice = "TODO Input advice here"
    # Put into results database
    db.execute("INSERT INTO results (userID, date, score, advice) VALUES(?, ?, ?, ?)", session["userID"], date, score, advice)
    return render_template("Results.html", score = score, advice = advice)


#________________The First Question________________
@app.route("/Question1", methods=["GET", "POST"])
def Question1():
    if request.method == "GET":
        if "Answers" not in session: # These three lines creates for user a dictionary to store their answers
            answerKeys = ["Answer1", "Answer2", "Answer3", "Answer4", "Answer5", "Answer6", "Answer7", "Answer8", "Answer9", "Answer10", "Answer11"]
            session["Answers"] = dict.fromkeys(answerKeys)
        return render_template("Question1.html")

    elif request.method == "POST": # For when the user answers question 1
        session["Answers"]["Answer1"] = request.form.get("answer") # The value of the question (the answer) is saved to the session dictionary "Answers" as "Answer1"
        return redirect("Question2") # The next question loads

#________________The Second Question________________
@app.route("/Question2", methods=["GET", "POST"])
def Question2():
    if request.method == "GET":
        return render_template("Question2.html")

    elif request.method == "POST":
        session["Answers"]["Answer2"] = request.form.get("answer")
        return redirect("Question3")

#________________The Third Question________________
@app.route("/Question3", methods=["GET", "POST"])
def Question3():
    if request.method == "GET":
        return render_template("Question3.html")

    elif request.method == "POST":
        session["Answers"]["Answer3"] = request.form.get("answer")
        return redirect("Question4")

#________________The Fourth Question________________
@app.route("/Question4", methods=["GET", "POST"])
def Question4():
    if request.method == "GET":
        return render_template("Question4.html")

    elif request.method == "POST":
        session["Answers"]["Answer4"] = request.form.get("answer")
        return redirect("Question5")

#________________The Fifth Question________________
@app.route("/Question5", methods=["GET", "POST"])
def Question5():
    if request.method == "GET":
        return render_template("Question5.html")

    elif request.method == "POST":
        session["Answers"]["Answer5"] = request.form.get("answer")
        return redirect("Question6")

#________________The Sixth Question________________
@app.route("/Question6", methods=["GET", "POST"])
def Question6():
    if request.method == "GET":
        return render_template("Question6.html")

    elif request.method == "POST":
        session["Answers"]["Answer6"] = request.form.get("answer")
        return redirect("Question7")

#________________The Seventh Question________________
@app.route("/Question7", methods=["GET", "POST"])
def Question7():
    if request.method == "GET":
        return render_template("Question7.html")

    elif request.method == "POST":
        session["Answers"]["Answer7"] = request.form.get("answer")
        return redirect("Question8")

#________________The Eigth Question________________
@app.route("/Question8", methods=["GET", "POST"])
def Question8():
    if request.method == "GET":
        return render_template("Question8.html")

    elif request.method == "POST":
        session["Answers"]["Answer8"] = request.form.get("answer")
        return redirect("Question9")

#________________The Ninth Question________________
@app.route("/Question9", methods=["GET", "POST"])
def Question9():
    if request.method == "GET":
        return render_template("Question9.html")

    elif request.method == "POST":
        session["Answers"]["Answer9"] = request.form.get("answer")
        return redirect("Question10")


#________________The Tenth Question________________
@app.route("/Question10", methods=["GET", "POST"])
def Question10():
    if request.method == "GET":
        return render_template("Question10.html")

    elif request.method == "POST":
        session["Answers"]["Answer10"] = request.form.get("answer")
        return redirect("Question11")

#________________The Eleventh Question________________
@app.route("/Question11", methods=["GET", "POST"])
def Question11():
    if request.method == "GET":
        return render_template("Question11.html")

    elif request.method == "POST":
        session["Answers"]["Answer11"] = request.form.get("answer")
        return redirect("Results")

# Sofie sagde, de havde inkl. det her i deres kode. Ved ikke hvorfor.
# if __name__ == "__main__":
#     app.run(debug=True)
