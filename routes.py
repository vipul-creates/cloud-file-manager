# routes.py
from flask import render_template, request, redirect, url_for, flash, session
from models import User
from extensions import db
from auth_helpers import current_user, login_required

def register_routes(app):

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/db-test")
    def db_test():
        try:
            count = User.query.count()
            return f"Database connected. Users in table: {count}"
        except Exception as e:
            return f"DB error: {e}", 500

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            name     = request.form.get("name", "").strip()
            email    = request.form.get("email", "").strip().lower()
            password = request.form.get("password", "")

            if not name or not email or not password:
                flash("All fields are required.", "error")
                return redirect(url_for("register"))
            if len(password) < 6:
                flash("Password must be at least 6 characters.", "error")
                return redirect(url_for("register"))
            if User.query.filter_by(email=email).first():
                flash("An account with that email already exists.", "error")
                return redirect(url_for("register"))

            user = User(name=name, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            flash("Account created. Please log in.", "success")
            return redirect(url_for("login"))

        return render_template("register.html")

    # --- DAY 7 ADDITIONS BELOW ---

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email    = request.form.get("email", "").strip().lower()
            password = request.form.get("password", "")

            # 1. Find user by email
            user = User.query.filter_by(email=email).first()

            # 2. Check user exists AND password matches
            if not user or not user.check_password(password):
                flash("Invalid email or password.", "error")
                return redirect(url_for("login"))

            # 3. Log them in — store ONLY the id in the session
            session["user_id"] = user.id
            flash(f"Welcome back, {user.name}!", "success")
            return redirect(url_for("dashboard"))

        return render_template("login.html")

    @app.route("/dashboard")
    @login_required
    def dashboard():
        user = current_user()
        return render_template("dashboard.html", user=user)

    @app.route("/logout")
    def logout():
        session.clear()
        flash("You have been logged out.", "success")
        return redirect(url_for("login"))