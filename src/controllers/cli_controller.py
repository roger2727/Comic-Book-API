from flask import Blueprint
from init import db,bcrypt
from models.user import User
from models.comic import Comic 
from datetime import date



db_commands = Blueprint('db', __name__)

# creates database tables
@db_commands.cli.command('create')
def create_db():
    
    db.create_all()
    print("Tables created")
    
# deletes database tables
@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped") 
    
       
# seeds the data into tables
@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            email='admin@test.com',
            password=bcrypt.generate_password_hash('deadpool').decode('utf-8'),
            is_admin=True,
            first_name = 'mitchell',
            last_name = 'roger'
        ),
        User(
           email='test@test.com',
            password=bcrypt.generate_password_hash('test').decode('utf-8'),
            is_admin=False,
            first_name = 'joe',
            last_name = 'blow')
    ]

    db.session.add_all(users)
    db.session.commit()

    comics = [
        Comic(
            title = "Superman",
            release= date.today(),
            price = 10.99,
            genre = "DC",
            author = "dont know yet"
        ),
        Comic(
            title = "batman",
            release= date.today(),
            price = 10.99,
            genre = "DC",
            author = "dont know yet"
        ),
        Comic(
            title = "deadpool",
            release= date.today(),
            price = 10.99,
            genre = "DC",
            author = "dont know yet"
        ),
        Comic(
            title = "x-men",
            release= date.today(),
            price = 10.99,
            genre = "DC",
            author = "dont know yet"
        )
    ]

    db.session.add_all(comics)
    db.session.commit()
