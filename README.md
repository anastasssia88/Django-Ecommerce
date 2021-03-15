# Django-Ecommerce-Website
This is an educational project meant to teach how to build dynamic web application using Django, Postgresql, CLI and to deploy on Heroku

# Functionality built:
Login, logout, user profile, user cart, user checkout, guest cart, guest checkout, add to cart, list view of products, detail view of each product

#Dependencies
asgiref==3.3.1
dj-database-url==0.5.0
Django==3.1.3
django-crispy-forms==1.10.0
django-heroku==0.3.1
gunicorn==20.0.4
Pillow==8.0.1
psycopg2==2.8.6
pytz==2020.4
sqlparse==0.4.1
whitenoise==5.2.0

#Run server
python manage.py runserver

#Commands for updating DB
python manage.py makemigrations
python manage.py migrate
