from flask import Blueprint, jsonify, request
from .models import Item, db

bp = Blueprint('routes', __name__)

@bp.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.as_dict() for item in items])

@bp.route('/item', methods=['POST'])
def create_item():
    data = request.get_json()
    item = Item(name=data['name'], description=data.get('description'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.as_dict()), 201

@bp.route('/item/<int:id>', methods=['PUT'])
def update_item(id):
    item = Item.query.get(id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    data = request.get_json()
    item.name = data['name']
    item.description = data.get('description')
    db.session.commit()
    return jsonify(item.as_dict())

@bp.route('/item/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get(id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    db.session.delete(item)
    db.session.commit()
    return '', 204

@bp.route('/seed', methods=['GET'])
def seed_db():
    item1 = Item(name='Sample Item 1', description='Description 1')
    item2 = Item(name='Sample Item 2', description='Description 2')
    db.session.add(item1)
    db.session.add(item2)
    db.session.commit()
    return jsonify({'message': 'Database seeded!'})
