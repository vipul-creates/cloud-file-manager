# models.py
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db

class User(db.Model):
    __tablename__ = "users"

    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name          = db.Column(db.String(100), nullable=False)
    email         = db.Column(db.String(150), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role          = db.Column(db.String(10), default="user", nullable=False)
    storage_used  = db.Column(db.BigInteger, default=0, nullable=False)
    created_at    = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Folder(db.Model):
    __tablename__ = "folders"

    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id    = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name       = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class File(db.Model):
    __tablename__ = "files"

    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id       = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    folder_id     = db.Column(db.Integer, db.ForeignKey('folders.id'), nullable=True) # NULL means root
    filename      = db.Column(db.String(255), nullable=False)
    file_size     = db.Column(db.BigInteger, nullable=False)
    mime_type     = db.Column(db.String(100))
    uploaded_at   = db.Column(db.DateTime, default=datetime.utcnow)