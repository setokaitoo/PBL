from flask_sqlalchemy import SQLAlchemy

# SQLAlchemyのインスタンスを初期化
db = SQLAlchemy()

# Storeモデルの定義
class Store(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    category = db.Column(db.String(50))