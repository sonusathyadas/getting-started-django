from django.urls import path
from sampleweb import views

urlpatterns=[
    path("", views.home),
    path("welcome/<name>", views.welcome),
    path("friends", views.friends_list),
    path("about", views.about),
    path("contact", views.contact)
]