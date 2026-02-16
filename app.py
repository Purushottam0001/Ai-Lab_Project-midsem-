from flask import Flask, render_template, request
from ai_engine import generate_plan, predict_performance

app = Flask(__name__)


# ---------------- HOME PAGE ----------------
@app.route("/")
def index():
    return render_template("index.html")


# ---------------- PLANNER PAGE ----------------
@app.route("/planner")
def planner():
    return render_template("planner.html")


# ---------------- HOW IT WORKS PAGE ----------------
@app.route("/how")
def how():
    return render_template("how.html")


# ---------------- GENERATE AI PLAN ----------------
@app.route("/generate", methods=["POST"])
def generate():

    # -------- SUBJECT DATA --------
    subjects = request.form.getlist("subject")
    hours = request.form.getlist("hours")
    difficulty = request.form.getlist("difficulty")

    data = []

    for i in range(len(subjects)):
        data.append({
            "subject": subjects[i],
            "hours": int(hours[i]),
            "difficulty": difficulty[i]
        })

    # -------- AVAILABLE TIME SLOTS --------
    available_slots = {
        "Monday": request.form.getlist("monday"),
        "Tuesday": request.form.getlist("tuesday"),
        "Wednesday": request.form.getlist("wednesday"),
        "Thursday": request.form.getlist("thursday"),
        "Friday": request.form.getlist("friday"),
        "Saturday": request.form.getlist("saturday"),
    }

    # -------- AI SCHEDULING --------
    timetable = generate_plan(data, available_slots)

    # -------- PERFORMANCE PREDICTION --------
    performance = predict_performance(data)

    # -------- SEND TO RESULT PAGE --------
    return render_template(
        "result.html",
        timetable=timetable,
        performance=performance
    )


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)
