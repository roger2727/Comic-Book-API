
from flask import Blueprint, request,abort
from init import db
from datetime import date
from models.comic import Comic
from models.review import ReviewSchema, Review
from controllers.auth_controller import check_user
from flask_jwt_extended import jwt_required, get_jwt_identity


from models.user import User


review_bp = Blueprint('review', __name__, url_prefix='/comics/review')

# VIEW ALL REVIEWS FROM USER ACCOUNT
@review_bp.route('/all/<int:id>')
@jwt_required()
def get_all_reviews(id):
    # CHECKS CORRECT USER
    check_user(id)
    # QUERY ALL REVIEWD FILTERS BY ID
    stmt = db.select(Review).order_by(Review.date.desc()).filter_by(user_id=id)
    reviews = db.session.scalars(stmt)
    return ReviewSchema(many=True).dump(reviews)

# SELECT REVIEW FROM REVIEW ID
@review_bp.route('/search/<int:id>/')
@jwt_required()
def search_by_id(id):
    user_id = get_jwt_identity()  
    # QUERY REVIEWS BY RERVIEW ID FILTERD BY USER ID
    stmt = db.select(Review).filter_by(id=id).filter_by(user_id=user_id)
    comic = db.session.scalar(stmt)
    
    if not comic or not user_id:
        return {'error': f'Review  not found with the id: {id}' },404
   
    else:
        
        return ReviewSchema().dump(comic)


# CREATE REVIEW FOR COMICBOOK
@review_bp.route('/add/<int:comic_id>/', methods=['POST'])
@jwt_required()
def create_review(comic_id):
    stmt = db.select(Comic).filter_by(id=comic_id)
    comic = db.session.scalar(stmt)
    try:
    
        user_review = Review(
            review = request.json['review'],
            rating = request.json['rating'],
            user_id = get_jwt_identity(),
            comic = comic,
            date = date.today()
        )
        # check user rating is between 1 and 10
        if user_review.rating <= 10 and user_review.rating >= 1:
            db.session.add(user_review)
            db.session.commit()
        
            return ReviewSchema().dump(user_review), 201  
        else:
            return {'error': f'rating needs to between 1 and 10 '}, 409  
    except Exception:   
        return {'error': f'User can not have multiple reviews on one comicbook, please edit the original review .'}, 409
        
    
        
        
    
        
    
# UPDATE REVIEW FROM REVIEW ID
@review_bp.route('/update/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_review(id):
    user_id = get_jwt_identity()  
    # SELECTS REVIEW FROM REVIEW ID AND FILTERS FROM USER ID
    stmt = db.select(Review).filter_by(id=id).filter_by(user_id=user_id)
    review = db.session.scalar(stmt)
    if review:
        review.review = request.json.get('review') or review.review
        review.rating= request.json.get('rating') or review.rating
        review.date = request.json.get('date') or review.date
        
        db.session.commit()      
        return ReviewSchema().dump(review)
    else:
        return {'error': f'Review not found with the id: {id}'}, 404




# DELETE REVIEW FROM COMIC BOOK
@review_bp.route('/remove/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_review(id):
    user_id = get_jwt_identity()  
    # REMOVE REVIEW BY SELECTING REVIEW ID FILTERS ONLY USER USERS REVIEW
    stmt = db.select(Review).filter_by(id=id).filter_by(user_id=user_id)
    review = db.session.scalar(stmt)
    if review and user_id:
        db.session.delete(review)
        db.session.commit()
        return {'message': "review deleted successfully"}
    else:
        return {'error': f'review not found with the id {id}'}, 404 
 

