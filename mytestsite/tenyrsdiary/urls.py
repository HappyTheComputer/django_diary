from django.urls import path
from . import views

app_name = 'tenyrsdiary'
urlpatterns = [
    path('', views.toDay, name='index'),
    path('pre/', views.lastDay, name='pre'),
    path('next/', views.nextDay, name='next'),
    path('input/', views.inputDiary, name='input'),
]