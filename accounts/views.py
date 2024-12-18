from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User


# Create your views here.

# def user_register(request):
# 	if request.method == 'POST':
# 		pass
# 	else:
# 		form = UserRegisterForm()
# 		return render(request, 'templates/register.html', {'form': form})





def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            User.objects.create_user(
                user_name=data['username'],
                email=data['email'],
                password_2=data['password'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['username'],


            )
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
