# elemements_task
## Setting
A customer would like to have a native mobile application that displays a simple data set, coming from a
spreadsheet. This document can be updated anytime by the client itself, so our API has to be resilient.
The data consists of:
Image
Title
Description (optional)
The spreadsheet is accessible as a CSV file through the following link: https://docs.google.com
/spreadsheet/ccc?
key=0Aqg9JQbnOwBwdEZFN2JKeldGZGFzUWVrNDBsczZxLUE&single=true&gid=0&output=csv

## Task
Because the CSV could potentially be moved to another location, replaced by another one or it could be
temporally unavailable an API should be implemented in between. Build a RESTful JSON API in Django t
hat will be used by the mobile application to fetch the CSV contents.
Things to take into consideration:
The CSV and its contents are not reliable.
The CSV could grow very big in size.
The frontend, at least, has to be able to get the list of entries and the details of a single one.
Include clear instructions on how to run it.
Include unit tests.
Bonus points:
Have a dockerized setup.
Think of this as a real project that will go to production.
A good cache strategy.
Remarks
No need to build everything by yourself, you can use your favourite libraries!
PLEASE don't make the solution public anywhere (private repositories on Github or similar
are OK)

## Solutions
I decide to create two solutions:
- simple serialize solution: app just to create quick and easy way of getting data with DRF
- API different versions solution: app with ability to keep different versions of API, using paginators and so on  

## Architecture
- Docker: each part of architecture is a microservice, that dockerized with docker and docker-compose.yml;
- Web application: Django application;
- DB: To give more flexibility PostgresQL installed instead of SQLite; 
- Pgadmin: additional service for administrating DB;
- Celery: used for manage task for adding data from csv file
- Redis: is a broker for all task managed with Celery
- Pytest: test for the whole project
- Unittest: test functionality

## Installation
1. Cit clone the project from github
   $ git clone https://github.com/zamula-soft/elements-task --branch base --single-branch
   $ cd elements_task

2. Build up all containers
   $ docker-compose up -d --build

3. Create superuser for Django
   $ docker-compose exec app python manage.py createsuperuser
    
4. Run all migrations 
   $ docker-compose exec app python manage.py makemigrations
   $ docker-compose exec app python manage.py migrate

5. Run application
   http://0.0.0.0:8000

6. Run tests
   $ docker-compose exec app python manage.py test

## Using 
As result there are following services should start:
1. app - web-application with Django
2. celery - task manager for adding data
3. db - PostgresQL DB instance
4. pgadmin: Service to admin DB

## Simple Serialize Solution
- to open Django: http://0.0.0.0:8000
- to open django admin http://0.0.0.0:8000/admin
- to open api for list of all images: http://0.0.0.0:8000/images
- to open detail view for the image (for example with id=15): http://0.0.0.0:8000/images/15

## API Different Versions Solution
- to open Django: http://0.0.0.0:8000
- to open django admin http://0.0.0.0:8000/admin
- to open API get list: 0.0.0.0:8000/api/v1/images/ 
- to open API get detail (for example with id=15): 0.0.0.0:8000/api/images/15

## Additional
Additional services can be implemented:
- Swagger: openapi - description of all API functions. Example of openapi.yaml is included.
   to open swagger-schema: http://0.0.0.0:8000/openapi/
- Postman: service for testing API endpoints and results


