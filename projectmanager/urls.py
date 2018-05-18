from django.urls import path
from . import views

app_name = 'projectmanager'
urlpatterns = [
    path('', views.OverView.as_view(), name='overview'), #directs to index method in views.py
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-details'),
    path('projects/new/', views.ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/update', views.ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete', views.ProjectDeleteView.as_view(), name='project-delete'),
    path('tasks/', views.TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-details'),
    path('tasks/new/', views.TaskCreate.as_view(), name='task-create'),
    path('tasks/<int:pk>/update', views.TaskUpdate.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete', views.TaskDelete.as_view(), name='task-delete')
    # path('projects/new/', views.add_new_project, name='add-new-project'),
]