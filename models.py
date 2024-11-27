from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# データベースURIの設定（muroran.db を使用）
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///muroran.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemyインスタンスを作成
db = SQLAlchemy(app)

# モデル定義
class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    homepage = db.Column(db.String(200), nullable=True)
    location = db.Column(db.String(200), nullable=True)

# データベースの初期化用関数
def initialize_db():
    with app.app_context():
        db.create_all()