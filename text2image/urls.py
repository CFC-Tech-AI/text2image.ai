from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("text2image/", text2image, name="text2image"),
     
]