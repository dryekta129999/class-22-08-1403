
from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(forms.Form):
	user_name=forms.CharField(max_length=20,)
	email = forms.EmailField(required=True)
	first_name = forms.CharField(max_length=20)
	last_name = forms.CharField(max_length=20)
	password_1 = forms.CharField(widget=forms.PasswordInput)
	password_2 = forms.CharField(widget=forms.PasswordInput)

	def save(self):
		pass

# user_name = forms.CharField(label='Username', widget=forms.TextInput())



