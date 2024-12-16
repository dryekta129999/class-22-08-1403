from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [

	path('register/', views.user_register, name='user_register'),
	# path('login/', views.user_login, name='user_login'),
	# path('logout/', views.user_logout, name='user_logout'),
	# path('profile/', views.user_profile, name='user_profile'),
	# path('change_password/', views.change_password, name='change_password'),
	# path('reset_password/', views.reset_password, name='reset_password'),
	# path('reset_password_sent/', views.reset_password_sent, name='reset_password_sent'),
	# path('reset_password_change/', views.reset_password_change, name='reset_password_change'),
	# path('reset_password_complete/', views.reset_password_complete, name='reset_password_complete'),
	# path('change_email/', views.change_email, name='change_email'),
	# path('change_email_sent/', views.change_email_sent, name='change_email_sent'),
	# path('change_email_complete/', views.change_email_complete, name='change_email_complete'),

]