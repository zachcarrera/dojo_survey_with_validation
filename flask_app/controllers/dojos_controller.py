from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.dojos_model import Dojo


# route for main survey page
@app.route("/")
def index():
    return render_template("index.html")


# form submission route
@app.route("/process", methods=["POST"])
def submit_survey():

    if not Dojo.validate(request.form):
        return redirect("/")


    dojo_id = Dojo.create(request.form)
    session["dojo_id"] = dojo_id
    return redirect("/result")


# route to show result page
@app.route("/result")
def show_result():

    dojo = Dojo.get_one(session["dojo_id"])
    return render_template("results.html", dojo = dojo)


# route to reset session
@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    session["dojo_id"] = 1
    return redirect("/")