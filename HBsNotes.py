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

############################ GIT ############################

#Created respository
#then in terminal from the relevent folder
git init
git add .
git commit -m "First Commit"
git remote add origin URL-FOR-THE-ONLINE-REPOSITORY
git -v #varifies the url
git push -u origin master

############################

# linked the main urls to the new app
# setup a urls.py file in the new app then created a generic index one
# Added an index method to the views.py
# Create a templates folder and added index.html

# Created the models

python manage.py makemigrations projectmanager
python manage.py migrate

#NEXT STEP IS TO START CREATING THE CRUD index, create etc methods

#Added some projects and tasks:

python manage.py shell

from projectmanager.models import Project, Task

p = Project(project_name="Spanish")
p.save()
p.id

a = Task(task_title="Task 1", project=Project.objects.get(pk=1))
a.save()
a.id

#and so on

#then created a means of printing which projects had which tasks
def task_printer(project_object):
    print(project_object.project_name)
    task_list = Task.objects.all()
    for task in task_list:
        if task.project == project_obj
            print(task.task_title)
    #better code:
    print(project_object.project_name)
    for task in project_object.task_set.all():
        print(task.task_title)

#iterate through projects and display associated tasks
projects_array = Project.objects.all()
for project in projects_array:
    task_printer(project)

#START TO ADD VIEWS AND URL PATHS

#in the urls file
path('projects/', views.ProjectsListView.as_view(), name='projects'),

#then in the views file
from django.views import generic
from .models import Project, Task

class ProjectListView(generic.ListView):
    model = Project
    #this basic generic view gets all the records for projects, then renders the template at projectmanager/templates/projectmanager/project_list.html (needs to be created). The list can be accessed in the template as object_list or project_list
    #context_object_name = overrides the object list name
    #queryset = overides the query used to create the list
    #template_name = overides the template

#out of order, but at this point I created a main html template

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/css/materialize.min.css">
    <title>Organiser App</title>
</head>
<body>
    <header>
        <h1>Henry Black Web Dev</h1>
    </header>
    <div class="container">
        {% block content %}
        {% endblock %}
        <br>

        <a style="display:block" class="center-align" href="/admin">Admin Login</a>
    </div>
</body>
</html>

#and extended it into the old index one:
{% extends 'projectmanager/main.html' %}

#created a project_list.html template
{% extends 'projectmanager/main.html' %}

{% block content %}
    <h1>Project List</h1>
    
    {% if project_list %}
    <ul>

        {% for project in project_list %}
        <li>
            {{ project.project_name }} ( XX linked tasks) # need to work out this logic
        </li>
        {% endfor %}
    </ul>
    {% else %}
        <p>There currently aren't any projects</p>
    {% endif %}
{% endblock %}

