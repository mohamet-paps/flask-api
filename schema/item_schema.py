import marshmallow as ma


class ItemSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    name = ma.fields.String()
    price = ma.fields.Int()
    store_id = ma.fields.Int()
