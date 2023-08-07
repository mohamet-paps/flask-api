from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy


from ressources.store import blp as StoreBlueprint
from ressources.item import blp as ItemBlueprint

from configs.db import db

import models


def create_app():

    app = Flask(__name__)

    app.config["API_TITLE"] = "Store Api"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///storeApi.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    api = Api(app)

    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(ItemBlueprint)

    with app.app_context():
        db.create_all()

    @app.get("/")
    def get_hello():
        return {"msg": "Hellow APi"}

    return app


app = create_app()
