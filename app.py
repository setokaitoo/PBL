from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
import random, string
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from models import db, Store
import os 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///muroran.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = os.urandom(24)

# dbのインスタンスを作成し、アプリに関連付け
#db = SQLAlchemy()

# アプリケーションに db を関連付ける
db.init_app(app)

#db = SQLAlchemy(app)

@app.before_request
def setup():
    with app.app_context():
        db.create_all()

uid = ''

#インスタンス化
login_manager = LoginManager()
#アプリにログイン機能を紐づける
login_manager.init_app(app)
#未ログインユーザーを転送する 
login_manager.login_view = 'login'

# 初回リクエスト時にテーブルを作成
@app.before_request
def setup():
    db.create_all()

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.String(255), primary_key=True)
    mailaddress = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    #def check_password(self, password):
    #    return check_password_hash(self.password_hash, password)
    
class Post(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    post_name = db.Column(db.String(255))
    time1 = db.Column(db.DateTime, nullable=False)
    place1 = db.Column(db.String(255), nullable=False)
    time2 = db.Column(db.DateTime, nullable=False)
    place2 = db.Column(db.String(255), nullable=False)
    time3 = db.Column(db.DateTime, nullable=False)
    place3 = db.Column(db.String(255), nullable=False)
    time4 = db.Column(db.DateTime, nullable=False)
    place4 = db.Column(db.String(255), nullable=False)
    # 複合主キーを定義
    __table_args__ = (PrimaryKeyConstraint(id, post_name),)
    
#class Store(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.String(80), nullable=False)
    #category = db.Column(db.String(50), nullable=False)
    #homepage = db.Column(db.String(255), nullable=True)  # ホームページURL
    #location = db.Column(db.String(255), nullable=True)  # 住所や地図リンク
    

    
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
        newpass = request.form['password']
        user_id = request.form['user_id']      
        user = User.query.filter_by(id=user_id).first()
        if user is not None:
            user = User.query.filter_by(password=newpass).first()
            if user is not None:
                uid = user_id
                return redirect(url_for('mypage',user_id=user_id))           
            else:
                flash('パスワードが間違っています。再度入力してください。')
                return redirect(url_for('login'))
        else:
            flash('このユーザーIDは存在しません。再度入力してください。')
            return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template('login.html')

#新規登録画面
@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    if request.method == 'POST':
        newpass = request.form['password']
        mail = request.form['mail']
        newid = request.form['id']
        
        user = User.query.filter_by(id=newid).first()
        if user is not None:
            flash('このユーザーIDは既に使用されています。')
            return redirect(url_for('adduser'))#再度登録画面へ
           
            
            
        else:
            user = User(id=newid, mailaddress=mail, password=newpass)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
            
        
        #return redirect(url_for('createuser', id=newid, mail=mail))
    return render_template('adduser.html')

#新規登録結果画面
@app.route('/createuser')

def createuser():
    user_id = request.args.get('id')
    return redirect(url_for('mypage', user_id=user_id))

# マイページ画面
@app.route('/mypage')
def mypage():
    user_id = request.args.get('user_id')
    
    # ログイン中のユーザーの投稿を取得
    user_posts = Post.query.filter_by(id=user_id).order_by(Post.id.desc()).all()
    return render_template('mypage.html', user_id=user_id, posts=user_posts)

# 店舗検索結果画面
@app.route('/result')
def result():
    category = request.args.get('category')
    # データベースから該当するお店を検索
    
    stores = Store.query.filter_by(category=category).all()

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

#スケジュール投稿画面
@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    if request.method == 'POST':
        # フォームからデータを取得
        title = request.args.get('post_title')
        time1 = datetime.strptime(request.form['time1'], '%Y-%m-%dT%H:%M')
        place1 = request.form['place1']
        
        if request.form['time2'] != '':
            time2 = datetime.strptime(request.form['time2'], '%Y-%m-%dT%H:%M')
            place2 = request.form['place2']
        else:
            time2 = None
            place2 = None
            
        if request.form['time3'] != '':
            time3 = datetime.strptime(request.form['time3'], '%Y-%m-%d %H:%M')
            place3 = request.form['place3']
        else:
            time3 = None
            place3 = None
            
        if request.form['time4'] != '':
            time4 = datetime.strptime(request.form['time4'], '%Y-%m-%d %H:%M')
            place4 = request.form['place4']
        else:
            time4 = None
            place4 = None

        post = Post.query.filter_by(id=uid, post_name=title).first()
        
        if post is not None:
            return render_template('schedule.html',id=id)
        # データを保存
        new_post = Post(id=uid, post_name=title, time1=time1, place1=place1, time2=time2, place2=place2, 
                        time3=time3, place3=place3, time4=time4, place4=place4)
        db.session.add(new_post)
        db.session.commit()

        # 投稿後にマイページにリダイレクト
        return redirect(url_for('mypage'))
    if request.method == 'GET':
        return render_template('schedule.html')
    
#スケジュール一覧画面
@app.route('/schedulelist')
def schedulelist():
    try:
        # データベースからすべての投稿を取得
        all_posts = Post.query.all()
        return render_template('schedulelist.html', posts=all_posts)
    except Exception as e:
        return f"エラーが発生しました: {e}", 400
    




if __name__ == '__main__':
    app.run()