
from sqlalchemy.sql import func

from configs.db import db


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    items = db.relationship('Item', backref='post',lazy="dynamic")
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __str__(self) -> str:
        return f'<Store {self.name}>'

    def __repr__(self):
        return f'<Store {self.name}>'
