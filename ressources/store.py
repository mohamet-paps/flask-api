from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.inspection import inspect


from schema.store_schema import StoreSchema, CreateStoreSchema

from models.store_model import Store
from configs.db import db

blp = Blueprint("stores", __name__, url_prefix="/stores",
                description="Operations on stores")


@blp.route("/")
class Stores(MethodView):

    @blp.response(200, StoreSchema(many=True))
    def get(self):
        stores = Store.query.all()
        print(stores)
        return stores

    @blp.arguments(CreateStoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        store = Store(**store_data)
        db.session.add(store)
        db.session.commit()
        return store


@blp.route("/<int:store_id>")
class StoreById(MethodView):

    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = db.get_or_404(Store, store_id)
        return store
