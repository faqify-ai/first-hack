from api.core import Mixin
from .base import db


class Source(Mixin, db.Model):
    """Source Table."""

    __tablename__ = "source"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    source = db.Column(db.String, nullable=False)
  
    def __init__(self, id: int, source: str):
        self.id = id
        self.source = source

    def __repr__(self):
        return f"<Source {self.source}>"
