from app import app, db
from flask_migrate import Migrate
from flask import Flask

# Migrateインスタンスを作成
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run()

