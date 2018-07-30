from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('', views.index),
    path('login/', login, {'template_name': 'account/login.html'}),
    path('logout/', logout, {'template_name': 'account/logout.html'}),
    path('register/', views.register, name='register'),
]