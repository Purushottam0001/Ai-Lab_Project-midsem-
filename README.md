# 📚 StudyWiz – AI Study Planner & Performance Predictor(BASIC AI_LAB PROJECT)

StudyWiz is a goal-based AI-powered study planner that generates intelligent weekly timetables based on subject difficulty, required hours, and user availability. It also predicts expected performance using weighted scoring logic.

---

## 🚀 Features

- Weekly AI-generated timetable (Monday–Sunday)
- Exact time-slot based scheduling
- ## Goal-based intelligent allocation
- ## Heuristic priority weighting (Easy / Medium / Hard)
- Performance prediction engine
- Modern clean UI (Flask + HTML + CSS)

---

## 🧠 How It Works

StudyWiz works as a Goal-Based Agent:

1. User enters subjects, hours, and difficulty.
2. User selects available time slots.
3. AI assigns subjects to available slots based on:
   - Difficulty weight
   - Required study hours
   - User constraints
4. Performance is predicted using weighted scoring.

---

## 🛠️ Tech Stack

- Python (Flask)
- HTML5
- CSS3
- Jinja2 Templates

---

## 📂 Project Structure

AI-Timetable-Generator/
│
├── app.py  
├── ai_engine.py  
├── templates/  
│   ├── index.html  
│   ├── planner.html  
│   ├── result.html  
│   └── how.html  
│
├── static/  
│   └── style.css  
│
└── README.md  

---

## ▶️ How To Run

1. Install Flask

pip install flask

2. Run the application

python app.py

3. Open in browser

http://127.0.0.1:5000

---

## 🎓 AI Concepts Used

- Goal-Based Agent
- Heuristic Scheduling
- Constraint-Based Allocation
- Weighted Scoring Model
