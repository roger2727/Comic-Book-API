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
        # admin comics
        Comic(
            title = 'superman vol 1',
            author = 'Jerry Siegel',
            comic_value = 97.50,
            user = users[0]
        ),
        Comic(
            title = 'superman vol 2',
            author = 'Jerry Siegel ',
            comic_value = 100.00, 
            user = users[0]
        ),
        Comic(
            title = 'superman vol 3',
            author = 'Jerry Siegel ',
            comic_value = 30.00, 
            user = users[0]),
        
        # mitchell roger's comic
        Comic(
            title = 'Batman vol 2',
            author = 'Bob Kane',
            comic_value = 20.00, 
            user = users[1]
        ),
        Comic(
            title = 'Batman vol 3',
            author = 'Bob Kane',
            comic_value = 10.00, 
            user = users[1]),
        Comic(
            title = 'Batman vol 5',
            author = 'Bob Kane',
            comic_value = 100.00, 
            user = users[1]
        ),
        # Charles Xavier's comics
        Comic(
            title = 'Xmen vol 1',
            author = 'Stan Lee',
            comic_value = 100.00, 
            user = users[2]),
        Comic(
            title = 'Xmen vol 12',
            author = 'Stan Lee',
            comic_value = 100.00, 
            user = users[2]
        ),
        Comic(
            title = 'Xmen vol 9',
            author = 'Stan Lee',
            comic_value = 100.00, 
            user = users[2])
        ]

    db.session.add_all(comics)
    db.session.commit()
    
# USER REVIEWS DATA
    user_review = [
        Review(
            review = 'a great read one of my favourite comics',
            rating = 9,
            user = users[0],
            comic= comics[3],
            date = date.today()
        ),
        Review(
            review = 'was boring not a fan',
            rating = 1,
            user = users[1],
            comic= comics[6],
            date = date.today()
        
         )
    
    ]

    db.session.add_all(user_review)
    db.session.commit()

    print('Tables seeded successfully')
