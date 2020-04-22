from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import loader

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")

def welcome(request, name):        
    return render(request,'sampleweb/welcome.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def friends_list(request):
    friends = ["Ajay", "Ashvini", "Omprakash", "Nabajyoti", "Chandrasekhar", "Mahendra"]
    return render(request, "sampleweb/friends-list.html",{
        'friends':friends 
    })

# another way to render template
def about(request):
    t = loader.get_template('sampleweb/about.html')
    data = {
        'description':"this is about page description"
    }
    return HttpResponse(t.render(data, request))

# redirecting to about page
def contact(request):
    return redirect('/about')
