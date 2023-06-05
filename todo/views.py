from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(username=self.request.user)
        context['taskscount'] = context['tasks'].filter(finish=False).count()
        search = self.request.GET.get('searchbar') or ''
        if search:
            context['tasks'] = context['tasks'].filter(title__icontains=search)
        return context


class Detail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'detailtask'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'finish']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'deletetask'
    success_url = reverse_lazy('tasks')


class Login(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class Register(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        username = form.save()
        if username is not None:
            login(self.request, username)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(Register, self).get(*args, **kwargs)