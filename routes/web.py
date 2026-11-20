from flask import Blueprint, render_template

web = Blueprint("web", __name__)


def page(template, page_name, title):
    return render_template(template, page=page_name, page_title=title)


@web.get("/")
def dashboard():
    return page("pages/dashboard.html", "dashboard", "Overview")


@web.get("/planner")
def planner():
    return page("pages/planner.html", "planner", "Study planner")


@web.get("/assignments")
def assignments():
    return page("pages/assignments.html", "assignments", "Assignments")


@web.get("/exams")
def exams():
    return page("pages/exams.html", "exams", "Exams & courses")


@web.get("/focus")
def focus():
    return page("pages/focus.html", "focus", "Focus room")


@web.get("/insights")
def insights():
    return page("pages/insights.html", "insights", "My progress")


@web.get("/research")
def research():
    return page("pages/research.html", "research", "Research lab")


@web.get("/settings")
def settings():
    return page("pages/settings.html", "settings", "Settings")
