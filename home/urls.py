from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('surveillance', views.surveillance, name='surveillance'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

]
