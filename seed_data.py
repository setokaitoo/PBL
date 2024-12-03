from models import db, Store

def seed_data():
    stores = [
        Store(name="THE LAMP ROOM CAFE", category="軽食", homepage="https://tabelog.com/hokkaido/A0108/A010803/1073644/", location="https://www.google.com/maps/d/viewer?mid=1qOVBnvYFo92NqgpxxWFQ7HffDQb8iUo&ll=42.34674620000001%2C141.0328872&z=11"),
        Store(name="CAFE工房MISUZU×食品倉庫 室蘭店", category="軽食", homepage="https://www.instagram.com/kobomuroran?igsh=NG9nN21sbHhtemti", location="https://www.google.com/maps/d/viewer?mid=1qOVBnvYFo92NqgpxxWFQ7HffDQb8iUo&ll=42.34674620000001%2C141.0328872&z=11"),
        Store(name="TENTO", category="軽食", homepage="https://npotentoten.wixsite.com/tentotenwebsite", location="https://www.google.com/maps/d/viewer?mid=1qOVBnvYFo92NqgpxxWFQ7HffDQb8iUo&ll=42.34674620000001%2C141.0328872&z=11"),
        Store(name="蘭東館", category="軽食", homepage="https://www.google.co.jp/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjAqvOX5YuKAxWth1YBHfOiKRkQFnoECDoQAQ&url=https%3A%2F%2Ftabelog.com%2Fhokkaido%2FA0108%2FA010803%2F1020747%2F&usg=AOvVaw1PTcK7dscbl00UU7SRRhW5&opi=89978449", location="https://www.google.com/maps/d/viewer?mid=1qOVBnvYFo92NqgpxxWFQ7HffDQb8iUo&ll=42.34674620000001%2C141.0328872&z=11"),
        Store(name="えんとつ町のドーナツ屋さん", category="軽食", homepage="https://entotsudonut.com/", location="https://www.google.com/maps/d/viewer?mid=1qOVBnvYFo92NqgpxxWFQ7HffDQb8iUo&ll=42.34674620000001%2C141.0328872&z=11"),
        Store(name="レストランB", category="がっつり", homepage="https://example.com/restaurant_b", location="https://maps.google.com/?q=レストランB"),
        Store(name="スイーツC", category="甘いもの", homepage="https://example.com/sweets_c", location="https://maps.google.com/?q=スイーツC"),
        Store(name="伊達和さび 室蘭店", category="海鮮", homepage="http://www.date-wasabi.com/", location="https://www.google.com/maps/d/viewer?hl=ja&mid=1VvQO8_9-EHnf5H9j"),
        Store(name="室蘭ランプ亭海の門", category="海鮮", homepage="https://www.google.co.jp/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiAm83d44uKAxVAafUHHRHVF0IQFnoECAwQAQ&url=https%3A%2F%2Ftabelog.com%2Fhokkaido%2FA0108%2FA010803%2F1003661%2F&usg=AOvVaw12vVY16WagE3905-AkzBRq&opi=89978449", location="https://www.google.com/maps/d/viewer?hl=ja&mid=1VvQO8_9-EHnf5H9j"),
        Store(name="海鮮ビアホール汽笛", category="海鮮", homepage="https://kaisenbeerhallkiteki.owst.jp/", location="https://www.google.com/maps/d/viewer?hl=ja&mid=1VvQO8_9-EHnf5H9j"),
        Store(name="海鮮炭火料理 空雅", category="海鮮", homepage="https://www.bing.com/ck/a?!&&p=739b515d5cd180e4cd697b42626737c14238ff76cd633647842c911d2ef3f7d1JmltdHM9MTczMDc2NDgwMA&ptn=3&ver=2&hsh=4&fclid=350d644a-d8c6-65a0-3df6-74a7d9bc64af&psq=%e5%ae%a4%e8%98%ad+%e7%a9%ba%e9%9b%85&u=a1aHR0cHM6Ly90YWJlbG9nLmNvbS9ob2trYWlkby9BMDEwOC9BMDEwODAzLzEwNjAwNDQvP21zb2NraWQ9MzUwZDY0NGFkOGM2NjVhMDNkZjY3NGE3ZDliYzY0YWY&ntb=1", location="https://www.google.com/maps/d/viewer?hl=ja&mid=1VvQO8_9-EHnf5H9j"),
        Store(name="味処いずみ", category="海鮮", homepage="https://www.bing.com/ck/a?!&&p=177a4a910ccfa138d7efbe17b645bd2a10b5140cac04e87b41b5a769add05d59JmltdHM9MTczMDc2NDgwMA&ptn=3&ver=2&hsh=4&fclid=350d644a-d8c6-65a0-3df6-74a7d9bc64af&psq=%e5%ae%a4%e8%98%ad%e3%80%80%e3%81%84%e3%81%9a%e3%81%bf&u=a1aHR0cHM6Ly90YWJlbG9nLmNvbS9ob2trYWlkby9BMDEwOC9BMDEwODAzLzEwMDY3NjYvP21zb2NraWQ9MzUwZDY0NGFkOGM2NjVhMDNkZjY3NGE3ZDliYzY0YWY&ntb=1", location="https://www.google.com/maps/d/viewer?hl=ja&mid=1VvQO8_9-EHnf5H9j"),
    ]
    db.session.add_all(stores)
    db.session.commit()