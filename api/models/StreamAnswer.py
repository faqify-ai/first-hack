from api.core import Mixin
from .base import db

# Note that we use sqlite for our tests, so you can't use Postgres Arrays
class StreamAnswer(Mixin, db.Model):
    """StreamAnswer Table."""

    __tablename__ = "stream_answer"

    sa_id = db.Column(db.Integer, nullable=False, primary_key=True)
    q_id = db.Column(db.Integer, nullable=False)
    blob = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=True)

    def __init__(self, sa_id: int, q_id: int, blob: str, author: str):
        self.sa_id = sa_id
        self.q_id = q_id
        self.blob = blob
        self.author = author

    def __repr__(self):
        return f"<StreamAnswer {self.sa_id}>"
