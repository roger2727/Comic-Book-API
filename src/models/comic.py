from init import db, ma
from marshmallow import fields
class Comic(db.Model):
    __tablename__ = 'comics'

    id =db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    release = db.Column(db.Date) 
    price = db.Column(db.Float)
    genre = db.Column(db.String)
    author = db.Column(db.String)
    
class ComicSchema(ma.Schema): 
    class Meta:
        fields = ('id', 'title', 'release', 'price', 'genre', 'author')
        ordered =True    