from django.urls import path
from sampleweb import views

urlpatterns=[
    path("", views.home, name= "home"),
    path("welcome/<name>", views.welcome, name="welcome"),
    path("friends", views.friends_list, name="friendslist"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact")
]