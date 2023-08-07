
from sqlalchemy.sql import func

from configs.db import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float(5, 2), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __str__(self) -> str:
        return f'<Item {self.name}>'

    def __repr__(self):
        return f'<Item {self.name}>'
