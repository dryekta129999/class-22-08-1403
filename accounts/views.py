from django.shortcuts import render


# Create your views here.

def user_register(request):
	return render(request, 'accounts/register.html')