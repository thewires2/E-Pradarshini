from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_main, name='project_main'),
]
