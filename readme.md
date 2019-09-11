# API Documentation

### Installation / Getting Started

Create a virtualenv using python3

`virtualenv -p python3 env`

Activate your virtualenv

`source env/bin/activate`

Install all dependencies

`pip install -r requirements.txt`



Carry out the database migrations (Django app uses a sqlite3 file-based db)

`python manage.py migrate`



Run the development server

`python manage.py runserver`



### Endpoints

`http://127.0.0.1:8000/api/v1/` 

Lists all urls of the API. Base url of API



`GET http://127.0.0.1:8000/api/v1/todoitems/` 

Lists all todo list items

Response: 

```json
{
    "count": 0,
    "next": null,
    "previous": null,
    "results": [
        {
            "title": "Complete project",
            "description": "Need to complete project for school",
            "status_of_task": "Not Started",
            "due_date": "2019-09-12"
        }
    ]
}
```



`POST http://127.0.0.1:8000/api/v1/todoitems/` 

Creates a todo item. 

Body format:

```json
{
    "title": "Title  here",
    "description": "some description",
    "status_of_task": "Not Started",
    "due_date": "2019-09-12"
}
```

