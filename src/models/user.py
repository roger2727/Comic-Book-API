
from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length

class User(db.Model):
    __tablename__ = 'users'
    # USER FIELDS
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String,nullable=False)
    last_name = db.Column(db.String,nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String,nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    # TABLE RELATIONS
    comics = db.relationship('Comic', back_populates='user', cascade='all, delete')
    review= db.relationship('Review', back_populates='user', cascade='all, delete')


class UserSchema(ma.Schema):
    # GETS COMIC AND REVIEW FIELDS
    comics = fields.List(fields.Nested('ComicSchema', exclude=['user']))
 
    
    #   PASSWORD BIGGER THAN 8 CHARACTERS
    password = fields.String(required=True, validate=
        Length(min=8, error='Password must be at least 8 characters long'),
        
    )
     
     
    class Meta:
        # FIELDS TO DISPLAY
        fields = ('id','user','first_name','last_name','email', 'password', 'is_admin')
        ordered = True
