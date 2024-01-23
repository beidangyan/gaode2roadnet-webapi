from flask import Flask
import config
from exts import db
from models import RoadUnit
from blueprints.roadCollect import bp
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(config)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(bp)


if __name__ == '__main__':
    app.run()
