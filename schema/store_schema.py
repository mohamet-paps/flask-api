import marshmallow as ma

from schema.item_schema import ItemSchema


class StoreSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    name = ma.fields.String()
    items = ma.fields.List(ma.fields.Nested(ItemSchema, dump_only=True))


class CreateStoreSchema(ma.Schema):
    name = ma.fields.String()
