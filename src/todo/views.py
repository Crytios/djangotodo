from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm, CreateForm
from django.contrib.auth.models import User

# Create your views here.
from .models import Todo

class CustomLoginView(LoginView):
	template_name = "login.html"
	model = User
	redirect_authenticated_user = True
	def get_success_url(self):
		print('ewfkwjeefjnkjnkj')
		return reverse_lazy('todoapp')

class CustomRegisterView(CreateView):
	form_class = SignUpForm
	template_name = "registration.html"
	success_url = reverse_lazy('login')
	

class TodoView(LoginRequiredMixin,ListView):
	model = Todo
	template_name = "todo/todo_list.html"
	context_object_name = 'todos'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['todos'] = context['todos'].filter(user=self.request.user)
		return context

class TodoCreate(LoginRequiredMixin,CreateView):
	template_name = "todo/todo_list_create.html"
	model = Todo
	form_class = CreateForm
	#fields = '__all__'
	success_url = reverse_lazy('todoapp')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(TodoCreate, self).form_valid(form)

class TodoDelete(LoginRequiredMixin,DeleteView):
	template_name = "todo/todo_list_delete.html"
	model = Todo
	context_object_name ="todo"
	success_url = reverse_lazy('todoapp')


