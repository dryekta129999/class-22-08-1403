from tkinter.font import names

from django.shortcuts import render
from django.http import HttpResponse
import datetime

from django.template import loader
from django.shortcuts import render
from django.utils import timezone

def home(request):
    context = {
        'mydate': timezone.now(),
    }
    return render(request, 'home.html', context)



# Create your views here.
# def testing(request):
# 	template = loader.get_template('master.html')
# 	context = {
# 		'mydate': datetime.datetime.now(),
# 	}
# 	return HttpResponse(template.render(context, request))


# def home(request):
# 	return render(request, 'home.html')
