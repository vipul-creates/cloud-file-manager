from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# --- DATABASE CONFIGURATION ---
# Format: mysql+pymysql://username:password@host/database_name
# Replace 'YOUR_MYSQL_PASSWORD' with the root password you set on Day 1.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Vipul123!@localhost/cloud_manager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database object
db = SQLAlchemy(app)

# --- DATABASE MODELS ---
# This class translates directly to a table in MySQL named 'user'
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

# --- ROUTES ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        return f"Login attempted with Email: {email}"
    return render_template("login.html")

@app.route("/register")
def register():
    return "<h1>Registration Page</h1><p>Coming soon.</p>"

# --- RUN ---
if __name__ == "__main__":
    # Create the database tables if they don't exist yet
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)