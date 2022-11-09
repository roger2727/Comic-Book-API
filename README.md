# **Comic Book Management System API**

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)![Visual Studio](https://img.shields.io/badge/Visual%20Studio-5C2D91.svg?style=for-the-badge&logo=visual-studio&logoColor=white)![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

![Example screenshot](/docs/banner.png)

Link to Github repo [_click here_](http).

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

I own a lot of comic books, and I hate flicking through piles to see which ones I have because they get damaged, and it gets messy. Usually, by the time I have gone through the entire stack, I forget which one's I wanted to read. This process of deciding what to read can waste a lot of time, So if I had an app to store all my comic books and give me the option to pick a random comic book, it would save a lot of time and prevent my comics from getting damaged. As a collector of comic books, I always wonder how many comics I own and how much all my comics are worth, so if I had an app to store all this information, it would help me keep track of my comic book investments.

<br>
<br>

# **Database system used for this project and why?**

<br>

<!-- R3 Why have you chosen this database system. What are the drawbacks compared to others? -->

For this project, I have chosen to use PostgreSQL.I have chosen Psql because it is an object-relational database management system (ORDBMS), .which means it has all the features of a Relational Database Management system and uses object-oriented management systems like inheritance, objects and classes. Another reason I have chosen Psql is that it has been Acid compliant since 2001, which means the database will guarantee validity even with power outages or errors. Some of the drawbacks of using Psql is its slow performance if you are to compare it to Mysql. Another drawback if comparing Postgresql to Mysql because Postgresql is more advanced and has a lot more features, it requires a higher learning curve.

<br>
<br>

<!-- R9 Discuss the database relations to be implemented in your application -->
<!-- R4 Identify and discuss the key functionalities and benefits of an ORM -->

# **functionalities and benefits of an ORM**

<br>

## **functionalities of an ORM**

- The main functionalities of a Relational object Database (ORM) are to map relational SQL objects object oriented programming (OOP) .When working with a database using OOP languages, operations are performed like creating, reading, updating, and deleting data from a database.

**example**: Using OOP to create a table

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

## Database Realatships

The ERD above shows The user's entity has a one-to-many relationship to the comics entity because the user can store multiple comic books and is linked by the foreign key user_id, and is also linked to the reviews table. The user has many reviews, so it is a one-to-many. The comics entity has a one-to-one relationship with the reviews entity because each comic book has one personal review by the user. They are linked by the foreign key comic_id in the reviews entity.
<br>
<br>

## methods/behaviour of the models

```python
    __tablename__ = 'users'
    # id is integer and is the primary key
    id = db.Column(db.Integer, primary_key=True)
    # first_name is a string and can not be empty
    first_name = db.Column(db.String,nullable=False)
    # last_name is a string and can not be empty
    last_name = db.Column(db.String,nullable=False)
    # email is s string and is unique so users dont have same email
    email = db.Column(db.String, nullable=False, unique=True)
    # password is a string and cant be less then 8 characters
    password = db.Column(db.String,nullable=False)
    # is_admin is a boolean
    is_admin = db.Column(db.Boolean, default=False)

    # TABLE RELATIONS
    # this is were comic points to the user and review points to user table
    comics = db.relationship('Comic', back_populates='user',cascade='all, delete')
    review= db.relationship('Review', back_populates='user', cascade='all, delete')
```

<br>
<br>

```python
    __tablename__ = 'comics'
    # id is a integer and is the primary key
    id = db.Column(db.Integer, primary_key=True)
    # title is a string and has a max of 100 characters and can not be empty
    title = db.Column(db.String(100),nullable=False)
    # author is a string and has a max of 100 characters
    author = db.Column(db.String(100))
    # comic_value is a float to repersent value in dollars
    comic_value = db.Column(db.Float)
    # FOREIGN_KEY user_id us used to link to users and must not be empty
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # TABLE RELATIONS
    # this is were user point to comics and review points to the comic table
    user = db.relationship('User', back_populates='comics', cascade='all, delete')
    review = db.relationship('Review', back_populates='comic', cascade='all, delete')
```

```python
   __tablename__ = 'reviews'
    # id is a integer and is the primary key
    id = db.Column(db.Integer, primary_key=True)
    # review is a string and and the max characters is 200
    review = db.Column(db.String(200))
    # rating is a int and the max is 10
    rating = db.Column(db.Integer)
    # date is used to recored date of reviews
    date = db.Column(db.Date)
    # user_id is a foreignkey that links to users
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # comic_d is a foreignkey that links to comics id
    comic_id = db.Column(db.Integer, db.ForeignKey('comics.id'), nullable=False,unique=True)

    # TABLE RELATIONS
    # this is were user point to review and comic points to the review table
    user = db.relationship("User", back_populates="review" )
    comic = db.relationship("Comic", back_populates="review")

```

# API Endpoints

<br>

## Table of Contents

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
