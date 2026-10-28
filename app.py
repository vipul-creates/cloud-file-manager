from flask import Flask, render_template, request

app = Flask(__name__)

# 1. The Dashboard (Homepage)
@app.route("/")
def home():
    return render_template("index.html")

# 2. The Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # This part runs when you click the "Login" button
        # We will add database checking here in Day 4
        email = request.form.get("email")
        password = request.form.get("password")
        return f"Login attempted with Email: {email} and Password: {password}. Database check coming soon!"
    
    # This part runs when you just visit the page
    return render_template("login.html")

# 3. The Register Page (Placeholder for now)
@app.route("/register")
def register():
    return "<h1>Registration Page</h1><p>Coming in Day 5.</p>"

if __name__ == "__main__":
    app.run(debug=True)