#from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

#just sets up what the application will do if a user visits a certain url
urlpatterns = [
    path('', views.index),
    path('order/', views.order, name='order'),
    path('cart/', views.cart, name="cart"),
    path('directions/', views.directions, name='directions'),
    path('hours/', views.hours, name='hours'),
    path('sicilianVSreg/', views.sicilianVSreg, name='sicilianVSreg'),
    path('contact/', views.contact, name='contact')
]