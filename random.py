import random
import string
import csv

# 10万件の会員IDを生成する関数
def generate_ids(num_ids):
    ids = set()
    
    while len(ids) < num_ids:
        id = ''.join(random.choices(string.ascii_uppercase, k=3)) + ''.join(random.choices(string.digits, k=5))
        ids.add(id)
        
    return list(ids)

# 10万件の会員IDを生成
ids = generate_ids(100000)

# CSVファイルに保存
csv_file_path = "ids.csv"
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID'])  # ヘッダ
    for id in ids:
        writer.writerow([id])  # ID

csv_file_path

print(ids)
