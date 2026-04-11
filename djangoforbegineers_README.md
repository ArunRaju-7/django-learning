ORM (Object-Relational Mapper): write Python rather than raw SQL for creating and querying database tables
Authentication: a full-featured and secure system for user accounts, groups, permissions, and cookie-based user sessions
Templating Engine: a simple syntax for adding variables and logic to create dynamic HTML
Forms: a powerful form library that handles rendering and validation
URL Routing: a clean, elegant URL schema that is easy to maintain and reason about
Admin Interface: a visual way to interact with all website data, including users and database tables
Internationalization: multilingual support plus locale-specific formatting of dates, time, numbers, and time zones
Security: protection against SQL injection, cross-site scripting, cross-site request forgery, clickjacking, and remote code execution


Chapter 1 : Initial Setup

python -m pip install django~=5.0.0

django-admin startproject django_project ch01-setup

1. manage.py
Command-line utility for Django
Used for:
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser

2. django_project/__init__.py
Makes it a Python package

django_project/settings.py
Main configuration file
Includes:
- Database config
- Installed apps
- Middleware
- Static files config

django_project/urls.py
Root URL routing
Maps URLs → views

django_project/wsgi.py
Used for deployment (WSGI servers like Gunicorn)

django_project/asgi.py
Used for async servers (WebSockets, async frameworks)


At its core, a web framework like Django has three main tasks:

Map URLs to view logic for rendering pages

What happens
- User hits: /hello/
- Django checks urls.py
- Calls say_hello() function
- Returns response

Provide an abstraction layer for interacting with a database

- Django converts Python → SQL
- Executes query
- Returns Python objects

Display HTML-like code via a templating system

- Django loads template
- Replaces {{ name }} with value
- Sends final HTML to browser

1. User hits URL
2. urls.py decides which view
3. View:
   - talks to DB (ORM)
   - prepares data
   - sends to template
4. Template renders HTML
5. Response goes back to browser

Django:
urls.py     → Routing (URL → View mapping)
views.py    → Controller (NOT really service layer)
models.py   → Database schema (tables)
ORM         → Converts Python ↔ SQL
templates   → Presentation layer (HTML rendering)


Django Architecture:

Web browser -> HTTP Request -> Django -> URL Dispatcher -> view -> model -> database
                                                        -> template
    
Web browser <- HTTP Request <- Django <- URL Dispatcher <- view <- model <- database
                                                        <- template

Django's approach is sometimes called Model-View-Template (MVT), but is more accurately a 4-part pattern incorporating URL configuration, Model-View-Template-URL (MVTU):

Model: Manages data and core business logic
View: Describes which data is sent to the user but not its presentation
Template: Presents the data as HTML with optional CSS, JavaScript, and static assets
URL Configuration: Regular expression components configured to a View
The "View" in MVC is analogous to a "Template" in Django, while the "Controller" in MVC is divided into a Django "View" and "URL dispatcher."

Migrations:
-----------
Migrations are special scripts Django creates automatically to track changes to the database. As a project grows over time, there are often many changes to the Django database models that define the structure of a database and all its tables. The Django migrations framework allows developers to track changes over time and change the database to match the configurations within a specific migrations file.

When you start a new project using the startproject command, Django includes several built-in apps (more on what an app is shortly) that make changes to the database, including admin, auth, contenttypes, and sessions. We can apply these changes to the local database using the management command, migrate.

admin.py is a configuration file for the built-in Django Admin app
apps.py is a configuration file for the app itself
migrations/ keeps track of any changes to our models.py file so it stays in sync with our database
models.py is where we define our database models, which Django automatically translates into database tables
tests.py is for app-specific tests
views.py is where we handle the request/response logic for our web app


python manage.py makemigrations --empty yourapp
for preserve old data on a column

python manage.py migrate yourapp zero
👉 Drops all tables of that app

python manage.py migrate yourapp 0001
👉 Rolls DB back to that version

python manage.py migrate --fake-initial
If table already exists → mark migration as applied
If not → run normally

python manage.py migrate pages 0002 --fake
Migration → ❌ DB unchanged → django_migrations updated