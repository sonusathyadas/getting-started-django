# Django Tutorial - Getting started with Django

## Setting up Python Virtual Environment in VS Code
-------------
To create and run Django projects you can use a Virtual environment. Using a virtual environment avoids installing Django into a global Python environment and gives you exact control over the libraries used in an application. In virtual environment you can create a `requirements.txt` to reproduce files of virtual environement  to another development environment. 

Follow the steps to setup the Django project in VS Code:
1) Create a folder  "djangoweb" in your development machine. 
2) Open command prompt and set "djangoweb" as current working directory
3) Run the following command to create a virtual environment 
	> `python -m venv env`
4) Open project folder in VS code by running 
	code .
5) In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the `Python: Select Interpreter command`:
6) It lists the available Python interpreters in the current environment. It lists globally installed python and virtual environment python in `env` folder. Select the virtual env python. (`eg: .\env\Scripts\Python.exe`)
7) Open the integrated terminal .Ensure the default terminal type is `Command Prommpt`. It activates the Python environment using the activation script automatically.
8) Install Django in the virtual environment by running one of the following commands in the VS Code Terminal:	
	> `python -m pip install django`
9) You now have a self-contained environment ready for writing Django code. VS Code activates the environment automatically when you use `Terminal: Create New Integrated Terminal`.

## Create a simple Django project
In Django terminology, a "Django project" is composed of several site-level configuration files along with one or more "apps" that you deploy to a web host to create a full web application. A Django project can contain multiple apps, each of which typically has an independent function in the project, and the same app can be in multiple Django projects.

To create a minimal Django app, then, it's necessary to first create the Django project to serve as the container for the app, then create the app itself. For both purposes, you use the Django administrative utility, `django-admin`, which is installed when you install the Django package.

1) In the VS Code Terminal where your virtual environment is activated, run the following command:
	> `django-admin startproject website .`
2)  creates the following within it:
	* **manage.py**: The Django command-line administrative utility for the project. You run administrative commands for the project using python manage.py <command> [options].
	* A subfolder named `website`, which contains the following files:
		* **__init__.py**: an empty file that tells Python that this folder is a Python package.
		* **wsgi.py**: an entry point for WSGI-compatible web servers to serve your project. You typically leave this file as-is as it provides the hooks for production web servers.
		* **settings.py**: contains settings for Django project, which you modify in the course of developing a web app.
		* **urls.py**: contains a table of contents for the Django project, which you also modify in the course of development.
3) To test the project is created and running successfully, Open the terminal (make sure it is in python venv) and run the following command.	
	> `python manage.py runserver`
4) The project will run and the server will listen on localhost port number 8000. Open browser and navigate to the url.
	```Watching for file changes with StatReloader
	Performing system checks...

	System check identified no issues (0 silenced).

	You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, 
	auth, contenttypes, sessions.
	Run 'python manage.py migrate' to apply them.
	April 22, 2020 - 11:03:23
	Django version 3.0.5, using settings 'website.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CTRL-BREAK.
	```
5) When you run the project for the first time it creates a `db.sqlite3` file. We will discuss about this file later.
6) Close the browser and press `Ctrl+C` to stop the server.

## Create a web app in the Django Project

To add a new Django web app to the project you have created, follow the steps:
1) Open the VS Code Integrated Terminal. Ensure that the terminal is in virual environment. Run the following command to create a new web app in the Django project.
	```
	python manage.py startapp sampleweb
	```
2) The command creates a folder called `sampleweb` that contains a number of code files and one subfolder.
	* **views.py** - contains the functions that define pages in your web app
	* **models.py** - contains classes defining your data objects
	* **migrations folder** - used by Django's administrative utility to manage database versions. 
	* **apps.py** - app configuration
	* **admin.py** - creating an administrative interface
	* **tests.py** -  tests for the application
3) Open the `views.py` file and update the content to add a method to handle the requests for home page. Add an import statement to import the `HttpResponse` from the `django.http` module.
	```
	from django.http import HttpResponse

	def home(request):
	    return HttpResponse("Hello, Django!")
	```
4) Create a new file in `samplewebsite` folder with the name `urls.py`. The `urls.py` file is where you specify patterns to route different URLs to their appropriate views. The code below contains one route to map root URL of the app ("") to the views.home function that you just added to `sampleweb/views.py`. Add the following code to `urls.py`:
	```
	from django.urls import path
	from sampleweb import views

	urlpatterns=[
    	path("", views.home)
	]
	```
