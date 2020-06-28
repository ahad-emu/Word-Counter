from django.urls import path
from WordCounterApp import views

urlpatterns = [
    path("", views.homepage, name="index"),
    path("counter/", views.wordcounter, name="counter"),
]
