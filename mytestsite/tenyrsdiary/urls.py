from django.urls import path
from . import views

app_name = 'tenyrsdiary'
urlpatterns = [
    path('', views.index, name='index'),
]