5) The `website` project folder also contains a `urls.py` file, which is where URL routing is actually handled. Open `website/urls.py` and modify it to match the following code. This code pulls in the app's `sampleweb/urls.py` using `django.urls.include`, which keeps the app's routes contained within the app. This separation is helpful when a project contains multiple apps.
	```
	from django.contrib import admin
	from django.urls import path, include

	urlpatterns = [
    	path('admin/', admin.site.urls),
    	path('', include('sampleweb.urls'))
	]
	```
6) In the VS Code Terminal, again with the virtual environment activated, run the development server with `python manage.py runserver` and open a browser to `http://127.0.0.1:8000/` to see a page that renders "Hello, Django".

## Using templates to render the views
It is a best practice to use the HTML templates to render the views. It reduces the chance of Cross Site Scripting (XSS) attacks. In Django, a template is an HTML file that contains placeholders for values that the code provides at run time. The Django templating engine then takes care of making the substitutions when rendering the page, and provides automatic escaping to prevent XSS attacks.

1) In the `website/settings.py` file, locate the `INSTALLED_APPS` list and add the name of the web application you created, `ie: sampleweb` , which makes sure the project knows about the app so it can handle templating:
	```
	INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sampleweb'
	]
	```
2) Inside the `sampleweb` folder, create a folder named `templates`, and then another subfolder named `sampleweb` to match the app name.
3) In the `templates/sampleweb` folder, create a file named `welcome.html` with the contents below. This template contains two placeholders for data values named `"name"`, and `"date"`, which are delineated by pairs of curly braces, `{{` and `}}`. As you can see, template placeholders can also include formatting, the expressions after the pipe `|` symbols, in this case using Django's built-in *date* filter and *time* filter.
	```
	<!DOCTYPE html>
	<html>
		<head>
			<meta charset="utf-8" />
			<title>Hello, Django</title>
		</head>
		<body>
			<strong>Hello there, {{ name }}!</strong> It's {{ date | date:"l, d F, Y" }} at {{ date | time:"H:i:s" }}
		</body>
	</html>
	```
4) At the top of `views.py`, add the following import statement:
	```
	from django.shortcuts import render
	```
5) Also, in `views.py` file add a new view method `welcome` with the following code. It uses the `render` from `django.shorcuts` module to render the view with a model object. A url parameter `name` is passed to the `welcome` page. We will configure the route in the `urls.py` file. 
	```
	def welcome(request, name):
    	return render(request,'sampleweb/welcome.html',
			{
            	'name': name,
            	'date': datetime.now()
        	})
	```
6) Open the `sampleweb\urls.py` file and add a new route to the route collection.
	```
	urlpatterns=[
    	path("", views.home),
    	path("welcome/<name>", views.welcome)
	]
	```
7) Run the application by running the `python manage.py runserver` command. Open browser and test the url `http://localhost:8000/welcome/guest`.

## Serving static files
Static files are pieces of content that your web app returns as-is for certain requests, such as CSS files. Serving static files requires that the `INSTALLED_APPS` list in `settings.py` contains `django.contrib.staticfiles`, which is included by default.

1) In the project's `website/urls.py`, add the following import statement:
 	```
	from django.contrib.staticfiles.urls import staticfiles_urlpatterns
	 ```
2) In that same file, add the following line at the end, which includes standard static file URLs to the list that the project recognizes:
	```
	urlpatterns += staticfiles_urlpatterns()
	```
3) In the `static/sampleweb` folder, create a file named `site.css` with the following contents.
	```
	.message {
    	font-weight: 600;
    	color: blue;
	}
	```
4) In templates/sampleweb/welcome.html, add the following lines after the &lt;title&gt; element. The `{% load static %}` tag is a custom Django template tag set, which allows you to use `{% static %}` to refer to a file like the stylesheet.
	```
	{% load static %}
	<link rel="stylesheet" type="text/css" href="{% static 'sampleweb/site.css' %}" />
	```
5) Update the body of the `templates/sampleweb/welcome.html` with the following:
	```
	<body>
        <p class="message">
            <strong>Hello there, {{ name }}!</strong> 
        </p>
        <p>It's {{ date | date:"l, d F, Y" }} at {{ date | time:"H:i:s" }}</p>
    </body>
	```
6) Run the application and test the url `http://localhost:8000/welcome/guest`

## Static files in production server
In production, Django will collect all static files from all applications in the project and put into a separate location. So we can use a dedicated static file server that improves the performance of the application. To do so, we need to run the `python manage.py collectstatic` command to put all files in to a specific location. This is required only when you deploy the application in production server, in development, we serve static files from application specific locations. 
1) In `website/settings.py`, add the following line that defines a location where static files are collected when you use the collectstatic command:
	```
	 STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
	 ```
