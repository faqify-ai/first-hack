from api.core import Mixin
from .base import db

# Note that we use sqlite for our tests, so you can't use Postgres Arrays
class QuestionAnswer(Mixin, db.Model):
    """QuestionAnswer Table."""

    __tablename__ = "question_answer"

    a_id = db.Column(db.Integer, nullable=False, primary_key=True)
    q_id = db.Column(db.Integer, nullable=False)
    answer = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=True)

    def __init__(self, a_id: int, q_id: int, answer: str, author: str):
        self.a_id = a_id
        self.q_id = q_id
        self.answer = answer
        self.author = author

    def __repr__(self):
        return f"<QuestionAnswer {self.a_id}>"