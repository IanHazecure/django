from django.urls import path
from . import views

urlpatterns =[
    path('main/', views.main, name='main'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/', views.productos, name='productos'),

 ]