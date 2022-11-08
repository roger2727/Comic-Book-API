from init import db, ma
from marshmallow import fields

class Review(db.Model):
    __tablename__ = 'reviews'
    # REVIEW FIELDS
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    date = db.Column(db.Date)
    # FOREIGN_KEYS
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comic_id = db.Column(db.Integer, db.ForeignKey('comics.id'), nullable=False,unique=True)
    # TABLE RELATIONS
    user = db.relationship("User", back_populates="review" )
    comic = db.relationship("Comic", back_populates="review")


class ReviewSchema(ma.Schema):
    # NEST COMIC FIELDS
    comic = fields.Nested('ComicSchema',only=['title'])

    

    class Meta:
        # FIELDS DISPLAY
        fields = ('comic','id', 'review','rating', 'date')
        ordered = True
