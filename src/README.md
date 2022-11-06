<br>
<br>

# **Comic Book Managment System API**

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)![Visual Studio](https://img.shields.io/badge/Visual%20Studio-5C2D91.svg?style=for-the-badge&logo=visual-studio&logoColor=white)![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

![Example screenshot](/docs/banner.png)

Link to Github repo [_click here_](http).

link to Trello Implementation plan [_click here_](http).
<br>
<br>

## Table of Contents

- [General Info](#the-purpose-for-building-this-app)
- [Database info](#database-system-used-for-this-project-and-why)
- [Entity Relationship Diagram](#erd)
- [End Points](#api-endpoints)
- [Implementation Plan](#implementation-plan)
- [Tech Stack](#tech-stack)
- [Reference](#reference)

<br>

# **The purpose for building this app**

<!-- R1 Identification of the problem you are trying to solve by building this particular app. -->
<!-- R2 Why is it a problem that needs solving? -->

I own a lot of comic books, and I can never remember what I have. I hate flicking through piles to see which ones I have because they get damaged, are messy, and can waste a lot of time. So if I have an app with a list that I can go through, it will save a lot of time and prevent my comics from getting damaged. Also, sometimes I need help deciding which one to read because I could spend hrs deciding. The app will generate a random comic book which will solve this problem. As a collector of comic books, I always wonder how much all my comics are worth, so the app will tell me how many comics I have and what they are worth to keep track of my investments.

<br>
<br>

# **Database system used for this project and why?**

<br>

<!-- R3 Why have you chosen this database system. What are the drawbacks compared to others? -->

For this project, I have chosen to use PostgreSQL.I have chosen Psql because it is an object-relational database management system (ORDBMS), .which means it has all the features of a Relational Database Management system and uses object-oriented management systems like inheritance, objects and classes. Another reason I have chosen Psql is that it has been Acid compliant since 2001, which means the database will guarantee validity even with power outages or errors etc. some of the drawbacks of using Psql is its slow performance if you are to compare it to Mysql. Another drawback if comparing Postgresql to Mysql because Postgresql is more advanced and has a lot more features, it requires a higher learning curve.

<br>
<br>

<!-- R9 Discuss the database relations to be implemented in your application -->
<!-- R4 Identify and discuss the key functionalities and benefits of an ORM -->

# **functionalities and benefits of an ORM**

<br>

The main functionalities of a Relational object Database (Orm) are to map relational SQL objects, and you have foreign and primary keys to actual objects and code so you can more easily both read, view and respond in objects and also manipulate them so you can set properties and make changes. The ORM is great as you won't need to rely on special technics or learn a new query language to be productive with the data system. another benefit of using relational object mapping is that the models are dry because you only write the models once, which makes it faster and easier to update and maintain.

<br>

<!-- R8 Describe your projects models in terms of the relationships they have with each other -->

<br>
<br>

# **ERD**

<!-- R6 An ERD for your app -->

![Example screenshot](/docs/erd.png)

<br>
<br>

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
| GET        | /auth/users/1/  | shows all user's        | [Response](#end-point-shows-all-users)         |
| POST       | /auth/register/ | Register a new user     | [Response](#register-a-new-user)               |
| POST       | /uath/login/    | login into user account | [Response](#end-point-login-into-user-account) |

<br>
<br>

### End point: shows all user's

```json
// ONLY ADMIN HAS ACCES TO INFORMATION
[
  {
    "id": 1,
    "first_name": "Stan",
    "last_name": "Lee",
    "email": "admin@gmail.com",
    "is_admin": true
  },
  {
    "id": 2,
    "first_name": "Mitchell",
    "last_name": "Roger",
    "email": "roger@gmail.com",
    "is_admin": false
  }
]

// IF NOT ADMIN
{
    "error": "You are not authorized to perform this action"
}
```

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

| HTTP   | Endpoints               | Action                    | Respose                                |
| ------ | ----------------------- | ------------------------- | -------------------------------------- |
| GET    | /comics/                | shows all comic books     | [Response](#shows-all-comic-books)     |
| GET    | /comics/int:id/         | shows user's comic books  | [Response](#register-a-new-user)       |
| GET    | /comics/search/comic_id | get comic by comic id     | [Response](#get-comic-by-comic-id)     |
| GET    | /comics//int:id/total/  | get total value of comics | [Response](#get-total-value-of-comics) |
| GET    | /comics/int:id/random/  | get random comic          | [Response](#get-random-comic)          |
| POST   | /comics/int:id/add/     | add comic book            | [Response](#add-comic-book)            |
| PATCH  | /comics/update/int:id/  | Update fields             | [Response](#Update-fields)             |
| DELETE | /comics/remove/int:id/  | delete's comic book       | [Response](#end-point-login-i)         |

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
// IF CORRECT FIELDS
{
  "message": "Comicbook Batman vol 2 successfully added to libary"
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
  "review": "fucking",
  "rating": 1,
  "date": "2022-11-06"
}
// IF NO MATCH WITH ID
{
    "error": "Review  not found with the id: 6"
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

Before developing this application, I began with the planning process by creating a new Trello board and adding a card for every task with checklists required to finish each task. Once I have made all the cards, I go back through them and decide what has to be completed first and what has more priority. Then I start adding time frames and dates to the cards. Doing this allows me to look at the project and see how much time I can spend on specific tasks and helps me keep track of the overall progress of the development of the application

<br>
<br>

link to Trello Implementation plan [_click here_](https://trello.com/invite/b/kgYlNK2u/ATTI23e01016826faea78b7ed251a0eb5af36A99C357/comic-book-api-project).

![Example screenshot](/docs/trello.png)

<br>
<br>

<!-- R7 Detail any third party services that your app will use -->

## **How to run**

<br>

nbvcnvcnvnnnbcvnncvbnnb

<br>

1. Create a Virtual Environment
   - type in the terminal `python3 -m venv venv`
   - type in the terminal `. venv/bin/activate`
   - Installation instructions: https://docs.python.org/3/library/venv.html
2. In your terminal, go to the directory containing the application
3. To execute run.sh file by entering: `./run.sh`

<br>
<br>

# **Tech Stack**

- **Python** - a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn’t specialized for any specific problems

- **PostgreSQL** - open source object-relational database system that uses the SQL language combined with many features that safely store and scale the most complicated data workloads

- **Flask** - Flask is a web framework, which provides you with tools, libraries and technologies that allow you to build a web application.

- **SQlAlchemy** - SQLAlchemy is a popular SQL toolkit and Object Relational Mapper. It is written in Python and gives full power and flexibility of SQL to an application developer

- **Marshmallow** - Marshmallow is a Python library that converts complex data types to and from Python data types. It is a powerful tool for both validating and converting data.

- **Psycopg2** - Psycopg2 is a PostgreSQL database driver, it is used to perform operations on PostgreSQL using python

- **JWT** - or JSON Web Token, is an open standard used to share security information between two parties

- **Bcrypt** - BCrypt Algorithm is used to hash and salt passwords securely

<br>

# **Reference**

<br>

Refrence for PEP8 style guidelines
