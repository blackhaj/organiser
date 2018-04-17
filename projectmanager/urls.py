from django.urls import path
from . import views

app_name = 'projectmanager'
urlpatterns = [
    path('', views.index, name='index'), #directs to index method in views.py
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-details'),
    path('projects/new/', views.ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/delete', views.ProjectDeleteView.as_view(), name='project-delete'),
    path('projects/<int:pk>/update', views.ProjectUpdateView.as_view(), name='project-update'),

    # path('projects/new/', views.add_new_project, name='add-new-project'),
]