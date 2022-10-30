from flask import Blueprint, request
from init import db
from datetime import date
from models.comic import Comic, ComicSchema





comics_bp = Blueprint('cards', __name__, url_prefix='/comics')


@comics_bp.route('/')
# @jwt_required()
def get_all_cards():
    # return 'all_cards route'
    # if not authorize():
    #     return {'error': 'You must be an admin'}, 401

    stmt = db.select(Comic).order_by(Comic.release.desc())
    comics = db.session.scalars(stmt)
    return ComicSchema(many=True).dump(comics)