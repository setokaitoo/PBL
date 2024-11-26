from models import db, Store

def seed_data():
    stores = [
        Store(name="カフェA", category="軽食", homepage="https://example.com/cafe_a", location="https://maps.google.com/?q=カフェA"),
        Store(name="レストランB", category="がっつり", homepage="https://example.com/restaurant_b", location="https://maps.google.com/?q=レストランB"),
        Store(name="スイーツC", category="甘いもの", homepage="https://example.com/sweets_c", location="https://maps.google.com/?q=スイーツC")
    ]
    db.session.add_all(stores)
    db.session.commit()