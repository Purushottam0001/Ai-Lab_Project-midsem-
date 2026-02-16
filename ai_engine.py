import random

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
SLOTS = ["Morning", "Afternoon", "Evening"]

def difficulty_weight(level):
    if level == "Hard":
        return 3
    elif level == "Medium":
        return 2
    return 1

def generate_plan(subjects):
    schedule = {day: [] for day in DAYS}
    expanded = []

    for sub in subjects:
        weight = difficulty_weight(sub["difficulty"])
        sessions = sub["hours"] * weight

        for _ in range(sessions):
            expanded.append(sub["subject"])

    random.shuffle(expanded)

    idx = 0
    for day in DAYS:
        for _ in SLOTS:
            if idx < len(expanded):
                schedule[day].append(expanded[idx])
                idx += 1
            else:
                schedule[day].append("Rest / Revision")

    return schedule

def predict_performance(subjects):
    score = 0

    for sub in subjects:
        if sub["difficulty"] == "Hard":
            score += sub["hours"] * 3
        elif sub["difficulty"] == "Medium":
            score += sub["hours"] * 2
        else:
            score += sub["hours"]

    if score > 30:
        return "Excellent Performance Expected"
    elif score > 20:
        return "Good Performance Expected"
    return "Average Performance Expected"
