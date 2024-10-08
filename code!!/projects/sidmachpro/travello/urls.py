from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'), 
               path('about/', views.about, name='about'),
               path('destinations/', views.destinations, name='destinations'),
               path('contact/', views.contact, name='contact'),
               path('news/', views.news, name='news')]