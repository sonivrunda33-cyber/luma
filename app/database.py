import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

from flask import current_app, g


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(_error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db(app):
    schema_path = Path(__file__).with_name("schema.sql")
    with sqlite3.connect(app.config["DATABASE"]) as db:
        db.execute("PRAGMA foreign_keys = ON")
        db.executescript(schema_path.read_text(encoding="utf-8"))
        if db.execute("SELECT COUNT(*) FROM courses").fetchone()[0] == 0:
            db.executemany(
                "INSERT INTO courses(name, color, semester, syllabus_progress) VALUES(?,?,?,?)",
                [("Statistics", "coral", "Semester 3", 42),
                 ("Web technology", "blue", "Semester 3", 68),
                 ("Python", "mint", "Semester 3", 53),
                 ("Design thinking", "violet", "Semester 3", 35),
                 ("Artificial intelligence", "gold", "Semester 3", 24)],
            )
        if db.execute("SELECT COUNT(*) FROM tasks").fetchone()[0] == 0:
            now = datetime.now().replace(second=0, microsecond=0)
            tasks = [
                ("Review probability distributions", "Statistics", now.replace(hour=11, minute=30), 50, "high", "study", "Revise normal, binomial and Poisson distributions."),
                ("Build research questionnaire", "Design thinking", now.replace(hour=14, minute=0), 35, "medium", "assignment", "Include Likert, multiple choice and open questions."),
                ("Read chapter 6 · Neural networks", "Artificial intelligence", now.replace(hour=16, minute=15), 45, "medium", "reading", "Capture three questions for the study group."),
                ("Finish responsive navigation prototype", "Web technology", (now + timedelta(days=1)).replace(hour=18, minute=0), 60, "high", "assignment", "Check mobile and keyboard states."),
                ("Practice Python data handling", "Python", (now + timedelta(days=2)).replace(hour=12, minute=0), 40, "low", "study", "Work through the SQLite examples."),
                ("Plan study group agenda", "Personal", (now + timedelta(days=3)).replace(hour=10, minute=0), 25, "low", "personal", "Pick one topic each person can explain."),
            ]
            db.executemany("""INSERT INTO tasks(title,subject,due_at,duration_minutes,priority,kind,notes,created_at)
                VALUES(?,?,?,?,?,?,?,?)""", [(*t, now.isoformat(timespec="minutes")) for t in tasks])
        if db.execute("SELECT COUNT(*) FROM exams").fetchone()[0] == 0:
            now = datetime.now().replace(second=0, microsecond=0)
            exams = [
                ("Probability & Statistics", "Statistics", (now + timedelta(days=6)).replace(hour=9, minute=30), "Hall B · 204", "coral", "Bring a calculator and student ID."),
                ("Python Programming", "Python", (now + timedelta(days=12)).replace(hour=13, minute=0), "Lab 3", "blue", "Revise file handling and SQL."),
                ("Web Technology", "Web technology", (now + timedelta(days=19)).replace(hour=10, minute=0), "Block C · 101", "mint", "Review responsive layouts and DOM events."),
            ]
            db.executemany("""INSERT INTO exams(title,subject,exam_at,location,color,notes,created_at)
                VALUES(?,?,?,?,?,?,?)""", [(*e, now.isoformat(timespec="minutes")) for e in exams])
    app.teardown_appcontext(close_db)
