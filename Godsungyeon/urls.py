# Godsungyeon/urls.py
from django.urls import path
from . import views

app_name = 'Godsungyeon'

urlpatterns = [
    path('', views.home, name='home'),
]