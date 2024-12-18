from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserRegisterForm


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
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
