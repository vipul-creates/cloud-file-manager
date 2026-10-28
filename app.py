from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash # NEW

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Vipul123!@localhost/cloud_manager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # ... (leave your existing login code here) ...
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        return f"Login attempted with Email: {email}"
    return render_template("login.html")

# --- NEW REGISTER ROUTE ---
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # 1. Get data from the HTML form
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # 2. Check if the email already exists in the database
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "Error: Email already registered. <a href='/register'>Try again</a>"

        # 3. Hash the password (never store plain text!)
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # 4. Create the new user object
        new_user = User(name=name, email=email, password_hash=hashed_password)

        # 5. Save to MySQL
        db.session.add(new_user)
        db.session.commit()

        return "Registration successful! <a href='/login'>Go to Login</a>"

    # If it's a GET request, just show the form
    return render_template("register.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)