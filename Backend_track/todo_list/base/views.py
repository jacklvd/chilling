from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login # to avoid login multi-time

from .models import Task

from typing import Any


class Login(LoginView):
    template_name: str = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user: bool = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name: str = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user: bool = True
    success_url = reverse_lazy('tasks')
    
    # render the form
    def form_valid(self, form):
        user = form.save()
        if user is not None: # if user has successfully created
            login(self.request, user) # log the user in
        return super(RegisterPage, self).form_valid(form)
    
    # to prevent see the register/login page after login
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)
    

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name: dict = 'tasks' # for better readable
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        # prevent return list of other user
        context['tasks'] = context['tasks'].filter(user=self.request.user) # to authenticate a specified user
        context['count'] = context['tasks'].filter(complete=False).count()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__startswith=search_input)
        
        context['search_input'] = search_input
            
        return context
        
      
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name: str = 'base/details.html'
    
    
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user = self.request.user # to make it is a login in user
        return super(TaskCreate, self).form_valid(form)    

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    
    
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name: str = 'task'
    template_name: str = 'base/task_delete.html'
    success_url = reverse_lazy('tasks')
