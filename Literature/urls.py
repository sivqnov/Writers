from django.urls import path
from .views import *

urlpatterns = [
    path("", mainPage, name='mainPage'),
]
