from flask import request, jsonify

from . import bp
from app.models import Marvel, User

@bp.get('/marvels')
def api_marvel():
    result = []
    marvels = Marvel.queery.all()
    for marvel in marvels:
        result.append({
            'id':marvel.id,
            'name': marvel.name,
            'description': marvel.description,
            'comics appeared in': marvel.comics_appeared_in,
            'super_power': marvel.super_power,
            'timestamp': marvel.date_created,
            'author': marvel.owner
        })
    return jsonify(result), 200

@bp.get('/marvel/<username>')
def user_marvel(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify([{
            'id':marvel.id,
            'name': marvel.name,
            'description': marvel.description,
            'comics appeared in': marvel.comics_appeared_in,
            'super_power': marvel.super_power,
            'timestamp': marvel.date_created,
            'author': marvel.owner
        }for marvel in user.marvel]), 200
    return jsonify({'message':'Invalid Username'}), 404


@bp.get('/marvel/<id>')
def get_marvel(id):
    try:
        marvel = Marvel.query.get(id)
        return jsonify([{
            'id':marvel.id,
            'name': marvel.name,
            'description': marvel.description,
            'comics appeared in': marvel.comics_appeared_in,
            'super_power': marvel.super_power,
            'timestamp': marvel.date_created,
            'author': marvel.owner
        }])
    except:
        return jsonify ({'mmessage':'Invalid Superhero Id'}), 404
