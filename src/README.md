# **Comic Book Management System API**

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)![Visual Studio](https://img.shields.io/badge/Visual%20Studio-5C2D91.svg?style=for-the-badge&logo=visual-studio&logoColor=white)![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Froger2727%2FT2A2---API-Webserver-Project&count_bg=%23C83D55&title_bg=%23555555&icon=&icon_color=%23EC0000&title=visits&edge_flat=true)

![Example screenshot](/docs/banner.png)

Link to Github repo [_click here_](https://github.com/roger2727/T2A2---API-Webserver-Project).

link to Trello Implementation plan [_click here_](https://trello.com/invite/b/kgYlNK2u/ATTI23e01016826faea78b7ed251a0eb5af36A99C357/comic-book-api-project).
<br>

# Table of Contents

- [General Info](#the-purpose-for-building-this-api)
- [Database Info](#database-system-used-for-this-project-and-why)
- [ERD Relations & Models Info](#erd-relations--models-info)
- [End Points](#api-endpoints)
- [Implementation Plan](#implementation-plan)
- [Tech Stack/ Dependencies](#tech-stack--dependencies)

<br>

# **The purpose for building this API**

<!-- R1 Identification of the problem you are trying to solve by building this particular app. -->
<!-- R2 Why is it a problem that needs solving? -->

I own a lot of comic books, and I hate flicking through piles to see which ones I have because they get damaged, and it gets messy. Usually, by the time I have gone through the entire stack, I forget which one's I wanted to read. This process of deciding what to read can waste a lot of time, So if I had an app to store all my comic books and give me the option to pick a random comic book, it would save a lot of time and prevent my comics from getting damaged. i want a place were i can store a review on a comic book and give it a rating to give me more information when browsing through.This will help me to keep track of the the comic books that i enjoyed reading the most. As a collector of comic books, I always wonder how many comics I own and how much all my comics are worth, so if I had an app to store all this information, it would help me keep track of my comic book investments.

<br>
<br>

# **Database system used for this project and why?**

<br>

<!-- R3 Why have you chosen this database system. What are the drawbacks compared to others? -->

For this project, I have chosen to use PostgreSQL.I have chosen Psql because it is an object-relational database management system (ORDBMS). which means it has all the features of a Relational Database Management system but also uses object-oriented management systems like inheritance, objects and classes. Another reason I have chosen Psql is that it has been Acid compliant since 2001, which means the database will guarantee validity even with power outages or errors.Another great feature is PostgreSQL has ROLES and legacy roles for setting and maintaining permissions for the database

**drawbacks**

Compared to MySQL, PostgreSQL lacks on the performance side of things, and Postgresql is more advanced and has many more features, requiring a higher learning curve.Another drawback is there is No caching for Query execution plans,which means when the sever runs again the sql server need to create another query plan which can hinder database perfomance

<br>
<br>

<!-- R9 Discuss the database relations to be implemented in your application -->
<!-- R4 Identify and discuss the key functionalities and benefits of an ORM -->

# **functionalities and benefits of an ORM**

<br>

## **functionalities of an ORM**

- Object Relational Mapper or (ORM) for short, is designed to translate between the data used by databases and those used in object-oriented programming. An ORM lets you work with the backend data using object-oriented structures like inheritance, objects and classes to performe operations like creating, reading, updating, and deleting data from a database.

**example**: Using ORM to create a class which will map to each field in the database

```python
# creates class
class Comic(db.Model):
  # table name
  __tablename__ = 'comics'
  # feilds for table
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100),nullable=False)
  author = db.Column(db.String(100))
  comic_value = db.Column(db.Float)
  user_id = db.Column(db.Integer,
  db.ForeignKey('users.id'), nullable=False)
```

**example**: what is created in the psql database

```Psql
comicbook=# \d comics
 id          | integer                |           | not null | nextval('comics_id_seq'::regclass)
 title       | character varying(100) |           | not null |
 author      | character varying(100) |           |          |
 comic_value | double precision       |           |          |
 user_id     | integer                |           | not null |

```

**Example**:using ORM to create a new instance of a comic class which will be mapped and become another record in the table

```python
comic = Comic(
              title = data['title'],
              author = data['author'],
              comic_value = data['comic_value'],
              user_id = get_jwt_identity()
              )

               db.session.add(comic)
               db.session.commit()

```

**example**: query using OOP

```python
  stmt = db.select(Comic).order_by(Comic.title.desc())
  comics = db.session.scalars(stmt)
  return ComicSchema(many=True).dump(comics)
```

## **benefits of an ORM**

- Using an ORM helps prevent SQL injection attacks which helps with security threats
- models are dry because you only write the models once, making it faster and easier to update and maintain.
- ORM is great as you won't need to rely on special technics or learn a new query language to be productive with the data system
- ORM is available in the language of your choice, and lets you use OOPs
- most ORM have come with features , such as support for transactions, connection pooling, migrations, seeds, streams,
  <br>

<!-- R8 Describe your projects models in terms of the relationships they have with each other -->

<br>
<br>

# **ERD Relations & Models Info**

<!-- R6 An ERD for your app -->

![Example screenshot](/docs/erd.png)
<br>
<br>

# Database Realatships

The ERD above shows The user's entity has a one-to-many relationship to the comics entity because the user can store multiple comic books and is linked by the foreign key user_id, and is also linked to the reviews table. The reason for the user tables linking to the comics table is so a user id can be assigned to a comic book to allow for the user to have multiple comics in their library. The user table is linked to the reviews table so that the review is assigned with the user id so it can be checked if the user has already entered a review for the comic book. The user has many reviews, so it is a one-to-many. The comics entity has a one-to-one relationship with the reviews entity because each comic book has one personal review by the user. They are linked by the foreign key comic_id in the reviews entity. The reason for the comics table linking to the reviews table is so the comic id is a assigned to the review so the review can show the details of the comic with review information.
<br>
<br>

# Methods and behaviours of the models

## Users model

In the users model, you have an id field which is the primary key of the user. It is an integer and is used as an identifier of each user. Then you have first_name and last_name, which are both strings and are set to nullable=True, which means that the user must enter the first and last name and can not be empty. The field email is also a string and set so it can't be empty, but it is also set to unique=True, which means that the email address can not be duplicated. Next is the password field, which is a string and can not be empty. It also needs to be at least eight characters. The field is_admin is a boolean which is set to default=false, which means every time a user is created, the is_admin field is set to false.

**example of users model:**

```python
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
```

<hr>

<br>
<br>

## Comics model

In the comics model, you have an id field which is the primary key of the comic. It is an integer and is used as an identifier of each comic book. The title field is a string and has a constraint of 100 characters. It can not be empty because the title will be used to make sure that it is not duplicated in the user's library. The title also needs to be more than two characters than you have the author, which is a string with a max of 100 characters and can be empty as it's not needed. Then, you have the comic_value set as a float to display the value in the correct format. user_id field is an Integer and is a foreign key, so it can link to the user's table and use the information from the user table to assign it to the comic book.

**example of comics model:**

```python
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
    user = fields.Nested('UserSchema', only=['first_name','last_name', 'email'])
    #  NEST REVIEW FIELDS
    review = fields.List(fields.Nested('ReviewSchema', exclude=['comic']))
    #  VALADATES TITLE
    title = fields.String(required=True, validate=
        Length(min=2, error='Title must be at least 2 characters long')
    )
    class Meta:
        # FIELDS TO DISPLAY
        fields = ('id', 'title','author', 'comic_value',  'review',"user")
        ordered = True
```

<hr>

<br>
<br>

## reviews model

The following example shows the reviews model that has the field id, which is an Integer and is a primary key that acts as an identifier of each review. The field review is a string and has a constraint of 200 characters. The rating field is an integer, and the input can only be between 1 and 10. then you have the date field, which will save the date when a review is done on a comic book. user_id is an Integer and is a foreign key that links to the user to grab the user id and assign it to the review. Than you have the comic_id, which is also an integer and is a foreign key to assign the comic id to the review

**example of review model:**

```python
  class Review(db.Model):
    __tablename__ = 'reviews'
    # REVIEW FIELDS
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(200))
    rating = db.Column(db.Integer,nullable=False)
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
```

<br>
<br>

# API Endpoints

<br>

**Table of Contents**

- [User Endpoints](#user-end-points)
- [Comic Book Endpoints](#comic-book-endpoints)
- [Review Endpoints](#reviews-endpoints)

<br>
<br>

# User end points

| HTTP Verbs | Endpoints       | Action                  | Respose                                        |
| ---------- | --------------- | ----------------------- | ---------------------------------------------- |
| POST       | /auth/register/ | Register a new user     | [Response](#register-a-new-user)               |
| POST       | /uath/login/    | login into user account | [Response](#end-point-login-into-user-account) |

<br>
<br>

### Register a new user

```json
// IF USER ENTERS ALL FIELDS CORECTLY USER IS CREATED
{
    "id": 5,
    "first_name": "matt",
    "last_name": "dre",
    "email": "mat@gmail.com",
    "is_admin": false
}
// IF EMAIL ALREADY EXISTS
{
    "error": "Email address already in use"
}
// first_name NOT ENTERED
{
    "error": "The field 'first_name' is required."
}
// LAST_NAME NOT ENTERED
{
  "error": "The field 'last_name' is required."
}
// EMAIL NOT ENTERED
{
    "error": "The field 'email' is required."
}
// password NOT ENTERED
{
    "error": "The field 'password' is required."
}
// PASSWORD TO SHORT
{
    "error": {
        "password": [
            "Password must be at least 8 characters long"
        ]
    }
}
```

### End point: login into user account

```json
// SUCCESFUL LOIGN
{
  "email": "roger@gmail.com",
  "token": "jwt-token is displayed to copy into authorization",
  "is_admin": false
}
// NOT SUCCESFUL LOIGN
{
    "error": "Invalid email or password"
}
```

<br>
<br>

# Comic Book Endpoints

<br>

| HTTP   | Endpoints                                | Action                    | Respose                                |
| ------ | ---------------------------------------- | ------------------------- | -------------------------------------- |
| GET    | /users/comics/                           | shows all comic books     | [Response](#shows-all-comic-books)     |
| GET    | /users/int:id/comics                     | shows user's comic books  | [Response](#register-a-new-user)       |
| GET    | /users/int:id/comics/search/int:comic_id | get comic by comic id     | [Response](#get-comic-by-comic-id)     |
| GET    | /users/int:id/comics/total/              | get total value of comics | [Response](#get-total-value-of-comics) |
| GET    | /users/int:id/comics/random/             | get random comic          | [Response](#get-random-comic)          |
| POST   | /users/int:id/add/                       | add comic book            | [Response](#add-comic-book)            |
| PATCH  | /users/int:id/comics/int:comic_id/       | Update fields             | [Response](#update-fields)             |
| DELETE | /users/comics/remove/int:comic_id/       | delete's comic book       | [Response](#deletes-comic-book)        |

<br>
<br>

### shows all comic books

```json
[
    {
        "id": 2,
        "title": "superman vol 2",
        "author": "super man duide",
        "comic_value": 100.0,
        "review": [
            {
                "id": 2,
                "review": "it was not good",
                "rating": 1,
                "date": "2022-11-06"
            }
        ]
    },
```

### shows user's comic books

```json
// IF CORRECT USER
[
  {
    "id": 2,
    "title": "superman vol 2",
    "author": "super man duide",
    "comic_value": 100.0,
    "review": [
      {
        "id": 2,
        "review": "crap",
        "rating": 1,
        "date": "2022-11-06"
      }
    ]
  }
]
// IF NOT THE CORRECT USER
{
    "error": "You are not authorized to perform this action"
}
```

### get comic by comic id

```json
// IF FINDS A MATCH
[
  {
    "id": 2,
    "title": "superman vol 2",
    "author": "super man duide",
    "comic_value": 100.0,
    "review": [
      {
        "id": 2,
        "review": "crap",
        "rating": 1,
        "date": "2022-11-06"
      }
    ]
  }
]
// IF ID HAS NO MATCH
{
    "error": "Comicbook not found with the id: 1"
}
```

### get total value of comics

```json
// IF CORRECT USER
{
  "message": "You have a total of 50 comicbooks, the total value comes to:  $1000 "
}
// IF NOT THE CORRECT USER
{
    "error": "Invalid user"
}
```

### Get random comic

```json
// IF CORRECT USER
[
  {
    "id": 2,
    "title": "superman vol 2",
    "author": "super man duide",
    "comic_value": 100.0,
    "review": [
      {
        "id": 2,
        "review": "poo",
        "rating": 1,
        "date": "2022-11-06"
      }
    ]
  }
]
// IF NOT CORRECT USER
{
    "error": "You are not authorized to perform this action"
}
```

### Add comic book

```json
// IF CORRECT FIELDS ADDED AND CORRECT USER
{
  "message": "Comicbook Batman vol 2 successfully added to libary"
}
// IF CORRECT FIELDS ADDED AND INCORRECT USER
{
    "error": "You are not authorized to perform this action"
}
// IF TITLE LESS THEN 2 CARACHTERS
{
    "error": {
        "title": [
            "Title must be at least 2 characters long"
        ]
    }
}
// ID TITLE ALREADY EXISTS
{
    "error": "Comicbook Batman vol 2 already exists for user"
}

//IF NO VALUE ADDED
{
    "error": "The field 'comic_value' is required."
}
// IF NO AUTHOR ADDED
{
    "error": "The field 'author' is required."
}
```

### Update fields

```json
//  IF COMIC BOOK ID IS FOUND
{
  "id": 2,
  "title": "batman update",
  "author": "ytinkle",
  "comic_value": 5000.0,
  "review": [
    {
      "id": 2,
      "review": "great",
      "rating": 9,
      "date": "2022-11-06"
    }
  ]
}
//  IF ID NOT FOUND
{
    "error": "Comicbook not found with the id: 6"
}
```

### Delete's comic book

```json
//  IF COMIC ID MATCHED AND CORRECT USER
{
  "message": "Comic book'BATMAN VOL2  deleted successfully"
}
// IF INCORRECT USER
{
    "error": "You are not authorized to perform this action"
}
//  COMIC BOOK ID NOT FOUND
{
    "error": "comicbook not found with the id 1"
}
```

<br>
<br>

# reviews endpoints

| HTTP Verbs | Endpoints                         | Action               | Respose                           |
| ---------- | --------------------------------- | -------------------- | --------------------------------- |
| GET        | /comics/review/all/int:id/        | shows all reviews    | [Response](#shows-all-reviews)    |
| GET        | /comics/review/search/int:id/     | Search for review id | [Response](#search-for-review)    |
| POST       | /comics/review/add/int:comic_id>/ | Adds review to comic | [Response](#adds-review-to-comic) |

<br>
<br>

### shows all reviews

```json
// SHOWS ALL USERS REVIEWS  WITH TITLE OF COMIC
[
  {
    "comic": {
      "title": "superman vol 1"
    },
    "id": 1,
    "review": "best comic i have ever seen",
    "rating": 1,
    "date": "2022-11-06"
  }
]
// IF NOT USER

{
    "error": "You are not authorized to perform this action"
}
```

### Search for review

```json
// IF ID IS A MATCH
{
  "comic": {
    "title": "superman vol 1"
  },
  "id": 1,
  "review": "CRAP",
  "rating": 1,
  "date": "2022-11-06"
}
// IF NO MATCH WITH ID
{
    "error": "Review  not found with the id: 6"
}
// IF RATING IN NOT BETWEEN 1 AND 10
{
    "error": "rating needs to between 1 and 10 "
}
```

### Adds review to comic

```json
//   IF COMIC BOOK ID IS FOUND
{
    "comic": {
        "title": "Batman vol 2"
    },
    "id": 7,
    "review": "yeah was foo",
    "rating": 12345,
    "date": "2022-11-06"
}

//  IF USER ALREADY HAVE A REVIEW ON TITLE
{
  "error": "User can not have multiple reviews on one comicbook, please edit the original review ."
}
```

<br>
<br>

# **Implementation plan**

<!-- R10 Describe the way tasks are allocated and tracked in your project -->

Before developing this application, I began with the planning process by creating a new Trello board and adding a card for every task with checklists required to finish each task. Once I have made all the cards, I will go through and highlight what is code and what is documentation, and then I will decide what has to be completed first and what has more priority. After that is done, I start adding time frames and dates to the cards. Doing this allows me to keep track of the overall progress of the development of the application.

<br>
<br>

link to Trello Implementation plan [_click here_](https://trello.com/invite/b/kgYlNK2u/ATTI23e01016826faea78b7ed251a0eb5af36A99C357/comic-book-api-project).

![Example screenshot](/docs/trello.png)
![Example screenshot](/docs/trello_check.png)

<br>
<br>

<!-- R7 Detail any third party services that your app will use -->

# Tech Stack & Dependencies

- **Python**

  a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn’t specialized for any specific problems. for more information visit [_https://www.python.org/_](https://www.python.org/).

- **PostgreSQL**

  open source object-relational database system that uses the SQL language combined with many features that safely store and scale the most complicated data workloads. for more information visit [_https://www.postgresql.org/_](https://www.postgresql.org/).

- **Flask**

  Flask is a web framework, which provides you with tools, libraries and technologies that allow you to build a web application.for more information visit [_https://palletsprojects.com/p/flask/_](https://palletsprojects.com/p/flask/).

- **SQlAlchemy**

  SQLAlchemy is a popular SQL toolkit and Object Relational Mapper. It is written in Python and gives full power and flexibility of SQL to an application developer.for more information visit [_https://www.sqlalchemy.org/_](https://www.sqlalchemy.org/).

- **Marshmallow**

  Marshmallow is a Python library that converts complex data types to and from Python data types. It is a powerful tool for both validating and converting data.for more information visit [_https://marshmallow.readthedocs.io/en/stable/_](https://marshmallow.readthedocs.io/en/stable/).

- **Psycopg2**

  - Psycopg2 is a PostgreSQL database driver, it is used to perform operations on PostgreSQL using python, it is designed for multi-threaded applications. SQL queries are executed with psycopg2 with the help of the execute() method. It is used to Execute a database operation query or command.
  - for more info visit [_https://www.psycopg.org/docs/_](https://www.psycopg.org/docs/)

- **JWT**

  or JSON Web Token, is an open standard used to share security information between two parties.

  **features JWT**

  - Because the JWT is comprised of encoded JavaScript Object Notation (JSON) objects, it is compact enough to be sent through a URL query, a POST parameter, or an HTTP header.

  - The JWT can contain all the required information about the user and therefore avoids querying the database more than once

  - The JWT can be digitally signed with HMAC algorithm or RSA algorithm, using a public/private key pair

  - for more information visit [_https://jwt.io/_](https://jwt.io/)

- **Flask-Bcrypt**

  Flask-Bcrypt Algorithm is used to hash and salt passwords securely.

  **features of Bcrypt**

  - Bcrypt is a one-way hash function to obfuscate the password such that it is not stored in plain text.

  - The hashing function is executed many times which is known as key stretching.

  - BCrypt stores the number of iterations as part of the hash

  - for more information visit [_https://flask-bcrypt.readthedocs.io/en/1.0.1/_](https://flask-bcrypt.readthedocs.io/en/1.0.1/)

- **python-dotenv**

  python-dotenv allows you load the configuration from a .env file which helps in the development of apps following the 12-factor principles .for more information visit [https://pypi.org/project/python-dotenv/](https://pypi.org/project/python-dotenv/)

<br>
