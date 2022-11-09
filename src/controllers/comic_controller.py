from ast import If
from flask import Blueprint, request,abort
from init import db
from datetime import date, datetime
from models.comic import Comic, ComicSchema
from models.review import ReviewSchema, Review
from controllers.auth_controller import authorize,check_user
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.sql import func, select
import random
from models.user import User

comics_bp = Blueprint('comics', __name__, url_prefix='/users')

# GETS ALL COMIC BOOKS FROM ALL USERS
@comics_bp.route('/comics/')
@jwt_required()
def get_all_comics():
    # selects all comics order by title
    stmt = db.select(Comic).order_by(Comic.title.desc())
    comics = db.session.scalars(stmt)
    return ComicSchema(many=True).dump(comics)

# GETS ALL COMIC BOOKS FROM USER ACCOUNT
@comics_bp.route('/<int:id>/comics/')
@jwt_required()
def get_user_comics(id):
    # CHECKS CORRECT USER ACCOUNT
    check_user(id)
    # query comic and filter_by user_id
    stmto = db.select(Comic).filter_by(user_id=id)
    comics = db.session.scalars(stmto)

    return ComicSchema(many=True).dump(comics)
  
# GETS COMIC BOOK BY COMICBOOK ID
@comics_bp.route('/<int:id>/search/<int:comic_id>/')
@jwt_required()
def search_by_id(comic_id,id):
    # CHECKS CORRECT USER ACCOUNT
    check_user(id)
    stmt = db.select(Comic).filter_by(id=comic_id).filter_by(user_id=id)
    comic = db.session.scalar(stmt)
    
    if not comic:
        return {'error': f'Comicbook not found with the id: {comic_id}' },404
   
    else:
        
        return ComicSchema().dump(comic)

# DELETE COMIC BOOK BY ID
@comics_bp.route('<int:id>/comics/remove/<int:comic_id>/', methods=['DELETE'])
@jwt_required()
def delete_one_comic(comic_id,id):
    check_user(id)
    stmt = db.select(Comic).filter_by(id=comic_id).filter_by(user_id=id)
    comic = db.session.scalar(stmt)
    # CHECKS COMICBOK ID EXISTS 
    if comic:
        db.session.delete(comic)
        db.session.commit()
        return {'message': f"Comic book'{comic.title}  deleted successfully"}
    else:
        return {'error': f'comicbook not found with the id {id}'}, 404

# UPDATE COMIC BOOK
@comics_bp.route('/comics/<int:id>/update/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_comic(id):
    user_id = get_jwt_identity()  
    stmt = db.select(Comic).filter_by(id=id).filter_by(user_id=user_id)
    comic = db.session.scalar(stmt)
    if comic and user_id:
        comic.title = request.json.get('title') or comic.title
        comic.author = request.json.get('author') or comic.author
        comic.comic_value = request.json.get('comic_value') or comic.comic_value
        db.session.commit()      
        return ComicSchema().dump(comic)
    else:
        return {'error': f'Comicbook not found with the id: {id}'}, 404

# ADD NEW COMICBOOK 
@comics_bp.route('<int:id>/comics/add', methods=['POST'])
@jwt_required()
def create_comic(id):
    # CHECKS CORRECT USER
    check_user(id)
    data = ComicSchema().load(request.json)
    query = db.select(Comic.title).filter_by(user_id=id)
    stmt = db.session.scalars(query).all()
    
    comic = Comic(
        title = data['title'],
        author = data['author'],
        comic_value = data['comic_value'],
        user_id = get_jwt_identity()
        )
    # CHECKS IF COMICBOOK TITLE EXIST FOR USER ID
    
    if data['title']  in stmt or id in stmt:
        return {'error':f'Comicbook {comic.title} already exists for user'}
         
    else:
        db.session.add(comic) 
        db.session.commit() 
        return {'message': f'Comicbook {comic.title} successfully added to libary'}
        

# GETS TOTAL NUMBER OF COMICBOOKS AND THE TOTAL VALUE   
@comics_bp.route('/<int:id>/comics/total/')
@jwt_required()
def get_user_total(id):
    # uses func to count how may comic id's in users libary
    user_id = get_jwt_identity()  
    stmt = db.session.query(func.count(Comic.id)).filter_by(user_id=id)
    comicso = db.session.scalar(stmt)
    # uses fun sum to add up all the values from comic values
    stmt = db.session.query(func.sum(Comic.comic_value)).filter_by(user_id=id)
    comics = db.session.scalar(stmt)
    
    if int(user_id) == id:
        return {
            'totalComics': comicso,
            'totalValue': round(comics, 2)
        }
       
    else:
        return abort(401)
     
# GETS A RANDOM COMIC BOOK  
@comics_bp.route('/<int:id>/comics/random/')
@jwt_required()
def get_random_comic(id):
    # CHECKS CORRECT USER
    check_user(id)
     # USES FUN RANDOM TO SELECT A RANDOM COMIC ID
    stmt = db.select(Comic).order_by(func.random()).limit(1).filter_by(user_id=id)
    comics = db.session.scalars(stmt)
        
    return ComicSchema(many=True).dump(comics) 
   