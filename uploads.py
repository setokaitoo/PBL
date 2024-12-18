import os

UPLOAD_FOLDER = 'static/uploads'

# ディレクトリが存在しない場合は作成
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
