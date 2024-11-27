from models import db, Store

def seed_data():
    stores = [
        Store(name="THE LAMP ROOM CAFE", category="軽食", homepage="https://tabelog.com/hokkaido/A0108/A010803/1073644/", location="https://www.google.com/maps/d/viewer?mid=1qOVBnvYFo92NqgpxxWFQ7HffDQb8iUo&ll=42.34674620000001%2C141.0328872&z=11"),
        Store(name="カフェA", category="軽食", homepage="https://example.com/cafe_a", location="https://maps.google.com/?q=カフェA"),
        Store(name="レストランB", category="がっつり", homepage="https://example.com/restaurant_b", location="https://maps.google.com/?q=レストランB"),
        Store(name="スイーツC", category="甘いもの", homepage="https://example.com/sweets_c", location="https://maps.google.com/?q=スイーツC")
    ]
    db.session.add_all(stores)
    db.session.commit()