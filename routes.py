# routes.py
import os
from werkzeug.utils import secure_filename
from models import User, File 
from flask import render_template, request, redirect, url_for, flash, session, send_from_directory
from flask import render_template, request, redirect, url_for, flash, session
from models import User
from models import User, File, Folder
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
        query = request.args.get('q', '').strip()
        
        # Base query for this user's files
        files_query = File.query.filter_by(user_id=user.id)
        
        # If there's a search query, filter by filename
        if query:
            files_query = files_query.filter(File.filename.ilike(f'%{query}%'))
            
        user_files = files_query.all()
        user_folders = Folder.query.filter_by(user_id=user.id).all()
        
        return render_template("dashboard.html", user=user, files=user_files, folders=user_folders)
    

    @app.route("/logout")
    def logout():
        session.clear()
        flash("You have been logged out.", "success")
        return redirect(url_for("login"))
        
    @app.route("/upload", methods=["POST"])
    @login_required
    def upload():
        if "file" not in request.files:
            flash("No file part", "error")
            return redirect(url_for("dashboard"))
            
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file", "error")
            return redirect(url_for("dashboard"))

        folder_id = request.form.get("folder_id")
        # If folder_id is an empty string from the form, treat it as None (Root)
        folder_id = int(folder_id) if folder_id else None

        if file:
            filename = secure_filename(file.filename)
            upload_path = os.path.join("uploads", filename)
            file.save(upload_path)
            file_size = os.path.getsize(upload_path)
            
            new_file = File(
                user_id=current_user().id,
                folder_id=folder_id,
                filename=filename,
                file_size=file_size,
                mime_type=file.content_type
            )
            db.session.add(new_file)
            db.session.commit()
            
            flash(f"File '{filename}' uploaded successfully!", "success")
            return redirect(url_for("dashboard"))
    @app.route("/download/<int:file_id>")
    @login_required
    def download(file_id):
        # 1. Find the file in the database
        file_record = File.query.get_or_404(file_id)
        
        # 2. Security check: Ensure the file belongs to the logged-in user
        if file_record.user_id != current_user().id:
            flash("You do not have permission to download this file.", "error")
            return redirect(url_for("dashboard"))
        
        # 3. Send the file from the uploads folder
        return send_from_directory(
            os.path.abspath("uploads"), 
            file_record.filename, 
            as_attachment=True
        )

    @app.route("/delete/<int:file_id>", methods=["POST"])
    @login_required
    def delete(file_id):
        # 1. Find the file in the database
        file_record = File.query.get_or_404(file_id)
        
        # 2. Security check: Ensure the file belongs to the logged-in user
        if file_record.user_id != current_user().id:
            flash("You do not have permission to delete this file.", "error")
            return redirect(url_for("dashboard"))
        
        # 3. Delete from physical folder
        file_path = os.path.join("uploads", file_record.filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            
        # 4. Delete from database
        db.session.delete(file_record)
        db.session.commit()
        
        flash(f"File '{file_record.filename}' was deleted.", "success")
        return redirect(url_for("dashboard"))
    
    @app.route("/create_folder", methods=["POST"])
    @login_required
    def create_folder():
        folder_name = request.form.get("folder_name", "").strip()
        if folder_name:
            new_folder = Folder(user_id=current_user().id, name=folder_name)
            db.session.add(new_folder)
            db.session.commit()
            flash(f"Folder '{folder_name}' created!", "success")
        return redirect(url_for("dashboard"))