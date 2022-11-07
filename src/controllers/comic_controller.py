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

comics_bp = Blueprint('comics', __name__, url_prefix='/comics')

# GETS ALL COMIC BOOKS FROM ALL USERS
@comics_bp.route('/')
@jwt_required()
def get_all_comics():
    stmt = db.select(Comic).order_by(Comic.title.desc())
    comics = db.session.scalars(stmt)
    return ComicSchema(many=True).dump(comics)

# GETS ALL COMIC BOOKS FROM USER ACCOUNT
@comics_bp.route('/<int:id>/')
@jwt_required()
def get_user_comics(id):
    # CHECKS CORRECT USER ACCOUNT
    check_user(id)
    stmto = db.select(Comic).filter_by(user_id=id)
    comics = db.session.scalars(stmto)

    return ComicSchema(many=True).dump(comics)
  
# GETS COMIC BOOK BY COMICBOOK ID
@comics_bp.route('/search/<int:comic_id>/')
@jwt_required()
def search_by_id(comic_id):
    user_id = get_jwt_identity()  
    stmt = db.select(Comic).filter_by(id=comic_id).filter_by(user_id=user_id)
    comic = db.session.scalar(stmt)
    
    if not comic or not user_id:
        return {'error': f'Comicbook not found with the id: {comic_id}' },404
   
    else:
        
        return ComicSchema().dump(comic)

# DELETE COMIC BOOK BY ID
@comics_bp.route('/remove/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_comic(id):
    user_id = get_jwt_identity()  
    stmt = db.select(Comic).filter_by(id=id).filter_by(user_id=user_id)
    comic = db.session.scalar(stmt)
    # CHECKS COMICBOK ID EXISTS & CHECKS CORRECT USER
    if comic and user_id:
        db.session.delete(comic)
        db.session.commit()
        return {'message': f"Comic book'{comic.title}  deleted successfully"}
    else:
        return {'error': f'comicbook not found with the id {id}'}, 404

# UPDATE COMIC BOOK
@comics_bp.route('/update/<int:id>/', methods=['PUT', 'PATCH'])
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
@comics_bp.route('<int:id>/add', methods=['POST'])

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
@comics_bp.route('/<int:id>/total/')
@jwt_required()
def get_user_total(id):
    
    user_id = get_jwt_identity()  
    stmt = db.session.query(func.count(Comic.id)).filter_by(user_id=id)
    comicso = db.session.scalar(stmt)
    stmt = db.session.query(func.sum(Comic.comic_value)).filter_by(user_id=id)
    comics = db.session.scalar(stmt)
    
    if int(user_id) == id:
        return {
            'totalComics': comicso,
            'totalValue': round(comics, 2)
        }
        # return {'message': f'You have a total of {comicso} comicbooks, the total value comes to:  ${comics} |  {type(user_id)}  | {type(id)} '}
    else:
        return {'error': f'Invalid user'}
     
 

# GETS A RANDOM COMIC BOOK  
@comics_bp.route('/<int:id>/random/')
@jwt_required()
def get_random_comic(id):
    
    check_user(id)
    stmt = db.select(Comic).order_by(func.random()).limit(1).filter_by(user_id=id)
    comics = db.session.scalars(stmt)
        
    return ComicSchema(many=True).dump(comics) 
   