from django.contrib import admin
from django.urls import path
from group import views

'''
    'name=' is used for reverse linking which is efficient for dynamic routing
'''
urlpatterns = [
    path('', views.index, name='index'),
]