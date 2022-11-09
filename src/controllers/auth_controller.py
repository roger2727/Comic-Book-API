from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import timedelta
from models.user import User, UserSchema
from flask_jwt_extended import create_access_token, get_jwt_identity


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# REGISTER NEW USER ACCOUNT
@auth_bp.route('/register/', methods=['POST'])
def auth_register():
    data = UserSchema().load(request.json)
    try:
       
        user = User(
            first_name = request.json['first_name'],
            last_name = request.json['last_name'],
            email = request.json['email'],
            password = bcrypt.generate_password_hash(request.json['password']).decode('utf8'),
            
        )
        
        db.session.add(user)
        db.session.commit()
        
        return UserSchema(exclude=['password']).dump(user), 201
    except Exception:
        return {'error': 'Email address already in use'}, 409
    

# LOGIN USER ACCOUNT
@auth_bp.route('/login/', methods=['POST'])
def auth_login():
    #  query email to make sure email is not in use
    stmt = db.select(User).filter_by(email=request.json['email'])
    user = db.session.scalar(stmt)
    
    # CHECKS USER EXIST & PASSWORD IS A MATCH
    if user and bcrypt.check_password_hash(user.password, request.json['password']):
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        return {'email': user.email, 'token': token, 'is_admin': user.is_admin}
    else:
        return {'error': 'Invalid email or password'}, 401
    
# CHECKS IF ADMIN
def authorize():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        abort(401)
        
# CHECKS CORRECT USER AND NOT ADMIN
def check_user(id):
    user_id = get_jwt_identity()  
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if id != int(user_id):
        abort(401)
   
   
   