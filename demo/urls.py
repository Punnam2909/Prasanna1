from django.urls import path
from .views import Home,punnam,ramala,intial,category

urlpatterns = [
    path("home/",Home,name="Home"),
    path("punnam/",punnam,name="punnam"),
    path("ramala/",ramala,name="ramala"),
    path("intial/",intial,name="intial"),
    path("category/<int:id>/",category,name="category"),
]