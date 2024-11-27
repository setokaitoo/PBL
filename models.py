from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    homepage = db.Column(db.String(255), nullable=True)  # ホームページURL
    location = db.Column(db.String(255), nullable=True)  # 住所や地図リンク