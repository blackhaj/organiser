virtualenv organiseren

source organiserenv/bin/activate

pip install django

#this was additional because I hadn't merged old databases over to the new version
brew postgresql-upgrade-database

createdb organiserdb

psql organiserdb #check it works - exit with \q

django-admin startproject organiser

cd organiser

pip install psycopg2

#change the settings.py DATABASE section to point at the new DB:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'organiserdb',
        'USER': 'blackhaj',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

python manage.py migrate #then add to psequel to check that it is all in place

python manage.py startapp projectmanager #create the project manager app

