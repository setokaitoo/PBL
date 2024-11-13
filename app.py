from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///muroran.db'
db = SQLAlchemy(app)

#インスタンス化
login_manager = LoginManager()
#アプリにログイン機能を紐づける
login_manager.init_app(app)
#未ログインユーザーを転送する 
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    mailaddress = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    #def check_password(self, password):
    #    return check_password_hash(self.password_hash, password)
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time1 = db.Column(db.DateTime, nullable=False)
    place1 = db.Column(db.String(255), nullable=False)
    time2 = db.Column(db.DateTime, nullable=False)
    place2 = db.Column(db.String(255), nullable=False)
    time3 = db.Column(db.DateTime, nullable=False)
    place3 = db.Column(db.String(255), nullable=False)
    time4 = db.Column(db.DateTime, nullable=False)
    place4 = db.Column(db.String(255), nullable=False)
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    
# ホーム画面
@app.route('/')
def home():
    return render_template('home.html')

# ジャンル検索画面
@app.route('/search')
def search():
    return render_template('search.html')

# ログイン画面とユーザー登録処理
@app.route('/login', methods=['GET', 'POST'])
def login():
    usert = User
    if request.method == 'POST':
        password = request.form['password']
        user_id = request.form['user_id']
        
        user = User.query.filter_by(user_id=usert.id).first()
        if user is not None:
            user = User.query.filter_by(password=usert.password).first()
            if user is not None:
                return redirect('mypage')           
            else:
                return redirect('login')
        
        return redirect(url_for('mypage', password=password, user_id=user_id))
    return render_template('login.html')

#新規登録画面
@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    if request.method == 'POST':
        password = request.form['password']
        mail = request.form['mail']
        return redirect(url_for('login', password=password, mail=mail))
    return render_template('adduser.html')

# マイページ画面
@app.route('/mypage')
def mypage():
    username = request.args.get('username')
    user_id = request.args.get('user_id')
    return render_template('mypage.html', username=username, user_id=user_id)

# 店舗検索結果画面
@app.route('/result')
def result():
    # 店舗リストを仮に定義
    stores = [
        {'name': 'カフェ A', 'id': 1},
        {'name': 'レストラン B', 'id': 2},
        {'name': '書店 C', 'id': 3},
    ]
    return render_template('result.html', stores=stores)

# 店舗詳細画面
@app.route('/details/<int:store_id>')
def details(store_id):
    # 店舗情報を仮に定義
    store_details = {'id': store_id, 'name': f'店舗 {store_id}', 'description': '詳細情報'}
    return render_template('details.html', store=store_details)

# マップ画面
@app.route('/map')
def map():
    return render_template('map.html')


if __name__ == '__main__':
    app.run()