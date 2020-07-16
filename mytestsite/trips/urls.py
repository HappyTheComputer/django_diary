from django.urls import path
from . import views

app_name = 'trips'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
]