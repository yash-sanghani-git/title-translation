from django.urls import path
from .views import *
  
urlpatterns = [
    path('single-language/',home),
    path('all-language/',translator),
]