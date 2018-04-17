from django.urls import path
from . import views

app_name = 'projectmanager'
urlpatterns = [
    path('', views.index, name='index'), #directs to index method in views.py
    path('projects/', views.ProjectListView.as_view(), name='projects'),
]