# Project DevLog

## Day 1: Environment Setup & First Flask App
**Date:** [28-10-2026]
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
**Date:** [28-10-2026]
**Tasks Done:**
- Initialized Git in the project folder.
- Created `.gitignore` to exclude `venv/` and `__pycache__/`.
- Created a GitHub repository and pushed the initial commit.
- Generated `requirements.txt` using `pip freeze > requirements.txt`.

**Challenges Faced & Solved:**
- (None today, setup was smooth).

---

## Day 3: Frontend - Login Page UI
**Date:** [28-10-2026]
**Tasks Done:**
- Created `login.html` with CSS styling for a clean UI.
- Updated `index.html` to act as a placeholder dashboard.
- Updated `app.py` to handle GET and POST requests on the `/login` route.
- Used `request.form.get()` to capture user input.

**Challenges Faced & Solved:**
- [Add anything here if you face an error during today's steps]

## Day 4: Database Configuration & Security Hardening

**Focus:** MySQL 8.4 Setup, Authentication Migration, and Backend Connectivity.

### Tasks Completed
- [x] **Database Initialization:** Successfully logged into the MySQL 8.4 server and began configuring the root user for the Python backend application.
- [x] **Authentication Migration:** Encountered `ERROR 1524` (Plugin not loaded) due to MySQL 8.4 deprecating `mysql_native_password`. Migrated the user authentication method to the modern `caching_sha2_password` plugin.
- [x] **Password Policy Resolution:** Encountered `ERROR 1819` (Password policy requirement). Instead of lowering the database security policy, strengthened the root password to meet the default `validate_password` requirements.
- [x] **Connectivity Verification:** Successfully authenticated back into the MySQL server using the new credentials, ensuring the Python `venv` environment is ready to connect.

### Blockers Resolved
- Resolved MySQL 8.4 authentication plugin deprecation issues.
- Resolved strict password validation errors by adhering to the default security policies.

---

## Day 5: Module Verification & System Design Review

**Focus:** UI/Backend Integration, Screenshot Verification, and Design Component Finalization.

### Tasks Completed
- [x] **Module Verification (Catch-up Prep):** Captured working screenshots for the mentor catch-up. Verified that the Python frontend successfully communicates with the MySQL database (proving the backend is saving user/file metadata).
- [x] **System Design Check:** 
  - Finalized the **System Architecture** design (Client ↔ Python Backend ↔ MySQL ↔ Storage).
  - Confirmed **ER Diagram** and **Activity Diagrams** are prepared.
  - Reviewed the **Upload System Design Diagram** (mapping how files flow from the UI to the physical storage folder, while metadata goes to MySQL).
- [x] **SDLC Alignment:** Mapped current progress to the SDLC model. Confirmed that the project is currently in the **Implementation Phase** (approx. 60% complete).
- [x] **Tool Stack Selection:** Finalized the "Other" tools selection for the project form (Python, MySQL, VS Code, AWS) to accurately reflect the tech stack.

### Blockers / Pending
- [ ] **Pending:** Finalizing the flowchart for the *Storage Limits/Quota* module (M-07), as the low-level logic is not yet coded.

### Next Steps (Day 6)
- [ ] Complete the File Management module (M-05: Update/Delete).
- [ ] Begin implementing Storage Limits (M-07).
- [ ] Start writing the `Dockerfile` for AWS deployment.