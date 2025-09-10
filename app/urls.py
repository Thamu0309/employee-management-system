from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # replace with your view
]
