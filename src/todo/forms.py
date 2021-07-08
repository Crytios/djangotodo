from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Todo
class SignUpForm(UserCreationForm):
	username = forms.CharField(max_length=25, required=True)
	class Meta:
		model  = User
		fields = ['username','password1']



class CreateForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ['title']
		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Title Here'},)
		}

# class CustomLoginForm(forms.ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ['username','password']
# 		widgets = {
# 			'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Username Here'},),
# 			'password': forms.TextInput(attrs={'class':'form-control','placeholder':'Password Here'},)
# 		}

