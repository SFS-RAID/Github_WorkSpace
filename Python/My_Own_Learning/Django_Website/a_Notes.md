# Notes for a Django Server

**INITIATION:** To start your project, type the following command in the terminal:<br> **python manage.py startproject *ProjectName***

**INITIATION:** To Start a app, type:
 > **python manage.py startapp *AppName***

 **INITIATION:** To Start the Server, type:
 > **python manage.py runserver**

### Show your app when someone Types the AppURL
 - open *ProjectName*/urls.py
 - Add this to the imports:
   > **from django.urls import path, include**
 - To the first path, Add this:
   > **path(*'AppURL/'*, include(*Appname*.urls))**<br> # You can Decide a name for your AppURL
  - Go to **ProjectName/settings.py** and add the config

### Create an webpage
In Your app, open views.py and create a view by typing **def *PageName*(request)**
 - If you just want to return text, type this: <br>
  > from django.http import HttpResponse <br>**def *ViewName*(request):**<br>**return HttpResponse('*Your text Here*')**

 - If you want to return an HTML page, *Create a folder named '**templates**' in your App-Folder and Create a HTML file in it*
 Then, type<br>
 > from django.shortcuts import render<br>from .models import ModelName<br>**def *ViewName*(request):**<br>**return render(request, *Path to HTML file*)**
### Show the webage to the user when the user types the SubURL
 - Create 'urls.py' in your app
 - In it, Type the following as a template: 
   > **from django.urls import path
from * import views
urlpatterns = [
path('*TheSub-URL*, views.*YourViewName*')
// Note: The first path should be the index(appmainpage), The SubURL Should be empty
]**

### Create a Model
 - Go to ***AppName*/models.py**
 - Create a class
   > **class *ModelName*(models.Model):
   *CharAtt* = models.CharField(max_length=255)
   *IntAtt* = models.IntegerField()
   *FloatAtt* = models.FloatField()**
 - Go to ***AppName*/apps.py**
 - Remember the AppNameConfig
   > **class *AppName*Config(AppConfig)**
 - Go to ***ProjectName*/settings.py** and to the installed apps, add
     > ***AppName*.apps.AppNameConfig**
 - Type the following Commands in the Terminal
   > **python manage.py makemigrations
   python manage.py migrate**

### Admin Panel
 -  #### Create a admin
    - Run this command and enter the details
      > python manage.py createsuperuser
    - You can now Login using the details
 - #### Show the Models in Admin Panel
    - Open ***AppName*/admin.py** and write this
      > from .models import *ModelName*
      **admin.site.register(*ModelName*)**
 - #### Show the preview for the models in Admin Panel
    - In the **admin.py** file, write:
      > **class *ModelName*Admin(admin.ModelAdmin):
      list_display = ('Att1', 'Att2', 'Att3')**
    - In the AdminSiteRegister,  add the paramater like this:
      > **admin.site.register(*ModelName*, *ModelName*Admin)**
  - #### Show the Models in the WebPage
    - Go to *AppName/*views.py and write this
      > from .models import ModelName
      **def ViewName(request):
      *AllModelName = ModelName.objects.all()*
return render(request, Path to HTML file, {'AllObjectsClassName' = AllModelName})**
// Note: You can choose the AllModelName and AllObjectsClassName and both can be the same name
    - Go to the HTML File(The path you typed in the ViewFunction) you want to show your model and type(NOTE: This is an example):
      > **<*ul*>
      {% for SingleModel in AllObjectsClassName %}
      <*li*>{{AOCN.Att1}} (${{AOCN.Att}})
      <*ul*>**