from .models import db, Item

def seed_data():
    item1 = Item(name='Sample Item 1', description='Description 1')
    item2 = Item(name='Sample Item 2', description='Description 2')
    db.session.add(item1)
    db.session.add(item2)
    db.session.commit()