2)  the Terminal, run the command `python manage.py collectstatic` and observe that `sampleweb/site.css` is copied into the top level `static_files` folder alongside `manage.py`.
3) In practice, run `collectstatic` any time you change static files and before deploying into production.

## Common layout for view templates 
In web applications, multiple view pages will share a set of common elements such as navigation hyperlinks, headers, sidebar contents and footers. It will be difficult to manage the changes of those shared elements in all view if they are independently defined in each views. Django allows us to create a common layout template and inherit it to other view templates. Let's see how to setup a common layout for our web application.

A base page template in Django contains all the shared parts of a set of pages, including references to CSS files, script files, and so forth. Base templates also define one or more block tags with content that extended templates are expected to override. A block tag is delineated by `{% block <name> %}` and `{% endblock %}` in both the base template and extended templates.

1) In the `templates/sampleweb` folder, create a file named `layout.html` with the contents below, which contains blocks named "title" and "content". 
	```
	<!DOCTYPE html>
	<html>
	<head>
		<meta charset="utf-8"/>
		<title>{% block title %}{% endblock %}</title>
		{% load static %}
		<link rel="stylesheet" type="text/css" href="{% static 'sampleweb/site.css' %}"/>
	</head>

	<body>
	<div class="navbar">
		<a href="{% url 'home' %}" class="navbar-brand">Home</a>
		<a href="{% url 'about' %}" class="navbar-item">About</a>
		<a href="{% url 'contact' %}" class="navbar-item">Contact</a>
	</div>

	<div class="body-content">
		{% block content %}
		{% endblock %}
		<hr/>
		<footer>
			<p>Sample Django website</p>
		</footer>
	</div>
	</body>
	</html>
	```
2) For styling add the following css styles in `static\sampleweb\site.css` file.
	```
	.navbar {
		background-color: lightslategray;
		font-size: 1em;
		font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
		color: white;
		padding: 8px 5px 8px 5px;
	}

	.navbar a {
		text-decoration: none;
		color: inherit;
	}

	.navbar-brand {
		font-size: 1.2em;
		font-weight: 600;
	}

	.navbar-item {
		font-variant: small-caps;
		margin-left: 30px;
	}

	.body-content {
		padding: 5px;
		font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
	}
	```
3) Update the `templates\welcome.html` with the following code. You will define the `title` block and `content` blocks with proper html contents.
	```
	{% extends "sampleweb/layout.html" %}
	{% block title %}
		Welcome - SampleWeb
	{% endblock %}
	{% block content %}
		<p class="message">
			<strong>Hello there, {{ name }}!</strong>
		</p>
		<p>It's {{ date | date:"l, d F, Y" }} at {{ date | time:"H:i:s" }}</p>
	{% endblock %}
	```
4) Run the application and navigate to the `http://localhost:8000/welcome/guest` url. You will see the navigation bar with hyperlinks and footer. You can repeat the step 3 for applying layout to all pages. 

## Working with data models and database migrations
In Django, a model is a Python class, derived from `django.db.models.Model`, that represents a specific database object, typically a table. You place these classes in an app's `models.py` file.
Your work on databases are done using the models defined using the code. Whenever you update the models you can perform a Django 'migration' operation to sync the changes to the database. It contains the following operations. 
1. Make changes to the models in your `models.py` file.
2. Run `python manage.py makemigrations` to generate scripts in the migrations folder that migrate the database from its current state to the new state.
3. Run `python manage.py migrate` to apply the scripts to the actual database.

The migration scripts effectively record all the incremental changes you make to your data models over time. By applying the migrations, Django updates the database to match your models. Because each incremental change has its own script, Django can automatically migrate any previous version of a database (including a new database) to the current version. You can use the Django administrative utility `loaddata` to perform database initializations after the migration is completed. 

When using the `db.sqlite3` file, you can also work directly with the database using a tool like the `SQLite browser`. It's fine to add or delete records in tables using such a tool, but avoid making changes to the database schema because the database will then be out of sync with your app's models. Instead, change the models, run `makemigrations`, then run `migrate`. 

> Note: When you deploy the application in multi-server environmet or while performing scaling and geo-replication it is adviced to use some other databases instead of the `SQLite`. SQLite is good for development purpose or applications that have less data traffic typically less than 199K per day.

### Django models
A Django model is again a Python class derived from `django.db.model.Models`, which you place in the app's `models.py` file. In the database, each model is automatically given a unique ID field named `id`. All other fields are defined as properties of the class using types from `django.db.models` such as `CharField` (limited text), `TextField` (unlimited text), `EmailField`, `URLField`, `IntegerField`, `DecimalField`, `BooleanField`, `DateTimeField`, `ForeignKey` and `ManyToMany`. 

