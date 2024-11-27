from models import db, Store, app

def seed_data():
    # アプリケーションコンテキスト内で操作を実行
    with app.app_context():
        # データベースの初期化（必要に応じて）
        db.create_all()

        # データの追加
        stores = [
            Store(name="THE LAMP ROOM CAFE", category="軽食", 
                  homepage="https://tabelog.com/hokkaido/A0108/A010803/1073644/",
                  location="https://www.google.com/maps/d/viewer?mid=1qOVBnvYFo92NqgpxxWFQ7HffDQb8iUo&ll=42.34674620000001%2C141.0328872&z=11"),
            Store(name="カフェA", category="軽食", 
                  homepage="https://example.com/cafe_a",
                  location="https://maps.google.com/?q=カフェA"),
            Store(name="レストランB", category="がっつり", 
                  homepage="https://example.com/restaurant_b",
                  location="https://maps.google.com/?q=レストランB"),
            Store(name="スイーツC", category="甘いもの", 
                  homepage="https://example.com/sweets_c",
                  location="https://maps.google.com/?q=スイーツC"),
            Store(name="CAFF工房MISUZU×食品倉庫 室蘭店",category="甘いもの",
                  homepage="https://www.misuzucoffee.com/",
                  location="https://www.google.com/maps/d/edit?mid=1qOVBnvYFo92NqgpxxWFQ7HffDQb8iUo&ll=42.349110400417466%2C141.01611710999043&z=17")
            
        ]

        # データベースにデータを追加
        db.session.add_all(stores)
        db.session.commit()
        print("データの追加が完了しました！")

if __name__ == "__main__":
    seed_data()