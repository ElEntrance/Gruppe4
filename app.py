from flask import Flask, render_template, request, session, redirect

#________________Setting up Flask________________
app = Flask(__name__) # These four lines are form the web stack video on databases. They allow for uniqe sessions for each user.
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

#________________The Homepage________________
@app.route("/")
def Homepage():
    return render_template("Homepage.html")

#________________The Login Page________________
@app.route("/Login")
def Login():
    return render_template("Login.html")

#________________The Signup Page________________
@app.route("/Signup")
def Signup():
    return render_template("Signup.html")

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
    return render_template("Profile.html")

#________________The Results Page________________
@app.route("/Results")
def Results():
    return render_template("Results.html")

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