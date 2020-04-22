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
	>  python manage.py startapp sampleweb

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
	> from django.shortcuts import render
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
 	> `from django.contrib.staticfiles.urls import staticfiles_urlpatterns`
2) In that same file, add the following line at the end, which includes standard static file URLs to the list that the project recognizes:
	> `urlpatterns += staticfiles_urlpatterns()`
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
	> STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
2)  the Terminal, run the command `python manage.py collectstatic` and observe that `sampleweb/site.css` is copied into the top level `static_files` folder alongside `manage.py`.
3) In practice, run `collectstatic` any time you change static files and before deploying into production.
