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
- [End Points](#end-points-for-the-api)
- [Implementation Plan](#implementation-plan)
- [Tech Stack](#tech-stack)
- [Reference](#reference)

<br>

## **The purpose for building this app**

<!-- R1 Identification of the problem you are trying to solve by building this particular app. -->
<!-- R2 Why is it a problem that needs solving? -->

I own a lot of comic books, and I can never remember what I have. I hate flicking through piles to see which ones I have because they get damaged, are messy, and can waste a lot of time. So if I have an app with a list that I can go through, it will save a lot of time and prevent my comics from getting damaged. Also, sometimes I need help deciding which one to read because I could spend hrs deciding. The app will generate a random comic book which will solve this problem. As a collector of comic books, I always wonder how much all my comics are worth, so the app will tell me how many comics I have and what they are worth to keep track of my investments.

<br>
<br>

## **Database system used for this project and why?**

<br>

<!-- R3 Why have you chosen this database system. What are the drawbacks compared to others? -->

For this project, I have chosen to use PostgreSQL.I have chosen Psql because it is an object-relational database management system (ORDBMS), .which means it has all the features of a Relational Database Management system and uses object-oriented management systems like inheritance, objects and classes. Another reason I have chosen Psql is that it has been Acid compliant since 2001, which means the database will guarantee validity even with power outages or errors etc. some of the drawbacks of using Psql is its slow performance if you are to compare it to Mysql. Another drawback if comparing Postgresql to Mysql because Postgresql is more advanced and has a lot more features, it requires a higher learning curve.

<br>
<br>

<!-- R9 Discuss the database relations to be implemented in your application -->
<!-- R4 Identify and discuss the key functionalities and benefits of an ORM -->

## **functionalities and benefits of an ORM**

<br>

The main functionalities of a Relational object Database (Orm) are to map relational SQL objects, and you have foreign and primary keys to actual objects and code so you can more easily both read, view and respond in objects and also manipulate them so you can set properties and make changes. The ORM is great as you won't need to rely on special technics or learn a new query language to be productive with the data system. another benefit of using relational object mapping is that the models are dry because you only write the models once, which makes it faster and easier to update and maintain.

<br>

<!-- R8 Describe your projects models in terms of the relationships they have with each other -->

<br>
<br>

## **ERD**

<!-- R6 An ERD for your app -->

![Example screenshot](/docs/erd.png)

<br>
<br>

## **End points for the api**

<!-- R5 Document all endpoints for your API -->

The PEP8 style guidelines were implemented to develop this Python application.
Example of some of the guidelines (PEP 8 – Style Guide for Python Code | peps.python.org 2022)The PEP8 style guidelines were implemented to develop this Python application.
Example of some of the guidelines (PEP 8 – Style Guide for Python Code | peps.python.org 2022)

<br>
<br>

### **Implementation plan**

<!-- R10 Describe the way tasks are allocated and tracked in your project -->

Before developing this application, I began with the planning process by creating a new Trello board and adding a card for every task with checklists required to finish each task. Once I have made all the cards, I go back through them and decide what has to be completed first and what has more priority. Then I start adding time frames and dates to the cards. Doing this allows me to look at the project and see how much time I can spend on specific tasks and helps me keep track of the overall progress of the development of the application

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

## **Tech Stack**

- **Python** - a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn’t specialized for any specific problems

- **PostgreSQL** - open source object-relational database system that uses the SQL language combined with many features that safely store and scale the most complicated data workloads

- **Flask** - Flask is a web framework, which provides you with tools, libraries and technologies that allow you to build a web application.

- **SQlAlchemy** - SQLAlchemy is a popular SQL toolkit and Object Relational Mapper. It is written in Python and gives full power and flexibility of SQL to an application developer

- **Marshmallow** - Marshmallow is a Python library that converts complex data types to and from Python data types. It is a powerful tool for both validating and converting data.

- **Psycopg2** - Psycopg2 is a PostgreSQL database driver, it is used to perform operations on PostgreSQL using python

- **JWT** - or JSON Web Token, is an open standard used to share security information between two parties

- **Bcrypt** - BCrypt Algorithm is used to hash and salt passwords securely

<br>

## **Reference**

<br>

Refrence for PEP8 style guidelines
