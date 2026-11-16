# auth_helpers.py
from functools import wraps
from flask import session, redirect, url_for, flash
from models import User

def current_user():
    """Return the logged-in User object, or None if not logged in."""
    uid = session.get("user_id")
    if not uid:
        return None
    return User.query.get(uid)

def login_required(view):
    """Decorator: protects a route so only logged-in users can access it."""
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("user_id"):
            flash("Please log in first.", "error")
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped
    