import csv
from models import db, Store
from flask import Flask

def seed_data(csv_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # データベースに新しいStoreを追加
            store = Store(
                name=row['name'],
                category=row['category'],
                homepage=row['homepage'],
                location=row['location']
            )
            db.session.add(store)
        db.session.commit()
        
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print("CSVヘッダー:", reader.fieldnames)  # ヘッダー行を表示
            for row in reader:
                print("読み込んだ行:", row)

if __name__ == "__main__":
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///muroran.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        seed_data('seed_data.csv')
        
    