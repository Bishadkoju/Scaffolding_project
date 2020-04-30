from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .models import ProjectRegister
from .forms import addProjectForm
from .filters import ProjectFilter
from django.contrib import messages


# Create your views here.

class ProjectCreateView(SuccessMessageMixin,generic.CreateView):
    model=ProjectRegister
    template_name='project/project_add.html'
    form_class=addProjectForm
    success_url=reverse_lazy('dashboard')
    success_message="Project added Successully !!"
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['action']='Add'
        context['title']='Add Project'
        return context

class ProjectUpdateView(SuccessMessageMixin,generic.UpdateView):
    model=ProjectRegister
    form_class=addProjectForm
    template_name='project/project_add.html'
    success_message="Project Updated Successfully"
    success_url= reverse_lazy('dashboard')
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['action']='Update'
        context['title']='Update Project'
        return context


class ProjectListView(generic.ListView):
    model=ProjectRegister
    paginate_by=10
    context_object_name='project_list'
    template_name='project/project_list.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['filter']=ProjectFilter(self.request.GET,self.get_queryset())
        return context


class ProjectDetailView(generic.DetailView):
    model=ProjectRegister
    context_object_name='project'
    template_name='project/project_detail.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['action']='Detail'
        context['title']='Project Detail'
        return context

class ProjectDeleteView(SuccessMessageMixin,generic.DeleteView):
    model=ProjectRegister
    context_object_name='project'
    template_name='project/project_detail.html'
    success_message="Project Deleted Successfully"
    success_url=reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['action']='Delete'
        context['title']='Delete Project'
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

