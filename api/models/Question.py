from api.core import Mixin
from .base import db


class Question(Mixin, db.Model):
    """Question Table."""

    __tablename__ = "question"

    q_id = db.Column(db.Integer, nullable=False, primary_key=True)
    q_key = db.Column(db.String, nullable=False)
    q_variant = db.Column(db.String, nullable=False)
    q_date_created = db.Column(db.String, nullable=False)

    def __init__(self, q_id: int, q_key: str, q_variant: str, q_date_created: str):
        self.q_id = q_id
        self.q_key = q_key
        self.q_variant = q_variant
        self.q_date_created = q_date_created

    def __repr__(self):
        return f"<Question {self.q_key}>"
