from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
 
 
class BlogArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))
 
#@app.route('/')
#def blog():
    #return render_template('index.html')

#if __name__ == '__main__':
    #app.run()
    
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
        username = request.form['username']
        user_id = request.form['user_id']
        return redirect(url_for('mypage', username=username, user_id=user_id))
    return render_template('login.html')

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