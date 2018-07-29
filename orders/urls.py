#from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('', views.index),
    path('menu/', views.menu, name='menu')
]