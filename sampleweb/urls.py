from django.urls import path
from sampleweb import views
from sampleweb.models import Todo

home_list_view = views.HomeListView.as_view(queryset=Todo.objects.order_by("added_date")
    ,context_object_name="todo_list",
    template_name="sampleweb/home.html")

urlpatterns=[
    path("", home_list_view, name= "home"),
    path("welcome/<name>", views.welcome, name="welcome"),
    path("friends", views.friends_list, name="friendslist"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("todo/", views.add_todo, name="addtodo"),
]