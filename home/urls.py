from django.conf.urls.static import static
from django.urls import path, include
from .views import *

from home import views

app_name = 'home'

urlpatterns = [
	path('', views.home, name='home'),
]