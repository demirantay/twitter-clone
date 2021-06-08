dropdb twitter_clone
createdb twitter_clone
virtualenv venv
venv/bin/pip install django
venv/bin/pip install Pillow
venv/bin/pip install psycopg2
venv/bin/python manage.py makemigrations
venv/bin/python manage.py migrate
venv/bin/python manage.py createsuperuser
