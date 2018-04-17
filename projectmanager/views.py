from django.shortcuts import render
#new
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Project, Task
from django.urls import reverse_lazy
# from .forms import NewProjectForm

# Create your views here.

def index(request):
    return render(request, 'projectmanager/index.html') #renders the request using the template index.html

class ProjectListView(generic.ListView): #change ProjectListView to ProjectList
    model = Project

class ProjectDetailView(generic.DetailView):
    model = Project

class ProjectCreateView(generic.CreateView):
    model = Project
    fields = ['project_name']

class ProjectUpdateView(generic.UpdateView):
    model = Project
    fields = '__all__'

class ProjectDeleteView(generic.DeleteView):
    model = Project
    success_url = reverse_lazy('projectmanager:project-list')



# def add_new_project(request):
#     if request.method == 'POST':
#         form = NewProjectForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/projectmanager/projects/') #hopefully back to index
#     else:
#         form= NewProjectForm()
    
#     return render(request, 'projectmanager/project_form.html', {'form': form})