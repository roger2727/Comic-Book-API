from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp



class Comic(db.Model):
    __tablename__ = 'comics'
    # COMIC FIELDS
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    author = db.Column(db.String(100))
    comic_value = db.Column(db.Float)
    # FOREIGN_KEY
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # TABLE RELATIONS
    user = db.relationship('User', back_populates='comics')
    review = db.relationship('Review', back_populates='comic', cascade='all, delete')


class ComicSchema(ma.Schema):
    #  NEST REVIEW FIELDS
    review = fields.List(fields.Nested('ReviewSchema', exclude=['comic']))
    #  VALADATES TITLE 
    title = fields.String(required=True, validate=
        Length(min=2, error='Title must be at least 2 characters long')
    )

    
    class Meta:
        # FIELDS TO DISPLAY
        fields = ('id', 'title','author', 'comic_value',  'review')
        ordered = True
