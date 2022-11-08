from flask import Blueprint
from init import db, bcrypt
from datetime import date
from models.comic import Comic
from models.user import User
from models.review import Review


db_commands = Blueprint('db', __name__)

# CREATE TABLES
@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created successfully")
    
# DROPS TABLES
@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped successfully")
    
# SEEDS DATABASE
@db_commands.cli.command('seed')
def seed_db():
 # USERS ACCOUNTS DATA
    users = [
        User(
            first_name='Stan',
            last_name='Lee',
            email='admin@gmail.com',
            password=bcrypt.generate_password_hash('admin').decode('utf-8'),
            is_admin=True
        ),
        User(
            first_name='Mitchell',
            last_name='Roger',
            email='roger@gmail.com',
            password=bcrypt.generate_password_hash('12345').decode('utf-8')
        ),
         User(
            first_name='Charles',
            last_name='Xavier',
            email='mutant@gmail.com',
            password=bcrypt.generate_password_hash('12345').decode('utf-8')
        ),    
        
    ]

    db.session.add_all(users)
    db.session.commit()
    
# COMICBOOKS DATA
    comics = [
        Comic(
            title = 'superman vol 1',
            author = 'super man duide',
            comic_value = 97.50,
            user = users[0]
        ),
        Comic(
            title = 'superman vol 2',
            author = 'super man duide',
            comic_value = 100.00, 
            user = users[1]
        )]

    db.session.add_all(comics)
    db.session.commit()
    
# USER REVIEWS DATA
    user_review = [
        Review(
            review = 'fucking',
            rating = 1,
            user = users[1],
            comic= comics[0],
            date = date.today()
        ),
        Review(
            review = 'poo',
            rating = 1,
            user = users[0],
            comic= comics[1],
            date = date.today()
        
         )
    
    ]

    db.session.add_all(user_review)
    db.session.commit()

    print('Tables seeded successfully')
