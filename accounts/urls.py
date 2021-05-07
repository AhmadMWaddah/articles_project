from django.urls import path
from . import views

urlpatterns = [
	path('register', views.accountRegister, name='register'),
	path('login', views.accountLogIn, name='login'),
	path('logout', views.accountLogOut, name='logout'),
]
