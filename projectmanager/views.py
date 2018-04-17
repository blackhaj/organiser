from django.shortcuts import render
#new
from django.http import HttpResponse
from django.views import generic
from .models import Project, Task

# Create your views here.

def index(request):
    return render(request, 'projectmanager/index.html') #renders the request using the template index.html

class ProjectListView(generic.ListView):
    model = Project

class ProjectDetailView(generic.DetailView):
    model = Project