Each field takes some attributes, like `max_length`. The `blank=True` attribute means the field is optional; `null=true` means that a value is optional. There is also a `choices` attribute that limits values to values in an array of data value/display value tuples.

1) Open the `sampleweb\models.py` file and update the code with the following 
	```
	from django.db import models

	# Create your models here.

	class Todo(models.Model):
		title = models.CharField(max_length=250)
		is_done = models.BooleanField(default=False)

		def __str__(self):
			"""Returns the string representation of the todo object"""
			return f"Title={self.title} , Completed = {self.is_done}"

	```
2) Open the Terminal in the virutual environment and run the following command
	> python manage.py makemigrations
3) Run the migration command to update the model changes to database.
	> python manage.py migrate
4) You can see the migration files generated in the `migrations` folder.
5) Add a form page to the app through which you can add a todo item. You then modify the home page to display those todo items. In the `sampleweb` folder (where the views.py is located), create a new file `forms.py` and add the following code to it.
	```
	from sampleweb.models import Todo
	from django import forms

	class TodoForm(forms.ModelForm):
		class Meta:
			model = Todo
			fields = ('title', 'is_done')
	```
6) Open the `views.py` and add a new method for handling the add todo GET and POST actions.
	```
	def add_todo(request):
    form = TodoForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():            
            todoitem = form.save(commit=False) # save posted data to todo model object
            print(todoitem)            
            todoitem.save()
            return redirect("home")
    else:
        return render(request, "sampleweb/add-todo.html", {"form": form})
	```
7) Now, you need to add a new route to the `urls.py` file. 
	```
	path("todo/", views.add_todo, name="addtodo")
	```
8) Open the `templates\sampleweb\layout.html` and add a new hyperlink in the navigation bar.
	```
	<a href="{% url 'addtodo' %}" class="navbar-item">Add Todo</a>
	```
9) Run the application and navigate to `http://localhost:8000/todo`. Provide the value for title and is_done and submit. The data will be saved to the database using the `add_tod` view method and redirects to `home` view.
10) You can now make changes in your model and execute migrations to sync the changes with database. Open the `models.py` and add a new field to `Todo` model.
	```
	added_date = models.DateTimeField(null=True)
	```
11) Run the following commands to generate migration files and execute it
	> python manage.py makemigrations
	> python manage.py migrate

12) This will add a new column to the table. You also need to update the `add_todo` method in the `views.py` as follows. We will explicitly add the current time to the field `added_date`. In the `forms.py` we dont need to include the `added_date` in the fields list as it does not require a textbox field to accept value from user.
	```
	def add_todo(request):
		form = TodoForm(request.POST or None)

		if request.method == "POST":
			if form.is_valid():       
				try:     
					todoitem = form.save(commit=False)            
					todoitem.added_date = datetime.now() # add the current date, not a field in form					
					todoitem.save()
					return redirect("home")
				except IntegrityError as e:
					print(e)
					return render(request,"sampleweb/add-todo.html", {"form": form})
		else:
			return render(request, "sampleweb/add-todo.html", {"form": form})
	```
13) Re-run the application and test the add todo page.

14) Open the `views.py` and add a new class called `HomeListView`. HomeListView class inherit the `django.views.generic.ListView` class. Import the ListView class in the `views.py` file. You also requires to import the `Todo` model from `sampleweb.models`.
	```
	from django.views.generic import ListView
	from sampleweb.models import Todo
	```
15) Add the `HomeListView` class in `views.py` file
	```
	class HomeListView(ListView):
		"""Renders the home page, with a list of all todos."""
		model = Todo

		def get_context_data(self, **kwargs):
			context = super(HomeListView, self).get_context_data(**kwargs)
			return context
	```
16) In the app's urls.py, import the data model:
	```
	from sampleweb.models import Todo
	```
17) Also in `urls.py`, make a variable for the new view, which retrieves the five most recent Todo objects in ascending order, and then provides a name for the data in the template context (todo_list), and identifies the template to use:
	```
	home_list_view = views.HomeListView.as_view(queryset=Todo.objects.order_by("added_date")
    	,context_object_name="todo_list",
    	template_name="sampleweb/home.html")

	```
18) In `urls.py`, modify the path to the home page to use the `home_list_view` variable:
	```
    # Replace the existing path for ""
    path("", home_list_view, name="home"),
	```
19) Start the app and open a browser to the home page, which should now display list of todos.
