from flask import Flask
from flask import render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from datetime import datetime
import pytz
import random, string
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
import os
import list
from werkzeug.utils import secure_filename
import random
import csv
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///muroran.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # アップロード先のディレクトリ
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  # 許可するファイル形式


app.secret_key = os.urandom(24)

# dbのインスタンスを作成し、アプリに関連付け
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


#@app.before_request
#def setup():
    #with app.app_context():
        #db.create_all()

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
    
def load_stores_from_csv(file_path='data/stores.csv'):
    stores = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                stores.append(row)
    except FileNotFoundError:
        print(f"CSVファイルが見つかりません: {file_path}")
    return stores


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.String(255), primary_key=True)
    mailaddress = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    #def check_password(self, password):
    #    return check_password_hash(self.password_hash, password)
    
class Post(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    post_name = db.Column(db.String(255), primary_key=True)
    time1 = db.Column(db.DateTime, nullable=False)
    place1 = db.Column(db.String(255), nullable=False)
    image1_path = db.Column(db.String(200))  # 画像パスを保存するカラム
    time2 = db.Column(db.DateTime, nullable=True)
    place2 = db.Column(db.String(255), nullable=True)
    image2_path = db.Column(db.String(200))  # 画像パスを保存するカラム
    time3 = db.Column(db.DateTime, nullable=True)
    place3 = db.Column(db.String(255), nullable=True)
    image3_path = db.Column(db.String(200))  # 画像パスを保存するカラム
    time4 = db.Column(db.DateTime, nullable=True)
    place4 = db.Column(db.String(255), nullable=True)
    image4_path = db.Column(db.String(200))  # 画像パスを保存するカラム
    image_path = db.Column(db.String(255), nullable=True)  # 画像の保存先パスを追加
    # 複合主キーを定義
    __table_args__ = (PrimaryKeyConstraint(id, post_name),)
    



@app.route('/delete_post/<string:post_name>', methods=['POST'])

def delete_post(post_name):
    global uid
    try:
        

        # 指定された投稿を取得
        post = Post.query.filter_by(id=uid, post_name=post_name).first()

        # 投稿が存在しない場合の処理
        if not post:
            flash('投稿が見つかりませんでした。')
            return redirect(url_for('mypage'))

        # 投稿をデータベースから削除
        db.session.delete(post)
        db.session.commit()
        flash('投稿を削除しました。')

    except Exception as e:
        flash(f'エラーが発生しました: {e}')

    return redirect(url_for('mypage'))



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



# 画像ファイルのリスト
images = [
    'static/yakitori.jpg',
    'static/curry.jpg',
    'static/工場.jpeg',
    'static/地球岬.jpg'
]

# ホーム画面
@app.route('/')
def home():
    global uid
    #store_set()
    if uid:
        return render_template('newhome.html', images=images)
    else:
        return render_template('home.html', images=images)

#ログイン後のホーム画面
@app.route('/newhome')
def newhome():
    if uid:
    #store_set()
        return render_template('newhome.html', images=images)
    else:
        return redirect(url_for('home'))

# ジャンル検索画面
@app.route('/search')
def search():
    return render_template('search.html')

# ログイン画面とユーザー登録処理
@app.route('/login', methods=['GET', 'POST'])
def login():
    global uid
    if request.method == 'POST':
        newpass = request.form['password']
        user_id = request.form['user_id']      
        user = User.query.filter_by(id=user_id).first()
        if user is not None:
            user = User.query.filter_by(password=newpass).first()
            if user is not None:
                uid = user_id
                return redirect(url_for('newhome',images=images))           
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
    global uid
    
    if uid:
        # ログイン中のユーザーの投稿を取得
        user_posts = Post.query.filter_by(id=uid).order_by(Post.id.desc()).all()
        return render_template('mypage.html', user_id=uid, posts=user_posts)
    else:
        return redirect(url_for('login'))

# 店舗検索結果画面
@app.route('/result2')
def result2():
    category = request.args.get('category')
    # CSVからデータを読み込む
    stores = load_stores_from_csv()
    # 指定されたカテゴリのお店をフィルタリング
    filtered_stores = [store for store in stores if store['category'] == category]

    return render_template('result2.html', stores=filtered_stores)

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
        # 必須フィールドの取得
        title = request.form['post_title']
        time1 = datetime.strptime(request.form['time1'], '%Y-%m-%dT%H:%M')
        place1 = request.form['place1']

        # 画像アップロード処理
        def save_image(file):
            if file and allowed_file(file.filename):
                filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{secure_filename(file.filename)}"
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                return f"uploads/{filename}"  # データベース用パス
            return None

        image1_path = save_image(request.files.get('image1'))
        image2_path = save_image(request.files.get('image2'))
        image3_path = save_image(request.files.get('image3'))
        image4_path = save_image(request.files.get('image4'))

        # 新しい投稿を作成して保存
        new_post = Post(
            id=uid,
            post_name=title,
            time1=time1,
            place1=place1,
            image1_path=image1_path,
            time2=datetime.strptime(request.form['time2'], '%Y-%m-%dT%H:%M') if request.form.get('time2') else None,
            place2=request.form.get('place2'),
            image2_path=image2_path,
            time3=datetime.strptime(request.form['time3'], '%Y-%m-%dT%H:%M') if request.form.get('time3') else None,
            place3=request.form.get('place3'),
            image3_path=image3_path,
            time4=datetime.strptime(request.form['time4'], '%Y-%m-%dT%H:%M') if request.form.get('time4') else None,
            place4=request.form.get('place4'),
            image4_path=image4_path
        )
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('mypage'))
    
    if request.method == 'GET':
        if uid:
            return render_template('schedule.html')
        else:
            return redirect(url_for('login'))
#スケジュール一覧画面
@app.route('/schedulelist')
def schedulelist():
    global uid
    try:
        # データベースからすべての投稿を取得
        all_posts = Post.query.all()
        if uid:
            return render_template('newschedulelist.html', posts=all_posts)
        else:
            return render_template('schedulelist.html', posts=all_posts)
    except Exception as e:
        return f"エラーが発生しました: {e}", 400
    
@app.route('/logout')
def logout():
    global uid
    uid = ''
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()