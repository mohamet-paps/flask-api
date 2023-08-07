from flask.views import MethodView
from flask_smorest import Blueprint

from schema.item_schema import ItemSchema
from models.item_model import Item

from configs.db import db


blp = Blueprint("items", __name__, url_prefix="/items",
                description="Operations on Items")


Items = [
    {
        "id": 1,
        "name": "bobon",
        "price": 200
    },
    {
        "id": 2,
        "name": "oapokdso",
        "price": 200
    }, {
        "id": 3,
        "name": "Hasd",
        "price": 200
    }
]


@blp.route("/")
class Items(MethodView):

    @blp.response(200, ItemSchema(many=True))
    def get(self):
        items = Item.query.all()
        return items

    @blp.arguments(ItemSchema)
    @blp.response(200, ItemSchema)
    def post(self, item_data):
        new_item = Item(**item_data)
        try:
            db.session.add(new_item)
            db.session.commit()
            return new_item
        except Exception as e:
            print(e.__str__())


@blp.route("/<int:item_id>")
class ItemsOne(MethodView):

    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = db.get_or_404(Item, item_id)
        return item
