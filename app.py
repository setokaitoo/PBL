from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///muroran.db'
db = SQLAlchemy(app)
 
 
class user_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mailaddress = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    
class post_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time1 = db.Column(db.DateTime, nullable=False)
    place1 = db.Column(db.String(255), nullable=False)
    time2 = db.Column(db.DateTime, nullable=False)
    place2 = db.Column(db.String(255), nullable=False)
    time3 = db.Column(db.DateTime, nullable=False)
    place3 = db.Column(db.String(255), nullable=False)
    time4 = db.Column(db.DateTime, nullable=False)
    place4 = db.Column(db.String(255), nullable=False)
    
    
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
    if request.method == 'POST':
        password = request.form['password']
        user_id = request.form['user_id']
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