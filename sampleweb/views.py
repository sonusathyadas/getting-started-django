from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import loader
from sampleweb.forms import TodoForm
from sqlite3 import IntegrityError

# Create your views here.
def home(request):
    #return HttpResponse("Hello, Django!")
    return render(request, 'sampleweb/home.html')

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

def add_todo(request):
    form = TodoForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():       
            try:     
                todoitem = form.save(commit=False)            
                todoitem.added_date = datetime.now() # add the current date, not a field in form
                print(todoitem.added_date)
                todoitem.save()
                return redirect("home")
            except IntegrityError as e:
                print(e)
                return render(request,"sampleweb/add-todo.html", {"form": form})
    else:
        return render(request, "sampleweb/add-todo.html", {"form": form})
