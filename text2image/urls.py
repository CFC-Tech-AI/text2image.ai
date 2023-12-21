from django.urls import path
from .views import *

urlpatterns = [
    
    path("", text2image, name="text2image"),
     
]