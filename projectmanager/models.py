from django.db import models
from datetime import datetime

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True) #null has to be set to True to allow SET_NULL to work
    task_title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    priority_choices = (
        (0, 'Today'),
        (1, 'Tomorrow'),
        (2, 'Later'),
    )
    priority = models.IntegerField(choices=priority_choices, default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
