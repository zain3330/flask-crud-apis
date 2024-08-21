from . import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=True)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
