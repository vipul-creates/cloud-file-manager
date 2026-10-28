# Project DevLog

## Day 1: Environment Setup & First Flask App
**Date:** [Put today's date]
**Tasks Done:**
- Set up WSL Ubuntu, Python3, pip, venv, and Git.
- Installed MySQL and secured it with a root password.
- Created project folder and activated the virtual environment.
- Installed Flask and created the initial `app.py` and `index.html`.
- Set up VS Code to work inside WSL.

**Challenges Faced & Solved:**
- *Issue:* Got `TemplateNotFound` error.
- *Solution:* Realized Linux is case-sensitive. The folder was named `template` instead of `templates`. Renamed it with `mv template templates`.
- *Issue:* Flask wasn't found when running the app.
- *Solution:* The virtual environment wasn't active. Fixed by running `source venv/bin/activate`.

---

## Day 2: Version Control (Git & GitHub)
**Date:** [Put today's date]
**Tasks Done:**
- Initialized Git in the project folder.
- Created `.gitignore` to exclude `venv/` and `__pycache__/`.
- Created a GitHub repository and pushed the initial commit.
- Generated `requirements.txt` using `pip freeze > requirements.txt`.

**Challenges Faced & Solved:**
- (None today, setup was smooth).

---

## Day 3: Frontend - Login Page UI
**Date:** [Put today's date]
**Tasks Done:**
- Created `login.html` with CSS styling for a clean UI.
- Updated `index.html` to act as a placeholder dashboard.
- Updated `app.py` to handle GET and POST requests on the `/login` route.
- Used `request.form.get()` to capture user input.

**Challenges Faced & Solved:**
- [Add anything here if you face an error during today's steps]
