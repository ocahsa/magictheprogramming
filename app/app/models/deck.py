from .db import db
import datetime

class Deck(db.Model):
    __tablename__ = 'decks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    format = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(10000), nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.String(2000), default=datetime.datetime.now().strftime('%x'))
    private = db.Column(db.Boolean, default=False)

    owner = db.relationship("User", backref="decks")
    decklist = db.relationship("Card", secondary='decklists', backref="decks")
    comments = db.relationship("Comment", backref="decks", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'format': self.format,
            'description': self.description,
            'owner': self.owner.to_dict(),
            'decklist': [card.to_dict() for card in self.decklist],
            'private': self.private,
            'created_at': self.created_at,
            'owner_id': self.owner_id
        }