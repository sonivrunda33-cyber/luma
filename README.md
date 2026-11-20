# Luma Study

A polished student study-planner prototype built with Flask, SQLite, HTML, CSS and vanilla JavaScript. The interface includes the dashboard, weekly planner, assignments, exam tracking, focus timer, progress view and a small research-data collection area for the college project.

## Open and run in PyCharm

1. Open this folder as a project in PyCharm.
2. Create a Python virtual environment from **Settings → Project → Python Interpreter**.
3. Open the PyCharm terminal and install the main dependency:

   ```bash
   pip install -r requirements.txt
   ```

4. Open `run.py` and click **Run**. The development server opens at `http://127.0.0.1:5000`.
5. The SQLite database is created automatically at `instance/luma_study.sqlite3`. The first run adds example tasks, courses and exams so the screens have content. It does not create fake survey or usability results.

For the paired t-test/Wilcoxon calculations in Research Lab, install the optional analysis tools:

```bash
pip install -r requirements-analysis.txt
```

Without SciPy, the Research Lab still saves and exports responses and shows descriptive paired times; it does not invent a p-value.

## Project map

```text
run.py                      Development entry point
app/__init__.py             Flask application factory and blueprint setup
app/database.py             SQLite connection and first-run sample content
app/schema.sql              Database tables and indexes
app/routes/web.py           Page routes
app/routes/api.py           CRUD, measurement, research and CSV API routes
app/templates/base.html     Shared glass-style shell, navigation and task dialog
app/templates/pages/        Individual website pages
app/static/css/             Design tokens, layout, components, motion and page styles
app/static/js/core/         API helper, icons, UI helpers and shared renderers
app/static/js/pages/        Page-specific interactions
instance/                   Automatically created SQLite data folder
```

## Included features

- Create, edit, complete and delete study tasks.
- Weekly calendar view, course progress, exam countdowns and subject filters.
- Focus timer with recorded sessions and recent-session history.
- Dashboard and charts based on real saved planner activity.
- Basic interaction-event logging for task creation/completion, exams and focus sessions.
- Mixed-format baseline survey, post-task SUS scoring, paired usability-test entry and CSV exports.
- Paired comparison chooses a t-test only when the sample is large enough for a normality check and the paired differences pass it; otherwise it uses the Wilcoxon signed-rank test when SciPy is installed.

## Research integrity notes

Use actual participants and participant codes such as `P01`; do not enter names or contact details. A paired test should use the same participant and the same task with both methods. Record how the task was explained and note any order effects. Treat initial planner tasks as interface examples, not research evidence. Report the number of participants, test used, effect size, confidence interval, limitations and usability issues in the final college report.

## Before sharing or deploying

This is a local classroom prototype, not an account-secured production service. Change the development secret key, add proper authentication and CSRF protections if you expose it to other people, and avoid collecting personal identifiers in research forms.
